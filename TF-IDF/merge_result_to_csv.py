#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.bogotobogo.com/python/NLTK/tf_idf_with_scikit-learn_NLTK.php
import sys
import os

def mergeResultToCSV(input_path, output_path, file_name="train.csv"):
    foutname = os.path.join(output_path, file_name)
    o = open(foutname, 'w')
    number_dic = {}
    for dirpath, dirs, files in os.walk(input_path):
        # Root dir
        if dirpath == input_path:
            print "dirs",dirs
            continue
        deepestFolderName = os.path.split(dirpath)[-1]
        classId = deepestFolderName.split('_')[0]
        className = deepestFolderName.split('_')[1]
        print classId,'\t', className,'\t', dirpath
        # Each Class folder 
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
                number_dic[fin_name] = [' '.join(words),0,0]
    for dirpath, dirs, files in os.walk(input_path):
        # Root dir
        if dirpath == input_path:
            continue
        deepestFolderName = os.path.split(dirpath)[-1]
        classId = deepestFolderName.split('_')[0]
        className = deepestFolderName.split('_')[1]
        for f in files:
            fin_path = os.path.join(dirpath, f)
            fin_name = os.path.splitext(os.path.basename(fin_path))[0]
            fin_ext = os.path.splitext(os.path.basename(fin_path))[1]
            if fin_ext != '.txt':
                continue
            number_dic[fin_name][int(classId)] = 1
    for num in number_dic:
        data_col1 = num # Phone Number
        data_col2 = number_dic[num][0] # Bag of words
        data_col3 = str(number_dic[num][1]) # Result is_travel
        data_col4 = str(number_dic[num][2]) # Result is_restaurant
        o.write(data_col1+','+data_col2+','+data_col3+','+data_col4)
        o.write('\n')
    o.close()

path_train_data = './train-data/'

mergeResultToCSV(path_train_data, path_train_data)
