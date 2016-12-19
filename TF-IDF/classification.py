#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
import pickle
import os

import bing_search
import urlKeywordSearch
import wordParser_LexTo
import ngrams
import extract_feature
import merge_test_data_to_csv

def load_model(filename_in):
    f = open(filename_in, 'rb')
    classifier = pickle.load(f)
    f.close()
    return classifier

def processData(filename_in='./number_input.txt'):
    ## Processing Data
    bing_search.runBingSearch(filename_in)
    urlKeywordSearch.search()
    wordParser_LexTo.parseAllDocuments()
    ngrams.applyNgramAllDocuments()
    extract_feature.extract_feature()
    merge_test_data_to_csv.mergeResultToCSV()

def predict(filename_in='./number_input.txt',filename_out='./result/prediction.csv'):
    # processData(filename_in)
    all_words = []
    with open('./model/word_list.txt') as pearl:
        words = pearl.read().strip()
        all_words = words.split(" ")

    MODEL_FILE_PATH = './model/'
    for dirpath, dirs, files in os.walk(MODEL_FILE_PATH):
        # Each Class folder 
        for f in files:
            fin_path = os.path.join(dirpath, f)
            fin_name = os.path.splitext(os.path.basename(fin_path))[0]
            fin_ext = os.path.splitext(os.path.basename(fin_path))[1]
            if fin_ext != '.pickle':
                continue
            print "model: fname=", fin_name
            classifier = load_model(fin_path)
            with open('./temp-processing-data/05_merge-csv/test_data.csv','r') as fin:
                for line in fin:
                    num,words = line.split(",")
                    test_word = words.split(" ")
                    test_sent_features = {word: (word in test_word) for word in all_words}
                    dist = classifier.prob_classify(test_sent_features)
                    with open(filename_out, 'a') as file_out:
                        file_out.write(num + ',' + dist.max() + '\n')

predict()