#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from nltk import ngrams

def isThai(chr):
    cVal = ord(chr)
    if((cVal >= 3584 and cVal <= 3711) or cVal == 32):
        return True
    return False

def isEnglish(chr):
    cVal = ord(chr)
    if (cVal >= 97 and cVal <= 122 ) or (cVal >= 65 and cVal <= 90) or cVal == 32:
        return True
    return False

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

                # Get Thai words from all words
                thaiWordArr = []
                for word in wordArr:
                    word = word.decode('utf-8')
                    for c in word:
                        if isThai(c):
                            thaiWordArr.append(word.encode('utf-8'))
                            break 

                # Get English words from all words
                engWordArr = [word for word in wordArr if len(word)>0 and isEnglish(word[0])]                
                # print engWordArr

                # Apply N-Gram
                word_ngram = ngrams(thaiWordArr, number_of_gram)

                # Write to file
                ngram_word_list = ["".join(words) for words in word_ngram]
                for word in engWordArr:
                    ngram_word_list.append(word)
                o.write('\n'.join(ngram_word_list))
                o.close()