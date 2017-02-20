#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import os
import bing_search
import urlKeywordSearch
# import wordParser_LexTo
import wordParser_API
import ngrams
import extract_feature
import merge_test_data_to_csv
from collections import OrderedDict
import time


import sys, json
# Load the data that PHP sent us
import base64


CATEGORY = ['01_Airline','02_Accommodation','03_Tourism','04_Restaurant & Delivery']
MODEL_DIR_PATH = './model/'
N_MODEL = 4 # Edit here

def load_model(filename_in):
    f = open(filename_in, 'r')
    classifier = pickle.load(f)
    f.close()
    return classifier

def import_test_data(input_value,filename='./temp-processing-data/05_merge-csv/test_data.csv'):
    datasets = []
    with open(filename,'r') as fin:        
        for line in fin:
            num,words = line.split(",",1)
            
            phone_no = num.strip()
            if phone_no != input_value.strip():
                continue
            if len(words.strip())==0:
                words = dict()
            else:
                words = dict([x.split(':') for x in words.strip().split(' ')])
                words = dict((k,1.0) for k,v in words.iteritems())
            
            data = {
                'phone_no' : phone_no, # no need
                'words' : words
            }
            datasets.append(data)
    return datasets


def processData_phone_keyword(filename_in='./input.txt'):
    bing_search.runBingSearch(filename_in)
    urlKeywordSearch.search()
    wordParser_API.parseAllDocuments(path_in='./temp-processing-data/01_raw-data-keyword/')
    ngrams.applyNgramAllDocuments(path_in='./temp-processing-data/02_parsed-word-data-api/')
    extract_feature.extract_feature()
    merge_test_data_to_csv.mergeResultToCSV()

def processData_url(filename_in='./input.txt'):
    with open(filename_in) as pearl:
        url = pearl.read()
        fout = open('./temp-processing-data/00_url/'+filename_in,'w')
        fout.write(url+'|||')
        fout.close()
    urlKeywordSearch.search()
    hasKeyword = True
    with open('./temp-processing-data/01_raw-data-keyword/'+filename_in) as pearl:
        keyword = pearl.read().decode('utf-8','ignore').strip()
        if not keyword:
            hasKeyword = False
    if hasKeyword:
        wordParser_API.parseAllDocuments(path_in='./temp-processing-data/01_raw-data-keyword/')
    else:
        wordParser_API.parseAllDocuments(path_in='./temp-processing-data/01_raw-data/')        
    ngrams.applyNgramAllDocuments(path_in='./temp-processing-data/02_parsed-word-data-api/')
    extract_feature.extract_feature()
    merge_test_data_to_csv.mergeResultToCSV()

def processData_text(filename_in='./input.txt'):
    with open(filename_in) as pearl:
        text = pearl.read()
        fout = open('./temp-processing-data/01_raw-data/'+filename_in,'w')
        fout.write(text)
        fout.close()
    wordParser_API.parseAllDocuments(path_in='./temp-processing-data/01_raw-data/')
    ngrams.applyNgramAllDocuments(path_in='./temp-processing-data/02_parsed-word-data-api/')
    extract_feature.extract_feature()
    merge_test_data_to_csv.mergeResultToCSV()

def predict(only_filename_in,input_value,input_type,filename_in='./input.txt',filename_out='./results/result.csv'):
    if input_type in ["phone","keyword"]:
        processData_phone_keyword(filename_in)
    elif input_type == "url":
        processData_url(filename_in)
    else:
        processData_text(filename_in)
    result = OrderedDict([])
    
    # Each model
    for model_id in range(1,N_MODEL+1,1):        
        # Load Classification Model
        model_file_name = 'model_%02d.pickle' % model_id
        model_file_path = os.path.join(MODEL_DIR_PATH, model_file_name)
        # print "Model#%d:" % model_id, model_file_path
        classifier = load_model(model_file_path)
        
        # Load DictVectorizer Model
        dv_model_file_name = 'dictvect_%02d.pickle' % model_id
        dv_model_file_path = os.path.join(MODEL_DIR_PATH, dv_model_file_name)
        DictVec = load_model(dv_model_file_path)
        
        # Load Testing Data
        if input_type in ["phone","keyword"]: 
            test_data = import_test_data(input_value)
        else:
            test_data = import_test_data(only_filename_in)            
        # print len(test_data)
        for test_row in test_data:
            if test_row['phone_no'] not in result:
                result[test_row['phone_no']] = []
            if test_row['words'] == {}:
                result[test_row['phone_no']].append('0')
            else:
                dist = classifier.prob_classify(test_row['words'])
                diff = abs(dist.prob('1')-dist.prob('0'))
                if diff < 0.2:
                    result[test_row['phone_no']].append(str(dist.prob('1')))
                else:
                    result[test_row['phone_no']].append(str(dist.prob('1')))
            # only SINGLE INPUT classification
            # break

    # Write Result
    with open(filename_out, 'w') as file_out:
        for cat in CATEGORY:
            file_out.write(','+cat)
        file_out.write('\n')
        key_str_list = result.keys()
        # print key_str_list
        value_str_list = [','.join(result_row) for result_row in result.values()]
        pair_str_list = zip(key_str_list, value_str_list)

        result_str_list = [','.join(row) for row in pair_str_list]
        file_out.write('\n'.join(result_str_list))
    # print "Success :: Result is saved !"
    
    # output_result = {
    #     'category' : [
    #         {
    #             'name' : CATEGORY[idx],
    #             'score' : result[0][idx]
    #         } for idx in range(  min(N_MODEL, len(result[test_row['phone_no']]))  )
    #     ]
    # }
    return result

