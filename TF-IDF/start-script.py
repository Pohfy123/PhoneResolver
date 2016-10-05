#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wordParser_PyICU
import ngrams
import extract_feature
import numberSearchMain

# Configuration
path_number = "number_input.txt"
path_raw_data = './temp-processing-data/01_raw-data/'
path_parsed_words = './temp-processing-data/02_parsed-word-data/'
path_ngram_words = './temp-processing-data/03_n-gram-data/'
path_result_tf = './result/tf/'
path_result_tfidf = './result/tf-idf/'
number_of_gram = 3
delimeter = '|'

# STEP1: Google Crawling
print "\n\n############# RUN STEP1: Google Crawling #############"
numberSearchMain.searchPhoneNumber(path_number,path_raw_data)

# STEP2: Thai Parser (PyICU)
print "\n\n############# RUN STEP2: Thai Parser (PyICU) #############"
wordParser_PyICU.parseAllDocuments(path_raw_data, path_parsed_words, delimeter)

# STEP3: N-Gram
print "\n\n############# RUN STEP3: N-Gram #############"
ngrams.applyNgramAllDocuments(path_parsed_words, path_ngram_words, number_of_gram, delimeter)

# STEP4: Extract Feature (TF / TF-IDF)
print "\n\n############# RUN STEP4: Extract Feature (TF & TF-IDF) #############"
extract_feature.extract_feature(path_ngram_words, path_result_tf, feature_mode=1) # TF
extract_feature.extract_feature(path_ngram_words, path_result_tfidf, feature_mode=2) # TF-IDF