#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wordParser_PyICU
import wordParser_LexTo
import ngrams
import extract_feature
import numberSearchMain

# Configuration
path_number = "number_input.txt"
path_raw_data = './temp-processing-data/01_raw-data/'
# path_parsed_words_PyICU = './temp-processing-data/02_parsed-word-data-pyicu/'
# path_ngram_words_PyICU = './temp-processing-data/03_n-gram-data-pyicu/'
# path_result_tf_PyICU = './result/tf-pyicu/'
# path_result_tfidf_PyICU = './result/tf-idf-pyicu/'
path_parsed_words_Lexto = './temp-processing-data/02_parsed-word-data-lexto/'
path_ngram_words_Lexto = './temp-processing-data/03_n-gram-data-lexto/'
path_result_tf_Lexto = './result/tf-lexto/'
path_result_tfidf_Lexto = './result/tf-idf-lexto/'
number_of_gram = 1
delimeter = '|'

# STEP1: Google Crawling
print "\n\n############# RUN STEP1: Google Crawling #############"
numberSearchMain.searchPhoneNumber(path_number,path_raw_data)

# STEP2: Thai Parser (PyICU)
print "\n\n############# RUN STEP2: Thai Parser (PyICU) #############"
wordParser_LexTo.parseAllDocuments(path_raw_data, path_parsed_words_Lexto, delimeter)

# STEP3: N-Gram
print "\n\n############# RUN STEP3: N-Gram #############"
ngrams.applyNgramAllDocuments(path_parsed_words_Lexto, path_ngram_words_Lexto, number_of_gram, delimeter)

# STEP4: Extract Feature (TF / TF-IDF)
print "\n\n############# RUN STEP4: Extract Feature (TF & TF-IDF) #############"
extract_feature.extract_feature(path_ngram_words_Lexto, path_result_tf_Lexto, feature_mode=1) # TF
# extract_feature.extract_feature(path_ngram_words_Lexto, path_result_tfidf_Lexto, feature_mode=2) # TF-IDF