#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
import pickle

import bing_search
import urlKeywordSearch
import wordParser_LexTo
import ngrams
import extract_feature
# import merge_test_data_to_csv

def load_model(filename_in='my_classifier.pickle'):
    f = open(filename_in, 'rb')
    classifier = pickle.load(f)
    f.close()
    return classifier

def predict(filename_in='./number_input.txt',filename_out='./result/prediction.csv'):
    # BING Search
    bing_search.runBingSearch(filename_in)
    urlKeywordSearch.search()
    wordParser_LexTo.parseAllDocuments()
    ngrams.applyNgramAllDocuments()
    extract_feature.extract_feature()
    # merge_test_data_to_csv.mergeResultToCsv()

predict()