#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.bogotobogo.com/python/NLTK/tf_idf_with_scikit-learn_NLTK.php
import sys

import nltk
import string
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

path = './split_out/'
path_result = './result/'
token_dict = {}


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems

for dirpath, dirs, files in os.walk(path):
    for f in files:
        fname = os.path.join(dirpath, f)
        print("fname=", fname)
        with open(fname,encoding="utf-8-sig") as pearl:
            text = pearl.read()
            # Create a dictionary using a comprehension - this maps every character from
            # string.punctuation to None. Initialize a translation object from it.
            translator = str.maketrans({key: None for key in string.punctuation})
            # token_dict[f] = text.lower().translate(translator)
            token_dict[f] = text

tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())

for dirpath, dirs, files in os.walk(path):
    for f in files:
        fname = os.path.join(dirpath, f)
        foutname = os.path.join(path_result, f)
        print("result: fname=", fname)
        o = open(foutname, 'w', encoding="utf8")
        with open(fname,encoding="utf-8-sig") as pearl:
            text = pearl.read()
            # print(inp_str.encode("utf-8"))
            response = tfidf.transform([text])
            print(response)

            feature_names = tfidf.get_feature_names()
            for col in response.nonzero()[1]:
                # print(feature_names[col], ' - ', response[0, col])
                o.write(  str(feature_names[col])+' - '+str(response[0, col])+'\n'  )
        o.close()