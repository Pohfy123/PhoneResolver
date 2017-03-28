#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
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

NUMBER_OF_CLASSES = 4 # Edit here
LABEL_NAMES = ['01_Airline','02_Accommodation','03_Tourism','04_Restaurant & Delivery'] ## Edit here
train_data_file_name = './train-data/train_all_model.csv'

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



def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues,
                          showGraphic=True):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    
    if showGraphic:
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    if showGraphic:
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, cm[i, j],
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')

        
def display_confusion_matrix(classifier, test_data, showGraphic=False):
    # Compute confusion matrix
    y_pred = []
    y_test = []
    for tc in test_data:
        dist = classifier.prob_classify(tc[0])
        y_pred.append( dist.max() )
        y_test.append( tc[1] )

    cnf_matrix = confusion_matrix(y_test, y_pred)
    np.set_printoptions(precision=2)

    # Plot non-normalized confusion matrix
    if showGraphic:
        plt.figure()
    plot_confusion_matrix(cnf_matrix, classes="Class",
                        title='Confusion matrix, without normalization', showGraphic=showGraphic)

    # Plot normalized confusion matrix
    if showGraphic:
        plt.figure()
    plot_confusion_matrix(cnf_matrix, classes="Class", normalize=True,
                        title='Normalized confusion matrix', showGraphic=showGraphic)

    if showGraphic:
        plt.show()


def bin_list_to_dec(bin_list):
    return int(''.join(map(str, bin_list)),2)


def k_fold_evaluation(featuresets, labels, nfolds=5):
    datasets = zip(featuresets, labels)
    print colored("Datasets |N|=%d" % len(featuresets), 'blue', attrs=['bold'])
    print colored("Class distribution: {}".format(Counter([bin_list_to_dec(label) for label in labels])), 'blue', attrs=['bold'])

    # Stratified K-fold cross validation
    labels_dec = [bin_list_to_dec(y) for y in labels]
    skf = StratifiedKFold(labels_dec, n_folds=nfolds)

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

            X_train = [featuresets[idx] for idx in train_index]
            y_train = [this_class_labels[idx] for idx in train_index]
            train_data = zip(X_train, y_train)

            X_test = [featuresets[idx] for idx in test_index]
            y_test = [this_class_labels[idx] for idx in test_index]
            test_data = zip(X_test, y_test)

            print "Train data distribution: {}".format(Counter([bin_list_to_dec(labels[x]) for x in train_index]))
            print "Test data distribution: {}".format(Counter([bin_list_to_dec(labels[x]) for x in test_index]))

            # print "\n\n train"
            # print y_train
            # print "\n\n test"
            # print y_test

            # Train models
            classifier = train_model(train_data)
            y_pred = classifier.classify_many(X_test)

            # print "\n\n predict"
            # print y_pred
            
            # Evaluate
            y_pred_int = map(int, y_pred)
            y_test_int = map(int, y_test)
            
            print colored('Classification report:', 'magenta', attrs=['bold'])
            print sklearn.metrics.classification_report(y_test_int, y_pred_int)
            print colored('Confusion Matrix:', 'magenta', attrs=['bold'])
            print sklearn.metrics.confusion_matrix(y_test_int, y_pred_int)
            
            total_y_test.extend(y_test_int)
            total_y_pred.extend(y_pred_int)
            score = f1_score(y_test_int, y_pred_int, average=None)
            # print 'TEST#{}: F1-SCORE: {}'.format(fold_idx, score)
            scores.append(score)
            fold_idx += 1
        print colored('##############', 'red', attrs=['bold'])
        print colored('TOTAL Metrics of Model#{}: '.format(class_id+1), 'red', attrs=['bold'])
        this_report = sklearn.metrics.classification_report(total_y_test, total_y_pred)
        print colored(this_report, 'red')
        print colored('##############', 'red', attrs=['bold'])
        print "--- Evaluate a model! ({} secs) ---".format(time.time() - start_time)
        print '\n'*3
        all_avg_classification_reports += '\n\nModel#{}: \n'.format(class_id+1) + this_report
    print colored(all_avg_classification_reports, 'blue')


def train_model(train_data):    
    classifier = nltk.NaiveBayesClassifier.train(train_data)
    return classifier


def process_data(raw_datasets):
    # Convert word freq to Sparse matrix

    v = DictVectorizer(sparse=True)
    DictVec = v.fit([document['words'] for document in raw_datasets])
    for document in raw_datasets:
        document['words'] = DictVec.transform(document['words'])
    
    # Convert to ready-for-train format :: labeled_featuresets: A list of tuples ``(featureset, label)``.
    datasets = [ (DictVec.inverse_transform(data['words'])[0], data['result']) for data in raw_datasets ]
    
    # Save DictVectorizer model & word list
    save_model(DictVec, 'dictvect_'+('%02d'%class_id)+'.pickle')
    save_dict_words(DictVec.get_feature_names(), 'wordlist_'+('%02d'%class_id)+'.txt')

    return datasets, DictVec


def convert_to_sparse(featuresets):
    # Convert word freq to Sparse matrix
    v = DictVectorizer(sparse=True)
    dict_vec = v.fit(featuresets)

    # NOTICE: uncomment if sparse matrix is supported
    # featuresets = dict_vec.transform(featuresets)
    # featuresets = dict_vec.inverse_transform(x)

    # Save DictVectorizer model & word list
    save_model(dict_vec, 'dict_vect_models.pickle')
    save_dict_words(dict_vec.get_feature_names(), 'word_lists.txt')

    return featuresets


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
            words = dict((k,1.0) for k,v in words.iteritems())

            results = results.strip().split(",", n_class-1)

            featuresets.append(words)
            labels.append(results)
    
    return (convert_to_sparse(featuresets), labels)


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
    # print "Start reading an input file . . ."
    # for class_id in range(NUMBER_OF_CLASSES):
    #     print "> Training a model :: Category #{} {}".format(class_id+1,LABEL_NAMES[class_id]) 
    #     start_time = time.time()
    #     this_class_labels = [label[class_id] for label in labels]
    #     classifier = train_model(zip(featuresets, this_class_labels))
    #     save_model(classifier, "model_{:02d}.pickle".format(class_id+1))
    #     print "--- Trained a model! ({} secs) ---".format(time.time() - start_time)
    # print "\n"

    # K-Fold Cross Validation (Accuracy test)
    start_time = time.time()
    k_fold_evaluation(featuresets, labels)
    print "--- Evaluation model! {} seconds ---\n\n".format(time.time() - start_time)

    print "========================"
    print "Training Model SUCCESS!"
    print "--- Total time: {} seconds ---".format(time.time() - global_start_time)
    print "========================"