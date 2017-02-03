#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.bogotobogo.com/python/NLTK/tf_idf_with_scikit-learn_NLTK.php
import sys
import os

def mergeResultToCSV(path_in = './temp-processing-data/04_tf', path_out = './temp-processing-data/05_merge-csv', file_name="test_data.csv", limit_count_word=100):
    foutname = os.path.join(path_out, file_name)
    
    o = open(foutname, 'w')
    output_str = ""

    number_dic = {}
    for dirpath, dirs, files in os.walk(path_in):
        for f in files:
            fin_path = os.path.join(dirpath, f)
            fin_name = os.path.splitext(os.path.basename(fin_path))[0]
            fin_ext = os.path.splitext(os.path.basename(fin_path))[1]
            if fin_ext != '.txt':
                continue
            # print "Import test data from :  ", fin_name
            with open(fin_path) as pearl:
                words = []
                count_word = 0
                for line in pearl:
                    if count_word > limit_count_word:
                        break
                    word, freq = line.decode('utf-8').strip().split(" - ")
                    words.append(word.encode('utf-8')+':'+freq.encode('utf-8'))
                    count_word += 1
                    
                data_col1 = fin_name # Phone Number
                data_col2 = ' '.join(words) # Bag of words
                    
                output_str += data_col1+','+data_col2+'\n'
    
    with open(foutname, "a") as outfile:
        outfile.write(output_str)

# mergeResultToCSV()