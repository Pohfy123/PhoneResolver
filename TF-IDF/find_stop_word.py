#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import operator

input_path = './train-data'
words = {}

for dirpath, dirs, files in os.walk(input_path):
    # Root dir
    if dirpath == input_path:
        print "dirs",dirs
        continue
    deepestFolderName = os.path.split(dirpath)[-1]
    classId = deepestFolderName.split('_')[0]
    className = deepestFolderName.split('_')[1]
    print classId,'\t', className,'\t', dirpath

    for f in files:
        fin_path = os.path.join(dirpath, f)
        fin_name = os.path.splitext(os.path.basename(fin_path))[0]
        fin_ext = os.path.splitext(os.path.basename(fin_path))[1]
        if fin_ext != '.txt':
            continue
        # print "result: fname=", fin_name
        with open(fin_path) as pearl:
            for line in pearl:
                # print ">>>>%s"%line
                word, freq = line.decode('utf-8').strip().split(" - ")
                # print freq
                if word not in words:
                    words[word] = 0
                words[word] = words[word]+float(freq)

sorted_words = sorted(words.items(), key=operator.itemgetter(1),reverse=True) 


with open("stop words.txt", "a") as myfile:
    for key in sorted_words:
        myfile.write(key[0].encode('utf-8','ignore')+"\n")