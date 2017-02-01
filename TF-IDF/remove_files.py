#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

CAT_NAME = 'Airline Companies'

base_path = './temp-processing-data_'+CAT_NAME
input_path = './temp-processing-data_'+CAT_NAME+'/04_tf'
file_arr = []

for f in os.listdir(input_path):
    fin_path = os.path.join(input_path, f)
    fin_name = os.path.splitext(os.path.basename(fin_path))[0]
    fin_ext = os.path.splitext(os.path.basename(fin_path))[1]
    if fin_ext != '.txt':
        continue
    file_arr.append(fin_name)

for dirpath, dirs, files in os.walk(base_path):
    # Root dir
    if dirpath == input_path or dirpath == input_path:
        continue
    for f in files:
        fin_path = os.path.join(dirpath, f)
        fin_name = os.path.splitext(os.path.basename(fin_path))[0]
        fin_ext = os.path.splitext(os.path.basename(fin_path))[1]
        if fin_ext != '.txt':
            continue
        if fin_name not in file_arr:
            os.remove(fin_path)
