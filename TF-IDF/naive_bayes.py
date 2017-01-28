#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
from sklearn import cross_validation
import pickle
import time
from sklearn.feature_extraction import DictVectorizer
import os


import itertools
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


result_labels = ['1_Air Travel Ticket Agencies','2_Home Stay','3_Hotel','4_Travel Bureaus','5_Airline Companies','6_Resorts & Bungalows','7_Seafood','8_Sukiyaki Shabu','9_Lounge Hotel Restaurant','10_Bakery Cake','11_Barbeque Grill','12_Coffee Shop','13_Ice Cream','14_Japanese'] ## Edit here

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


def k_fold_evaluation(datasets, nfolds=5):
    # K-fold cross validation
    cv = cross_validation.KFold(len(datasets), n_folds=nfolds, shuffle=True, random_state=None)

    print "Datasets |N|=%d" % len(datasets)
    
    scores = []
    idx = 1
    for traincv, evalcv in cv:
        # Train model
        train_data = datasets[traincv[0]:traincv[len(traincv)-1]]
        classifier = nltk.NaiveBayesClassifier.train(train_data)
        # classifier.show_most_informative_features()

        # Accuracy test
        test_data = datasets[evalcv[0]:evalcv[len(evalcv)-1]]
        score = nltk.classify.accuracy(classifier, test_data)
        print 'TEST#%d: accuracy: %lf' % (idx, score)
        
        # Display confusion matrix
        display_confusion_matrix(classifier, test_data, showGraphic=False)

        scores.append(score)
        idx += 1
    print 'TOTAL ACCURACY: %lf' % (sum(scores)/len(scores)) 


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
    save_model(DictVec, 'dictvect_'+('%02d'%file_id)+'.pickle')
    save_dict_words(DictVec.get_feature_names(), 'wordlist_'+('%02d'%file_id)+'.txt')

    return datasets, DictVec


def import_training_data(filename):
    datasets = []
    with open(filename,'r') as fin:        
        for line in fin:
            num,words,result = line.split(",",2)
            
            # Skip empty file
            if len(words)==0 or len(result)==0:
                continue
                
            phone_no = num.strip()
            
            words = dict([x.split(':') for x in words.strip().split(' ')])
            words = dict((k,float(v)) for k,v in words.iteritems())
            
            result = result.strip()
            
            data = {
                'phone_no' : phone_no, # no need
                'words' : words,
                'result' : result
            }
            datasets.append(data)
    return datasets


if __name__ == '__main__':
    # Gather the filename of all training data files
    filenames = []
    for file in os.listdir("./train-data/"):
        if file.endswith(".csv") and file.startswith('train-model'):
            filenames.append(file)
    filenames = [os.path.join('./train-data/', filename) for filename in filenames]

    print 'All phone categories :\n', '\n'.join(result_labels) , '\n\n'
    print 'All training data files :\n', '\n'.join(filenames) , '\n\n'
    print "Start processing . . ."

    global_start_time = time.time()

    for filename in filenames:    
        # Initialization for each model    
        file_id = int(filename[filename.index('train-model')+11: filename.index('.csv')])
        print "========= TRAIN MODEL :: Category #%s (%s) =========" % (file_id,result_labels[file_id-1]) 
        round_time = time.time()
        
        # Import datasets
        start_time = time.time()
        raw_datasets = import_training_data(filename)
        print "> Imported data! (%f secs)" % (time.time() - start_time)
            
        # Preprocess data
        start_time = time.time()
        datasets, DictVec = process_data(raw_datasets)
        print "> Preprocessed data! (%f secs)" % (time.time() - start_time)

        # Train and save models
        start_time = time.time()
        classifier = train_model(datasets)
        save_model(classifier, "model_"+('%02d'%file_id)+".pickle")
        print "> Trained model! (%f secs)" % (time.time() - start_time)

        # K-Fold Cross Validation (Accuracy test)
        start_time = time.time()
        k_fold_evaluation(datasets)
        print "> Evaluation model! (%f secs)" % (time.time() - start_time)
        print "--- %s seconds ---\n\n" % (time.time() - round_time)

    print "========================"
    print "Training Model SUCCESS!"
    print "--- Total time: %s seconds ---" % (time.time() - global_start_time)


    # Show result of each
    # with open('./train-data/train.csv','r') as fin:
    #     count = 0
    #     for line in fin:
    #         count += 1
    #         if count >= number_of_train: 
    #             num,words,is_travel,is_rest = line.split(",")
    #             test_word = words.split(" ")
    #             test_sent_features = {word: (word in test_word) for word in words_set}
    #             is_rest = is_rest.replace("\n","")
    #             dist = classifier.prob_classify(test_sent_features)
    #             print num, "\tpred =",dist.max(),"\tans =", is_travel+""+is_rest, (dist.max()==is_travel+""+is_rest)

                # diff = 0
                # for label in dist.samples():
                #     # print "\tlabel >>>",label," prob >>>" , dist.prob(label)
                #     diff = abs(dist.prob(label)-diff)
                # print "\tdiff",diff

