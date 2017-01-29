#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import glob
import re

def merge_all_train_data(output_file_name='train-data-all.csv'):
    # Get list of training data files
    file_list = glob.glob('./train-data/train-model[0-9]*.csv')

    # Generate columns names
    header_list = []
    for fname in file_list:
        m = re.search(r'./train-data/train-model([0-9]*)\.csv', fname)
        cat_header = 'Category'+m.group(1)
        header_list.append(cat_header)

    # Read files into DataFrames
    dfs = [pd.read_csv(file_list[i], names=['mobile_no','words',header_list[i]]) for i in range(len(file_list))]

    # Merge all DataFrames
    df_final = reduce(lambda left,right: pd.merge(left,right.ix[:,right.columns!='words'],on='mobile_no'), dfs)

    df_final.to_csv('./train-data/'+output_file_name, index=False)

    return df_final

if __name__ == '__main__':
    merge_all_train_data()