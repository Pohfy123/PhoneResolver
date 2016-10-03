#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.bogotobogo.com/python/NLTK/tf_idf_with_scikit-learn_NLTK.php
import sys
import os
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from operator import itemgetter

token_dict = {}

# <<<<<<<<<<<<<<<<<<<<<< TF-IDF : Old source <<<<<<<<<<<<<<<<<<<<<<

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems

def tfidf(input_path, output_path, use_idf=True):
    for dirpath, dirs, files in os.walk(input_path):
        for f in files:
            finname = os.path.join(dirpath, f)
            print "fname=", finname
            with open(finname) as pearl:
                text = pearl.read().decode('utf-8')
                # Create a dictionary using a comprehension - this maps every character from
                # string.punctuation to None. Initialize a translation object from it.
                # translator = str.maketrans({key: None for key in string.punctuation})
                # token_dict[f] = text.lower().translate(translator)
                token_dict[f] = text.encode('utf-8')

    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words=None, use_idf=use_idf)
    tfs = tfidf.fit_transform(token_dict.values())

    for dirpath, dirs, files in os.walk(input_path):
        for f in files:
            finname = os.path.join(dirpath, f)
            foutname = os.path.join(output_path, f)
            print "result: fname=", finname
            o = open(foutname, 'w')
            with open(finname) as pearl:
                text = pearl.read().decode('utf-8')
                # print(inp_str.encode("utf-8"))
                response = tfidf.transform([text.encode('utf-8')])
                # print(response)

                feature_names = tfidf.get_feature_names()
                
                # Create freq table
                keys_freq_table = [str(feature_names[col].encode('utf-8')) for col in response.nonzero()[1] ]
                vals_freq_table = [response[0, col] for col in response.nonzero()[1] ]
                freq_table = zip(keys_freq_table, vals_freq_table)
                
                # Sort by (value) DESC
                sorted_freq_table = sorted(freq_table, key=itemgetter(1), reverse=True)

                # Print to file
                for row in sorted_freq_table:
                    o.write(row[0]+' - '+str(row[1])+'\n')
            o.close()

# >>>>>>>>>>>>>>>>>>>>>> TF-IDF : Old source >>>>>>>>>>>>>>>>>>>>>>

def tf(input_path, output_path):
    tfidf(input_path, output_path, False)

def extract_feature(input_path, output_path, feature_mode) :
    if(feature_mode == 1): # TF
        print('Mode: 1 TF')
        tf(input_path, output_path)
    elif(feature_mode == 2): # TF-IDF
        print('Mode: 2 TF-IDF')
        tfidf(input_path, output_path)
    else:
        print('Wrong parameter: (feature_mode should be 1 or 2)')


input_path  = './split_out/'
output_path = './result/'

feature_mode = 1       # TF
# feature_mode = 2    # TF-IDF

extract_feature(input_path, output_path, feature_mode)