#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import os
import bing_search
import urlKeywordSearch
import wordParser_LexTo
import ngrams
import extract_feature
import merge_test_data_to_csv
from collections import defaultdict
import time

MODEL_DIR_PATH = './model/'
N_MODEL = 4 # Edit here

known_category_phone_number = {}
new_format_input_path = './new_number_input.txt'
unknown_number_input_path = './unknown_number_input.txt'

def import_yellow_pages_db(file_name_in="./yellowpages.csv"):
    is_first_line = True
    phone_cat = {}
    with open(file_name_in) as pearl:
        for line in pearl:
            if is_first_line:
                is_first_line = False
                continue
            alldata = line.split(',')
            phone_num = alldata[1]
            # print phone_num
            sub_cat = alldata[3]
            is_airline = True if alldata[4] == '1' else False 
            is_accommodation = True if alldata[5] == '1' else False 
            is_tourism = True if alldata[6] == '1' else False 
            is_restaurant = True if alldata[7] == '1' else False 

            if phone_cat.get(phone_num, "empty") == "empty":
                phone_cat[phone_num] = {'airline':[],'accommodation':[],'tourism':[],'restaurant':[],'other':[]}
            if is_airline:
                phone_cat[phone_num]['airline'].append(sub_cat)
            if is_accommodation:
                phone_cat[phone_num]['accommodation'].append(sub_cat)
            if is_tourism:
                phone_cat[phone_num]['tourism'].append(sub_cat)
            if is_restaurant:
                phone_cat[phone_num]['restaurant'].append(sub_cat)
            if not is_airline and not is_accommodation and not is_tourism and not is_restaurant:
                phone_cat[phone_num]['other'].append(sub_cat)
    return phone_cat

def load_model(filename_in):
    f = open(filename_in, 'r')
    classifier = pickle.load(f)
    f.close()
    return classifier

def import_test_data(filename='./temp-processing-data/05_merge-csv/test_data.csv'):
    featuresets = []
    mobile_no = []
    with open(filename,'r') as fin:        
        for line in fin:
            num,words = line.split(",",1)
            
            phone_no = num.strip()
            if len(words.strip())==0:
                words = dict()
            else:
                words = dict([x.split(':') for x in words.strip().split(' ')])
                words = dict((k,float(v)) for k,v in words.iteritems())
            
            featuresets.append(words)
            mobile_no.append(num)
    return (mobile_no, featuresets)

def processData(filename_in='./number_input.txt'):
    bing_search.runBingSearch(filename_in)
    urlKeywordSearch.search()
    wordParser_LexTo.parseAllDocuments(path_in='./temp-processing-data/01_raw-data-keyword/')
    ngrams.applyNgramAllDocuments()
    extract_feature.extract_feature()
    merge_test_data_to_csv.mergeResultToCSV()

def check_yellowpages(filename_in):
    phone_cat = {}
    fout = open(unknown_number_input_path,'w')
    with open(filename_in) as pearl:
        for num in pearl:
            num = num.strip()
            # print 'num',num
            # print 'num in known',known_category_phone_number[num]
            # print 'known',known_category_phone_number
            if num in known_category_phone_number:
                # print 'yes'
                phone_cat[num] = known_category_phone_number[num]
            else:
                fout.write(num+'\n')
    return phone_cat

def change_format_phone(file_name_in):
    fout = open(new_format_input_path,'w')
    with open(file_name_in) as pearl:
        for num in pearl:
            num = num.strip()
            if len(num) == 9:
                fout.write(num[0:2]+'-'+num[2:5]+'-'+num[5:9]+'\n')
            elif len(num) == 10:
                fout.write(num[0:3]+'-'+num[3:6]+'-'+num[6:10]+'\n')
            else:
                fout.write(num+'\n')                

def predict(filename_in='./number_input.txt',filename_out='./results/result.csv'):
    change_format_phone(filename_in)
    phone_cat = check_yellowpages(new_format_input_path)
    # print phone_cat
    processData(unknown_number_input_path)
    result = defaultdict(list)
    
    # Each model
    for model_id in range(1,N_MODEL+1,1):        
        # Load Classification Model
        model_file_name = 'sklearn_model_%02d.pickle' % model_id
        # model_file_name = 'model_%02d.pickle' % model_id
        model_file_path = os.path.join(MODEL_DIR_PATH, model_file_name)
        print "Model#%d:" % model_id, model_file_path
        classifier = load_model(model_file_path)
        
        # Load Testing Data
        mobile_no, test_data = import_test_data()

        proba_list = classifier.predict_proba(test_data)

        for row_i in len(test_data):
            this_mobile_no = mobile_no[row_i]
            if test_row['words'] == {}:
                result[this_mobile_no].append('0')
                print 'phone number : ', test_row['phone_no']
                print 'NOT FOUND'
            else:
                dist = classifier.prob_classify(test_row['words'])
                diff = abs(proba_list[row_i][1]-proba_list[row_i][0])
                if diff < 0.2:
                    result[this_mobile_no].append(proba_list[row_i][1])
                else:
                    result[this_mobile_no].append(proba_list[row_i][1])
            
                # Show Prediction Result
                print 'phone number : ', test_row['phone_no']

    # Write Result
    with open(filename_out, 'w') as file_out:
        CATEGORY = ['Airline','Accommodation','Tourism','Restaurant & Delivery']
        for cat in CATEGORY:
            file_out.write(','+cat)
        for cat in CATEGORY:
            file_out.write(',subcat_'+cat)
        file_out.write(',other,\n')
        key_str_list = result.keys()
        value_str_list = [','.join(result_row) for result_row in result.values()]
        pair_str_list = zip(key_str_list, value_str_list)

        result_str_list = [','.join(row) for row in pair_str_list]
        file_out.write('\n'.join(result_str_list))
        file_out.write('\n')
        for num_key in phone_cat:
            # print '>>', num_key
            file_out.write(num_key+','+('1' if len(phone_cat[num_key]['airline'])>0 else '0') +\
            ','+ ('1' if len(phone_cat[num_key]['accommodation'])>0 else '0') +\
            ','+ ('1' if len(phone_cat[num_key]['tourism'])>0 else '0') +\
            ','+ ('1' if len(phone_cat[num_key]['restaurant'])>0 else '0') + ',' )
            file_out.write('|'.join(phone_cat[num_key]['airline']))
            file_out.write(',')
            file_out.write('|'.join(phone_cat[num_key]['accommodation']))
            file_out.write(',')
            file_out.write('|'.join(phone_cat[num_key]['tourism']))
            file_out.write(',')
            file_out.write('|'.join(phone_cat[num_key]['restaurant']))
            file_out.write(',')
            file_out.write('|'.join(phone_cat[num_key]['other']))
            file_out.write('\n')



            
    print "Success :: Result is saved !"
    
    return dict(result)


if __name__ == '__main__':
    dt = time.strftime("%Y%m%d_%H-%M",time.localtime())
    filename_out = './results/result'+dt+'.csv'
    known_category_phone_number = import_yellow_pages_db()
    result = predict(filename_out=filename_out)