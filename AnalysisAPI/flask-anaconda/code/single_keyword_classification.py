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
from collections import defaultdict
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


def processData(filename_in='./input.txt'):
    # bing_search.runBingSearch(filename_in)
    # urlKeywordSearch.search()
    # wordParser_API.parseAllDocuments(path_in='./temp-processing-data/01_raw-data-keyword/')
    ngrams.applyNgramAllDocuments(path_in='./temp-processing-data/02_parsed-word-data-api/')
    extract_feature.extract_feature()
    merge_test_data_to_csv.mergeResultToCSV()

def predict(filename_in='./input.txt',filename_out='./results/result.csv'):
    processData(filename_in)
    result = defaultdict(list)
    
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
        test_data = import_test_data()
        # print len(test_data)
        for test_row in test_data:
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

    return dict(result)

def run(input_data):
    start_dt = time.strftime("%Y%m%d_%H-%M",time.localtime())
    print 'start time : ',start_dt
    try:
        data = input_data
    except:
        result = {
            'status': '400', 
            'msg': 'No input'
        }
        print json.dumps(result)
        return result
        sys.exit(1)

    if data['input']['type'] not in ['phone']:
        result = {
            'status': '400', 
            'msg': 'Invalid input type'
        }
        print json.dumps(result)
        return result
        sys.exit(1)
        
    dt = time.strftime("%Y%m%d_%H-%M",time.localtime())
    filename_in = './input_'+dt+'.txt'
    filename_out = './results/result_'+dt+'.csv'
    with open(filename_in, 'w') as file_out:
        file_out.write(data['input']['value'])
    predict_result = predict(filename_in=filename_in, filename_out=filename_out)

    urlList = []
    with open('./temp-processing-data/00_url/'+data['input']['value']+'.txt') as pearl:
        # Read content from a document
        for line in pearl:
            # print '>>>',line
            url,keywords =  line.split("|||")
            urlList.append(url)

    keywordList = []
    with open('./temp-processing-data/04_tf/'+data['input']['value']+'.txt') as pearl:
        # Read content from a document
        count = 0
        for line in pearl:
            # print '>>>',line
            if count > 10:
                break
            keyword,tf =  line.decode('utf-8').split("-")
            keywordList.append(keyword)
            count += 1

    contents = ""
    with open('./temp-processing-data/01_raw-data-keyword/'+data['input']['value']+'.txt') as pearl:
        # Read content from a document
        contents = pearl.read().decode('utf-8')

    categories = []
    for idx, val in enumerate(predict_result[data['input']['value']]):
        num,cat = CATEGORY[idx].split('_')
        categories.append({
            'name':cat,
            'score':val,
            'confidence': 'Yes' if float(val) > 0.5 else 'No'
        })

    # Generate some data to send to PHP
    result = {
        'status': '200', 
        'data': [
            {
                'request':{
                    'input':data['input']['value'],
                    'type':data['input']['type'],
                    'api': 'analyze',
                    'version': '1.0.0',
                    'resolvedPageUrl': urlList              
                },
                'language':"th",
                'result': {
                    'keywords': keywordList,
                    'contents': contents
                },
                'category': categories
            }
        ]
    }
    # print json.dumps(result)
    end_dt = time.strftime("%Y%m%d_%H-%M",time.localtime())
    print 'end time : ',end_dt
    return result


if __name__ == '__main__':
    try:
        data = json.loads(base64.b64decode(sys.argv[1]))
    except:
        result = {
            'status': '400', 
            'msg': 'No input'
        }
        print json.dumps(result)
        sys.exit(1)

    if data['input']['type'] not in []:
        result = {
            'status': '400', 
            'msg': 'Invalid input type'
        }
        print json.dumps(result)
        sys.exit(1)
        
    dt = time.strftime("%Y%m%d_%H-%M",time.localtime())
    filename_in = './input_'+dt+'.txt'
    filename_out = './results/result_'+dt+'.csv'

    with open(filename_in, 'w') as file_out:
        file_out.write(data['input']['value'])
    predict_result = predict(filename_in=filename_in, filename_out=filename_out)

    # Generate some data to send to PHP
    result = {
        'status': '200', 
        'data': [
            {
                'input': data['input'],
                'result': predict_result
            }
        ]
    }
    print json.dumps(result)