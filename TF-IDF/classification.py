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
# import merge_test_data_to_csv

def load_model(filename_in='./model/model_1.pickle'):
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
    # merge_test_data_to_csv.mergeResultToCsv()

def predict(filename_in='./number_input.txt',filename_out='./result/prediction.csv'):
    processData(filename_in)
    all_words = []
    classifier = load_model()
    with open('./model/word_list.txt') as pearl:
        words = pearl.read().strip()
        all_words = words.split(" ")

    with open('./temp-processing-data/05_merge-csv/test_data.csv','r') as fin:
        for line in fin:
            num,words = line.split(",")
            test_word = words.split(" ")
            test_sent_features = {word: (word in test_word) for word in all_words}
            dist = classifier.prob_classify(test_sent_features)
            with open(filename_out, 'w') as file_out:
                file_out.write(num + ',' + dist.max() + '\n')
