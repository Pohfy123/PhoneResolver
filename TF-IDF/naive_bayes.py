#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
from sklearn import cross_validation
import pickle

result_labels = ['Air Travel Ticket Agencies','Home Stay','Hotel','Travel Bureaus','Bakery Cake']

def save_model(classifier, filename_out='my_classifier.pickle'):
    f = open(filename_out, 'wb')
    pickle.dump(classifier, f)
    f.close()
    print 'Model saved ! :: (' + filename_out + ')'


def load_model(filename_in='my_classifier.pickle'):
    f = open(filename_in, 'rb')
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
        
        train_data = featuresets
        classifier = nltk.NaiveBayesClassifier.train(train_data)

        model_name = "model_"+str(result_idx)+".pickle"
        save_model(classifier, model_name)


print "Start processing . . ."

all_words = ""
datasets = []

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

all_words = set(all_words.split(" "))

# accuracy_test(datasets, all_words, 2)

train_model(datasets, all_words)


# Show result of each
# with open('./train-data/train.csv','r') as fin:
#     count = 0
#     for line in fin:
#         count += 1
#         if count >= number_of_train: 
#             num,words,is_travel,is_rest = line.split(",")
#             test_word = words.split(" ")
#             test_sent_features = {word: (word in test_word) for word in all_words}
#             is_rest = is_rest.replace("\n","")
#             dist = classifier.prob_classify(test_sent_features)
#             print num, "\tpred =",dist.max(),"\tans =", is_travel+""+is_rest, (dist.max()==is_travel+""+is_rest)

            # diff = 0
            # for label in dist.samples():
            #     # print "\tlabel >>>",label," prob >>>" , dist.prob(label)
            #     diff = abs(dist.prob(label)-diff)
            # print "\tdiff",diff

