#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pickle
from sklearn.metrics import classification_report
import merge_train_data_files
import pandas as pd

MODEL_DIR_PATH = './model/'
N_MODEL = 14

def load_model(filename_in):
    f = open(filename_in, 'r')
    classifier = pickle.load(f)
    f.close()
    return classifier

def transform_words_to_dictvect(words, dict_vectorizer):
    words = dict([x.split(':') for x in words.strip().split(' ')])
    words = dict((k,float(v)) for k,v in words.iteritems())
    words = dict_vectorizer.transform(words)
    
    # Convert to ready-for-train format
    words_dict = dict_vectorizer.inverse_transform(words)
    return words_dict[0]

def model_evaluate(filename_in='./train-data/train-data-all.csv'):
    # Merge all train data files
    merge_train_data_files.merge_all_train_data()
    
    # Load Testing Data
    df = pd.read_csv(filename_in)
    
    # Each model
    for model_id in range(1,N_MODEL+1,1):
        # Load Classification Model
        if model_id not in [1,2,3,5,6,11]:
            continue
        model_file_name = 'model_%02d.pickle' % model_id
        model_file_path = os.path.join(MODEL_DIR_PATH, model_file_name)
        print "Model#%d:" % model_id, model_file_path
        classifier = load_model(model_file_path)
        
        # Load DictVectorizer Model
        dv_model_file_name = 'dictvect_%02d.pickle' % model_id
        dv_model_file_path = os.path.join(MODEL_DIR_PATH, dv_model_file_name)
        DictVec = load_model(dv_model_file_path)
    
        # Classification Report
        y_true = [str(result) for result in df['Category%02d'%model_id]]
        y_pred = []
        for idx in range(len(df)):
            feature = df['words'][idx]
            if pd.isnull(feature):  # Empty words -> predict "0"
                y_pred.append("0")
            else:
                feature = transform_words_to_dictvect(feature, DictVec)
                # print feature
                dist = classifier.prob_classify(feature)
                y_pred.append(dist.max())
        target_names = ['class %02d <no>'% model_id, 'class %02d <yes>'%model_id]
        print(classification_report(y_true, y_pred, target_names=target_names))

if __name__ == '__main__':
    model_evaluate()