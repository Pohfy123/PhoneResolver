#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
from sklearn import cross_validation
import pickle
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer

result_labels = ['Air Travel Ticket Agencies','Home Stay','Hotel','Travel Bureaus','Bakery Cake','CAT6','CAT7','CAT8','CAT9','CAT10','CAT11','CAT12']

def save_dict_words(words_list, filename_out='word_list.txt'):
    with open('./model/'+filename_out, "w") as outfile:
        outfile.write('\n'.join(words_list))

def save_model(classifier, filename_out='my_classifier.pickle'):
    f = open('./model/'+filename_out, 'wb')
    pickle.dump(classifier, f)
    f.close()
    print 'Model saved ! :: (' + filename_out + ')'


def load_model(filename_in='my_classifier.pickle'):
    f = open('./model/'+filename_in, 'rb')
    classifier = pickle.load(f)
    f.close()
    return classifier


def accuracy_test(datasets, words_set, nfolds=2):
    # Construct each model (each category)
    for result_idx in range( len(datasets[0]['result']) ):
        print "========= TEST FEATURE #%d (%s) =========" % (result_idx+1,result_labels[result_idx]) 
        featuresets = [ ({word: (word in data['words']) for word in words_set}, data['result'][result_idx]) for data in datasets ]
                
        # K-fold cross validation
        cv = cross_validation.KFold(len(featuresets), n_folds=nfolds, shuffle=True, random_state=None)

        scores = []
        idx = 1
        for traincv, evalcv in cv:
            # Train model
            train_data = featuresets[traincv[0]:traincv[len(traincv)-1]]
            classifier = nltk.NaiveBayesClassifier.train(train_data)

            # Evaluate model
            test_data = featuresets[evalcv[0]:evalcv[len(evalcv)-1]]
            score = nltk.classify.accuracy(classifier, test_data)

            # classifier.show_most_informative_features()
            print 'TEST#%d: accuracy: %lf' % (idx, score)
            scores.append(score)
            idx += 1
            break
        print 'TOTAL ACCURACY: %lf' % (sum(scores)/len(scores)) 


def train_model(datasets, words_set):
    # Construct each model (each category)
    for result_idx in range( len(datasets[0]['result']) ):
        print "========= TRAIN FEATURE #%d (%s) =========" % (result_idx+1,result_labels[result_idx]) 
        featuresets = [ ({word: (word in data['words']) for word in words_set}, data['result'][result_idx]) for data in datasets ]
        print "STEP 1: Completed !"
        train_data = featuresets
        classifier = nltk.NaiveBayesClassifier.train(train_data)
        print "STEP 2: Completed !"
        model_name = "model_"+str(result_idx+1)+".pickle"
        save_model(classifier, model_name)
        print "STEP 3: Completed !"

        
def new_train_model(featuresets, results):
    # Construct each model (each category)
    for result_idx in range( len(results[0]) ):
        print "========= TRAIN FEATURE #%d (%s) =========" % (result_idx+1,result_labels[result_idx]) 
        print "STEP 1: Completed !"
        train_data = []
        feature_data = []
        for feature in featuresets:
            feat = {}
            for i in range(len(feature)):
                feat[i]=feature[i]
            feature_data.append(feat)
        train_data_row = min(len(feature_data), len(result)) 
        for i in range(train_data_row):
            train_data.append( [feature_data[i], results[i][result_idx]] )
#         print train_data[0]
#         return
        classifier = nltk.NaiveBayesClassifier.train(train_data)
        print "STEP 2: Completed !"
        model_name = "model_"+str(result_idx+1)+".pickle"
        save_model(classifier, model_name)
        print "STEP 3: Completed !"
        
        
# https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-1-for-beginners-bag-of-words
def desc_words_to_features(desc_words):
    # Initialize the "CountVectorizer" object, which is scikit-learn's
    # bag of words tool.  
    vectorizer = CountVectorizer(analyzer = "word",   \
                                 tokenizer = None,    \
                                 preprocessor = None, \
                                 stop_words = None,   \
                                 max_features = 5000) 

    # fit_transform() does two functions: First, it fits the model
    # and learns the vocabulary; second, it transforms our training data
    # into feature vectors. The input to fit_transform should be a list of 
    # strings.
    train_data_features = vectorizer.fit_transform(desc_words)

    # Numpy arrays are easy to work with, so convert the result to an 
    # array
    train_data_features = train_data_features.toarray()
    
    ## Take a look at the words in the vocabulary
    vocab = vectorizer.get_feature_names()
    vocab = [word.encode('utf-8') for word in vocab]
    save_dict_words(vocab)
    
    return train_data_features



print "Start processing . . ."

all_words = ""
datasets = []
desc_words = []

with open('./train-data/train.csv','r') as fin:
    for line in fin:
        num,words,result_str = line.split(",",2)
        # Split result results = [is_rest, is_travel]
        results = result_str.split(",")
        results = [result.strip() for result in results]
        
        # datasets.append((words,is_travel+""+is_rest))
        datasets.append({
            'phone_no' : num,
            'words' : words.split(" "),
            'result' : results
        })
        
        # Collect all words
        all_words = all_words+" "+words
        
        desc_words.append(words)

# words_set = set(all_words.split(" "))
# print "Number of words in dict :  %d words" % len(words_set)
# save_dict_words(words_set)

# New method
print "Convert (words description of each phone no) to (Features) ::"
train_data_features = desc_words_to_features(desc_words)
print "Completed !"


print "Convert to Pandas DataFrame"
train_datasets = pd.DataFrame(datasets)
train_datasets['words'] = pd.DataFrame(train_data_features.tolist())
print "Completed !"

print "===== Completed All Steps of Training Data ====="