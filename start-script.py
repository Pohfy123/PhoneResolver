#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wordParser_PyICU
import ngrams
import extract_feature

# Configuration
path_raw_data       = './raw_data/'
path_parsed_words   = './split/'
path_ngram_words    = './split_out/'
path_result         = './result/'
number_of_gram = 3
delimeter = '|'
feature_mode = 1       # TF
# feature_mode = 2    # TF-IDF

# STEP1: Google Crawling

# STEP2: Thai Parser (PyICU)
wordParser_PyICU.parseAllDocuments(path_raw_data, path_parsed_words, delimeter)

# STEP3: N-Gram
ngrams.applyNgramAllDocuments(path_parsed_words, path_ngram_words, number_of_gram, delimeter)

# STEP4: Extract Feature (TF / TF-IDF)
extract_feature.extract_feature(path_ngram_words, path_result, feature_mode)