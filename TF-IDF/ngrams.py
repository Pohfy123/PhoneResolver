#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from nltk import ngrams

def applyNgramAllDocuments(path_in, path_out, number_of_gram, delimeter='|'):
    for dirpath, dirs, files in os.walk(path_in):
        for f in files:
            finname = os.path.join(dirpath, f)
            foutname = os.path.join(path_out, f)
            print "fname=", finname
            with open(finname) as pearl:
                o = open(foutname, 'w')

                # Read content from a document
                content = pearl.read().decode('utf-8')

                # Split words to array of word
                wordArr = content.encode('utf-8').split(delimeter)

                # Apply N-Gram
                word_ngram = ngrams(wordArr, number_of_gram)

                # Write to file
                for w in word_ngram:
                    gram = "".join(w)
                    o.write(gram+"\n")
                o.close()


input_path  = './split/'
output_path = './split_out/'
number_of_gram = 3
delimeter = '|'
applyNgramAllDocuments(input_path, output_path, number_of_gram, delimeter)
