#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import wordParser_PyICU
import wordParser_LexTo
import ngrams
import extract_feature
import urlKeywordSearch
import wordParser_API

# Configuration
# PyICU
print "processing . . ."
path_url = "./temp-processing-data-for-train/00_url/"
path_raw_data = './temp-processing-data-for-train/01_raw-data/'
path_raw_data_keyword = './temp-processing-data-for-train/01_raw-data-keyword/'
path_raw_data_content = './temp-processing-data-for-train/01_raw-data-content/'
path_parsed_words_PyICU = './temp-processing-data-for-train/02_parsed-word-data-pyicu/'
path_ngram_words_PyICU = './temp-processing-data-for-train/03_n-gram-data-pyicu/'
# Lexto
path_parsed_words_Lexto = './temp-processing-data-for-train/02_parsed-word-data-lexto/'
path_ngram_words_Lexto = './temp-processing-data-for-train/03_n-gram-data-lexto/'
#API
path_parsed_words_api = './temp-processing-data-for-train/02_parsed-word-data-api/'
path_ngram_words_api = './temp-processing-data-for-train/03_n-gram-data-api/'

path_tf = './temp-processing-data-for-train/04_tf/'
path_tfidf = './temp-processing-data-for-train/04_tf-idf/'

number_of_gram = 2
delimeter = '|'

# tokenizer_method = 'API'
tokenizer_method = 'LexTo'
# tokenizer_method = 'PyICU'
include_content = True

# # STEP1: Keyword Crawling
print "\n\n############# RUN STEP1: Text Crawling #############"
urlKeywordSearch.search(path_url,path_raw_data,path_raw_data_keyword,path_raw_data_content,include_content)

if tokenizer_method == 'PyICU':
    # # STEP2: Thai Parser (LexTo)
    print "\n\n############# RUN STEP2: Thai Parser (PyICU) #############"
    wordParser_LexTo.parseAllDocuments(path_raw_data, path_parsed_words_PyICU, delimeter,tokenizer_method=='PyICU')
    # STEP3: N-Gram
    print "\n\n############# RUN STEP3: N-Gram #############"
    ngrams.applyNgramAllDocuments(path_parsed_words_PyICU, path_ngram_words_PyICU, number_of_gram, delimeter)
    # STEP4: Extract Feature (TF / TF-IDF)
    print "\n\n############# RUN STEP4: Extract Feature (TF & TF-IDF) #############"
    extract_feature.extract_feature(path_ngram_words_PyICU, path_tf, feature_mode=1) # TF
    extract_feature.extract_feature(path_ngram_words_PyICU, path_tfidf, feature_mode=2) # TF-IDF
elif tokenizer_method == 'LexTo':
    # # STEP2: Thai Parser (LexTo)
    print "\n\n############# RUN STEP2: Thai Parser (LexTo) #############"
    wordParser_LexTo.parseAllDocuments(path_raw_data, path_parsed_words_Lexto, delimeter, tokenizer_method=='PyICU')
    # # STEP3: N-Gram
    print "\n\n############# RUN STEP3: N-Gram #############"
    ngrams.applyNgramAllDocuments(path_parsed_words_Lexto, path_ngram_words_Lexto, number_of_gram, delimeter)
    # # STEP4: Extract Feature (TF / TF-IDF)
    print "\n\n############# RUN STEP4: Extract Feature (TF & TF-IDF) #############"
    extract_feature.extract_feature(path_ngram_words_Lexto, path_tf, feature_mode=1) # TF
    # #extract_feature.extract_feature(path_ngram_words_Lexto, path_tfidf, feature_mode=2) # TF-IDF
elif tokenizer_method == 'API':
    # # STEP2: Thai Parser (API)
    print "\n\n############# RUN STEP2: Thai Parser (API) #############"
    parseAllDocuments('./temp-processing-data/01_raw-data/', path_out='./temp-processing-data/02_parsed-word-data-api/', delimeter='|')
    # # STEP3: N-Gram
    print "\n\n############# RUN STEP3: N-Gram #############"
    ngrams.applyNgramAllDocuments(path_parsed_words_Lexto, path_ngram_words_Lexto, number_of_gram, delimeter)
    # # STEP4: Extract Feature (TF / TF-IDF)
    print "\n\n############# RUN STEP4: Extract Feature (TF & TF-IDF) #############"
    extract_feature.extract_feature(path_ngram_words_Lexto, path_tf, feature_mode=1) # TF
    # #extract_feature.extract_feature(path_ngram_words_Lexto, path_tfidf, feature_mode=2) # TF-IDF