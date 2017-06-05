#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk

from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB

from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline

from sklearn.cross_validation import StratifiedKFold
import pickle
import time
from sklearn.feature_extraction import DictVectorizer
import os

import itertools
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, f1_score
from termcolor import colored
import sklearn.datasets

from collections import Counter
import random_over_sampler

SEED = 127
NUMBER_OF_CLASSES = 4 # Edit here
LABEL_NAMES = ['01_Airline','02_Accommodation','03_Tourism','04_Restaurant & Delivery'] ## Edit here
train_data_file_name = './train-data/train_data.csv'

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


def bin_list_to_dec(bin_list):
    return int(''.join(map(str, bin_list)),2)


def k_fold_evaluation(featuresets, labels, nfolds=5):
    datasets = zip(featuresets, labels)
    # print colored("Datasets |N|=%d" % len(featuresets), 'blue', attrs=['bold'])
    # print colored("Class distribution: {}".format(Counter([bin_list_to_dec(label) for label in labels])), 'blue', attrs=['bold'])

    # Stratified K-fold cross validation
    labels_dec = [bin_list_to_dec(y) for y in labels]
    random_state = np.random.RandomState(SEED)
    skf = StratifiedKFold(labels_dec, n_folds=nfolds, random_state=random_state)

    all_avg_classification_reports = ""
    for class_id in range(NUMBER_OF_CLASSES):
        print colored('Evaluate a Model#{} ({}): '.format(class_id+1, LABEL_NAMES[class_id]), 'red', attrs=['bold'])
        this_class_labels = [label[class_id] for label in labels]
        fold_idx = 1
        scores = []
        total_y_test = []
        total_y_pred = []
        start_time = time.time()
        for train_index, test_index in skf:
            print colored("-------- \n > Fold#{}".format(fold_idx), attrs=['bold'])

            # Seperate between training data and test data
            X_train = [featuresets[idx] for idx in train_index]
            y_train = [this_class_labels[idx] for idx in train_index]
            train_data = zip(X_train, y_train)

            X_test = [featuresets[idx] for idx in test_index]
            y_test = [this_class_labels[idx] for idx in test_index]
            test_data = zip(X_test, y_test)

            # print "Train data distribution: {}".format(Counter([bin_list_to_dec(labels[x]) for x in train_index]))
            # print "Test data distribution: {}".format(Counter([bin_list_to_dec(labels[x]) for x in test_index]))

            # Oversampling to adjust class distribution
            # ros = RandomOverSampler()
            # X_resampled, y_resampled = ros.fit_sample(X_train, y_train)
            X_resampled, y_resampled = random_over_sampler.random_over_sample(X_train, y_train)
            X_train = X_resampled
            y_train = y_resampled
            train_data = zip(X_resampled, y_resampled)

            # Train models
            classifier = train_model(train_data)
            y_pred = classifier.predict(X_test)
            
            # Evaluate
            y_pred_int = map(int, y_pred)
            y_test_int = map(int, y_test)
            
            total_y_test.extend(y_test_int)
            total_y_pred.extend(y_pred_int)
            score = f1_score(y_test_int, y_pred_int, average=None)
            # print 'TEST#{}: F1-SCORE: {}'.format(fold_idx, score)
            scores.append(score)
            fold_idx += 1
        # print colored('##############', 'red', attrs=['bold'])
        # print colored('TOTAL Metrics of Model#{}: '.format(class_id+1), 'red', attrs=['bold'])
        this_report = sklearn.metrics.classification_report(total_y_test, total_y_pred)
        # print colored(this_report, 'red')
        # print colored('##############', 'red', attrs=['bold'])
        # print "--- Evaluate a model! ({} secs) ---".format(time.time() - start_time)
        # print '\n'*3
        all_avg_classification_reports += '\n\nModel#{}: \n'.format(class_id+1) + this_report
    print colored(all_avg_classification_reports, 'blue')


def train_model(train_data, is_weighted=False):
    if is_weighted:
        classifier = Pipeline([
            ('vectorizer', DictVectorizer()),
            ('tfidf', TfidfTransformer(use_idf=False)),
            # ('clf', OneVsRestClassifier(MultinomialNB()))])
            ('clf', MultinomialNB())])
    else:
        classifier = Pipeline([
            ('vectorizer', DictVectorizer()),
            ('tfidf', TfidfTransformer(use_idf=False)),
            # ('clf', OneVsRestClassifier(BernoulliNB()))])
            ('clf', BernoulliNB())])
    X_train, y_train = zip(*train_data)
    classifier.fit(X_train, y_train)
    return classifier


def import_training_data(filename, n_class=1):
    featuresets = []
    labels = []
    with open(filename,'r') as fin:        
        for line in fin:
            phone_no, words, results = line.split(",", 2)

            # Skip empty file
            if len(words)==0 or len(results)==0:
                continue
            
            words = dict([x.split(':') for x in words.strip().split(' ')])
            words = dict((k,float(v)) for k,v in words.iteritems())

            results = results.strip().split(",", n_class-1)

            featuresets.append(words)
            labels.append(results)
    
    return (featuresets, labels)

if __name__ == '__main__':
    print 'All phone categories :\n', '\n'.join(LABEL_NAMES) , '\n\n'
    print "Start processing . . .\n\n"
    global_start_time = time.time()

    # Import & Preprocess datasets
    print "Start reading an input file . . ."
    start_time = time.time()
    featuresets, labels = import_training_data(train_data_file_name, NUMBER_OF_CLASSES)
    print "> Imported & Preprocessed data! ({} secs)\n\n".format(time.time() - start_time)

    # Train and save models
    print "Start reading an input file . . ."
    for class_id in range(NUMBER_OF_CLASSES):
        print "> Training a model :: Category #{} {}".format(class_id+1,LABEL_NAMES[class_id]) 
        start_time = time.time()
        this_class_labels = [label[class_id] for label in labels]
        X_resampled, y_resampled = random_over_sampler.random_over_sample(featuresets, this_class_labels)
        classifier = train_model(zip(X_resampled, y_resampled))
        save_model(classifier, "sklearn_model_{:02d}.pickle".format(class_id+1))
        # save_model(classifier, "model_{:02d}.pickle".format(class_id+1))
        print "--- Trained a model! ({} secs) ---".format(time.time() - start_time)
    print "\n"

    # K-Fold Cross Validation (Accuracy test)
    start_time = time.time()
    k_fold_evaluation(featuresets, labels)
    print "--- Evaluation model! {} seconds ---\n\n".format(time.time() - start_time)

    print "========================"
    print "Training Model SUCCESS!"
    print "--- Total time: {} seconds ---".format(time.time() - global_start_time)
    print "========================"