def run(input_data):
    start_dt = time.strftime("%Y%m%d_%H-%M",time.localtime())
    print 'start time : ',start_dt
    try:
        data = input_data
        data['input']['value'] = data['input']['value'].encode('utf-8','ignore')
    except:
        result = {
            'status': '400', 
            'msg': 'No input'
        }
        print json.dumps(result)
        return result
        sys.exit(1)

    if data['input']['type'] not in ['phone','keyword','url','text']:
        result = {
            'status': '400', 
            'msg': 'Invalid input type'
        }
        print json.dumps(result)
        return result
        sys.exit(1)
    
    dt = time.strftime("%Y%m%d_%H-%M",time.localtime())
    only_filename_in = 'input_'+dt
    filename_in = './input_'+dt+'.txt'
    filename_out = './results/result_'+dt+'.csv'
    with open(filename_in, 'w') as file_out:
        file_out.write(data['input']['value'])
    predict_result = predict(only_filename_in,data['input']['value'],data['input']['type'],filename_in=filename_in, filename_out=filename_out)
    
    urlList = []
    if data['input']['type'] in ['phone','keyword']:
        with open('./temp-processing-data/00_url/'+data['input']['value']+'.txt') as pearl:
            # Read content from a document
            for line in pearl:
                # print '>>>',line
                url,keywords =  line.decode('utf-8').split("|||")
                urlList.append(url)
    elif data['input']['type'] == "url":
        with open('./temp-processing-data/00_url/'+only_filename_in+'.txt') as pearl:
            # Read content from a document
            for line in pearl:
                # print '>>>',line
                url,keywords =  line.decode('utf-8').split("|||")
                urlList.append(url)

    keywordList = []
    if data['input']['type'] in ['phone','keyword']:
        with open('./temp-processing-data/04_tf/'+data['input']['value']+'.txt') as pearl:
            # Read content from a document
            count = 0
            for line in pearl:
                # print '>>>',line
                if count > 10:
                    break
                keyword,tf =  line.decode('utf-8').strip().split(" - ")
                keywordList.append(keyword)
                count += 1
    else:
        with open('./temp-processing-data/04_tf/'+only_filename_in+'.txt') as pearl:
            # Read content from a document
            count = 0
            for line in pearl:
                # print '>>>',line
                if count > 10:
                    break
                keyword,tf =  line.decode('utf-8').strip().split(" - ")
                keywordList.append(keyword)
                count += 1

    contents = ""
    if data['input']['type'] in ['phone','keyword']:
        with open('./temp-processing-data/01_raw-data-keyword/'+data['input']['value']+'.txt') as pearl:
            # Read content from a document
            contents = pearl.read().decode('utf-8')
    elif data['input']['type'] == "url":
        hasKeyword = True
        with open('./temp-processing-data/01_raw-data-keyword/'+only_filename_in+'.txt') as pearl:
            # Read content from a document
            contents = pearl.read().decode('utf-8').strip()
            if not contents:
                hasKeyword = False                
        if not hasKeyword:
            with open('./temp-processing-data/01_raw-data/'+only_filename_in+'.txt') as pearl:
                # Read content from a document
                contents = pearl.read().decode('utf-8')
    else:
        with open('./temp-processing-data/01_raw-data/'+only_filename_in+'.txt') as pearl:
                # Read content from a document
                contents = pearl.read().decode('utf-8')

    categories = []
    if data['input']['type'] in ['phone','keyword']:    
        for idx, val in enumerate(predict_result[data['input']['value']]):
            num,cat = CATEGORY[idx].split('_')
            categories.append(OrderedDict([
                ('name',cat),
                ('score',val),
                ('confidence', 'Yes' if float(val) > 0.5 else 'No'),
        ]))
    else:
        for idx, val in enumerate(predict_result[only_filename_in]):
            num,cat = CATEGORY[idx].split('_')
            categories.append(OrderedDict([
                ('name',cat),
                ('score',val),
                ('confidence', 'Yes' if float(val) > 0.5 else 'No'),
        ]))

    # sort categories
    def extract_score(json):
        try:
            # Also convert to int since update_time will be string.  When comparing
            # strings, "10" is smaller than "2".
            return float(json['score'])
        except KeyError:
            return 0

    # lines.sort() is more efficient than lines = lines.sorted()
    categories.sort(key=extract_score, reverse=True)

    # Generate some data to send to PHP
    request_json = OrderedDict([
                ('input',data['input']['value']),
                ('type',data['input']['type']),
                ('api', 'analyze'),
                ('version', '1.0.0'),
                ('resolvedPageUrl', urlList)              
            ])
    result_json = OrderedDict([
                ('keywords', keywordList),
                ('contents', contents)
            ])
    data_json = OrderedDict([
            ('request',request_json),
            ('language',"th"),
            ('result', result_json),
            ('category', categories)
    ])
    result = OrderedDict([
        ('status', '200'), 
        ('data', data_json)
    ])
    
    print json.dumps(result)
    end_dt = time.strftime("%Y%m%d_%H-%M",time.localtime())
    print 'end time : ',end_dt
    return result


# if __name__ == '__main__':
#     result = run(sys.argv[1])
#     print json.dumps(result)