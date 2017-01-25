#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.bogotobogo.com/python/NLTK/tf_idf_with_scikit-learn_NLTK.php
import sys
import os
import one_vs_all

def mergeResultToCSV(input_path, output_path, file_name_path="train-model"):

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
        number_dic = {}
        for f in files:
            fin_path = os.path.join(dirpath, f)
            fin_name = os.path.splitext(os.path.basename(fin_path))[0]
            fin_ext = os.path.splitext(os.path.basename(fin_path))[1]
            
            if fin_ext != '.txt':
                continue
            print "result: fname=", fin_name
            # print "===============", fin_path            
            with open(fin_path) as pearl:
                words = []
                for line in pearl:
                    # print ">>>>%s"%line
                    word, freq = line.decode('utf-8').strip().split(" - ")
                    # print freq
                    words.append(word.encode('utf-8')+':'+freq.encode('utf-8'))
                number_dic[fin_name] = [' '.join(words),1]
        
        # one vs all
        total_files = one_vs_all.count_total_files(dirpath,input_path)  
        picked_files = one_vs_all.count_pickfiles(dirpath,total_files,input_path)
    # =============================================================
        for dirpath2, dirs2, files2 in os.walk(input_path):
            # Root dir
            if dirpath2 == input_path or dirpath2 == dirpath:
                continue
            deepestFolderName2 = os.path.split(dirpath2)[-1]
            classId2 = deepestFolderName2.split('_')[0]
            className2 = deepestFolderName2.split('_')[1]
            c = 0
            for f2 in files2:
                if c >= picked_files[classId2]:
                    break
                fin_path = os.path.join(dirpath2, f2)
                fin_name = os.path.splitext(os.path.basename(fin_path))[0]
                fin_ext = os.path.splitext(os.path.basename(fin_path))[1]
                if fin_ext != '.txt':
                    continue
                if fin_name in number_dic:
                    continue    
                # print "f2", f2
                # print ">>>>>>>>>>>>", fin_path
                with open(fin_path) as pearl:
                    words2 = []
                    for line in pearl:
                        # print ">>>>%s"%line
                        word2, freq2 = line.decode('utf-8').strip().split(" - ")
                        # print freq
                        words2.append(word2.encode('utf-8')+':'+freq2.encode('utf-8'))
                    number_dic[fin_name] = [' '.join(words2),0]
                c = c+1
    # ===============================================================

        foutname = os.path.join(output_path, file_name_path+classId+'.csv')
        o = open(foutname, 'w')
        for num in number_dic:
            data_col1 = num # Phone Number
            data_col2 = number_dic[num][0] # Bag of words
            data_col3 = str(number_dic[num][1])
            o.write(data_col1+','+data_col2+','+data_col3)
            o.write('\n')
        o.close()

path_train_data = './train-data/'

mergeResultToCSV(path_train_data, path_train_data)
