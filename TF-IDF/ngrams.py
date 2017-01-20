#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from nltk import ngrams

def applyNgramAllDocuments(path_in='./temp-processing-data/02_parsed-word-data-lexto/', path_out='./temp-processing-data/03_n-gram-data-lexto/', number_of_gram=2, delimeter='|'):
    for dirpath, dirs, files in os.walk(path_in):
        for f in files:
            fin_path = os.path.join(dirpath, f)
            _, fin_ext = os.path.splitext(os.path.basename(fin_path))
            if fin_ext != '.txt':
                continue
            
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
                ngram_word_list = ["".join(words) for words in word_ngram]
                o.write('\n'.join(ngram_word_list))
                o.close()