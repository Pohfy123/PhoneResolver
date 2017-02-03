#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from nltk import ngrams
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

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

## Old Ngram (1 Ngram)
def applyNgramAllDocuments(path_in='./temp-processing-data/02_parsed-word-data-lexto/', path_out='./temp-processing-data/03_n-gram-data-lexto/', number_of_gram=2, delimeter='|'):
    done_list = []
    for dirpath, dirs, files in os.walk(path_out):
        for f in files:
            fin_ext = os.path.splitext(os.path.basename(f))[1]
            if fin_ext == '.txt':
                done_list.append(f)
    
    for dirpath, dirs, files in os.walk(path_in):
        for f in files:
            # Skip done list
            if(f in done_list):
                continue
            fin_path = os.path.join(dirpath, f)
            _, fin_ext = os.path.splitext(os.path.basename(fin_path))
            if fin_ext != '.txt':
                continue
            
            finname = os.path.join(dirpath, f)
            foutname = os.path.join(path_out, f)
            # print "fname=", finname
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



def applyNewNgramAllDocuments(path_in='./temp-processing-data/02_parsed-word-data-lexto/', path_out='./temp-processing-data/03_n-gram-data-lexto/', number_of_gram=2, delimeter='|'):
    done_list = []
    for dirpath, dirs, files in os.walk(path_out):
        for f in files:
            fin_ext = os.path.splitext(os.path.basename(f))[1]
            if fin_ext == '.txt':
                done_list.append(f)
    
    for dirpath, dirs, files in os.walk(path_in):
        for f in files:
            # Skip done list
            if(f in done_list):
                continue
            fin_path = os.path.join(dirpath, f)
            _, fin_ext = os.path.splitext(os.path.basename(fin_path))
            if fin_ext != '.txt':
                continue
            
            finname = os.path.join(dirpath, f)
            foutname = os.path.join(path_out, f)
            # print "fname=", finname
            with open(finname) as pearl:
                o = open(foutname, 'w')

                # Read content from a document
                content = pearl.read().decode('utf-8')

                # Split words to array of word
                document = [content]

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

                thDocArr = []
                thaiDocument = ('|').join(thaiWordArr)
                thDocArr.append(thaiDocument)

                ngram_word_list = []
                # Apply N-Gram
                if len(thaiWordArr) != 0:
                    ngram_word_list = backOffNgram(thDocArr)           

                for word in engWordArr:
                    ngram_word_list.append(word)
                o.write('\n'.join(ngram_word_list))
                o.close()

def tok(str):
    return str.split('|')

## fake back-off
def backOffNgram(document, ngram_max = 2):
    vectorizer = CountVectorizer(ngram_range=(1, ngram_max), tokenizer=tok)

    # Don't need both X and transformer; they should be identical
    new_doc = [doc.decode('utf-8','ignore') for doc in document]
    X = vectorizer.fit_transform(new_doc)
    matrix_terms = np.array(vectorizer.get_feature_names())
    return [matrix_term.replace(' ','').encode('utf-8','ignore') for matrix_term in matrix_terms]