#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.bogotobogo.com/python/NLTK/tf_idf_with_scikit-learn_NLTK.php
import sys
import os

def mergeResultToCSV(input_path, output_path, file_name="result.csv"):
    foutname = os.path.join(output_path, file_name)
    o = open(foutname, 'w')

    for dirpath, dirs, files in os.walk(input_path):
        for f in files:
            fin_path = os.path.join(dirpath, f)
            fin_name = os.path.splitext(os.path.basename(fin_path))[0]
            fin_ext = os.path.splitext(os.path.basename(fin_path))[1]
            if fin_ext != '.txt':
                continue
            print "result: fname=", fin_name
            with open(fin_path) as pearl:
                words = []
                for line in pearl:
                    # print ">>>>%s"%line
                    word, freq = line.decode('utf-8').strip().split(" - ")
                    # print freq
                    words.append(word.encode('utf-8'))
                data_col1 = fin_name # Phone Number
                data_col2 = ' '.join(words) # Bag of words
                data_col3 = '' # Result
                o.write(data_col1+','+data_col2+','+data_col3)
                o.write('\n')
    o.close()


path_result_tf_PyICU = './result/tf-pyicu/'
path_result_tfidf_PyICU = './result/tf-idf-pyicu/'

path_result_tf_Lexto = './result/tf-lexto/'
path_result_tfidf_Lexto = './result/tf-idf-lexto/'

mergeResultToCSV(path_result_tf_Lexto, path_result_tf_Lexto)