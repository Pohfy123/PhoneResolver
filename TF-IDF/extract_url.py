#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

input_path = './temp-processing-data-for-train/write_url'
output_path = './temp-processing-data-for-train/00_url/'
for f in os.listdir(input_path):
    fin_path = os.path.join(input_path, f)
    fin_name = os.path.splitext(os.path.basename(fin_path))[0]
    fin_ext = os.path.splitext(os.path.basename(fin_path))[1]
    if fin_ext != '.txt':
        continue
    with open(fin_path) as pearl:
        c = 1
        for line in pearl:
            print fin_path
            fout = open(output_path+fin_name+'-'+str(c)+'.txt','w')
            fout.write(line)
            fout.close()
            c += 1
