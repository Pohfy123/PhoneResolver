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

def load_model(filename_in):
    f = open(filename_in, 'r')
    classifier = pickle.load(f)
    f.close()
    return classifier

def import_test_data(filename='./temp-processing-data/05_merge-csv/test_data.csv'):
    datasets = []
    with open(filename,'r') as fin:        
        for line in fin:
            num,words = line.split(",",1)
            
            phone_no = num.strip()
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


def processData(filename_in='./number_input.txt'):
    bing_search.runBingSearch(filename_in)
    urlKeywordSearch.search()
    wordParser_LexTo.parseAllDocuments(path_in='./temp-processing-data/01_raw-data-keyword/')
    ngrams.applyNgramAllDocuments()
    extract_feature.extract_feature()
    merge_test_data_to_csv.mergeResultToCSV()

def predict(filename_in='./number_input.txt',filename_out='./results/result.csv'):
    processData(filename_in)
    result = defaultdict(list)
    
    # Each model
    for model_id in range(1,N_MODEL+1,1):        
        # Load Classification Model
        model_file_name = 'model_%02d.pickle' % model_id
        model_file_path = os.path.join(MODEL_DIR_PATH, model_file_name)
        print "Model#%d:" % model_id, model_file_path
        classifier = load_model(model_file_path)
        
        # Load DictVectorizer Model
        dv_model_file_name = 'dictvect_%02d.pickle' % model_id
        dv_model_file_path = os.path.join(MODEL_DIR_PATH, dv_model_file_name)
        DictVec = load_model(dv_model_file_path)
        
        # Load Testing Data
        test_data = import_test_data()

        for test_row in test_data:
            if test_row['words'] == {}:
                result[test_row['phone_no']].append('0')
                print 'phone number : ', test_row['phone_no']
                print 'NOT FOUND'
            else:
                dist = classifier.prob_classify(test_row['words'])
                diff = abs(dist.prob('1')-dist.prob('0'))
                if diff < 0.2:
                    result[test_row['phone_no']].append(str(dist.prob('1')))
                else:
                    result[test_row['phone_no']].append(str(dist.prob('1')))
            
                # Show Prediction Result
                print 'phone number : ', test_row['phone_no']
                print 'prediction :', dist.max()
                for label in dist.samples():
                    print "\tlabel >>>",label," prob >>>" , dist.prob(label)

    # Write Result
    with open(filename_out, 'w') as file_out:
        CATEGORY = ['01_Airline','02_Accommodation','03_Tourism','04_Restaurant & Delivery']
        for cat in CATEGORY:
            file_out.write(','+cat)
        file_out.write('\n')
        key_str_list = result.keys()
        value_str_list = [','.join(result_row) for result_row in result.values()]
        pair_str_list = zip(key_str_list, value_str_list)

        result_str_list = [','.join(row) for row in pair_str_list]
        file_out.write('\n'.join(result_str_list))
    print "Success :: Result is saved !"
    
    return dict(result)


if __name__ == '__main__':
    dt = time.strftime("%Y%m%d_%H-%M",time.localtime())
    filename_out = './results/result'+dt+'.csv'
    result = predict(filename_out=filename_out)