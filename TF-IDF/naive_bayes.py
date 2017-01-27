#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
from sklearn import cross_validation
import pickle
import time
from sklearn.feature_extraction import DictVectorizer
import os

result_labels = ['01_Airline','02_Accommodation','04_Restaurant & Delivery','05_Sweet','06_Beverage'] ## Edit here

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


def accuracy_test(datasets, nfolds=5):
    # K-fold cross validation
    cv = cross_validation.KFold(len(datasets), n_folds=nfolds, shuffle=True, random_state=None)

    scores = []
    idx = 1
    for traincv, evalcv in cv:
        # Train model
        train_data = datasets[traincv[0]:traincv[len(traincv)-1]]
        classifier = nltk.NaiveBayesClassifier.train(train_data)

        # Evaluate model
        test_data = datasets[evalcv[0]:evalcv[len(evalcv)-1]]
        score = nltk.classify.accuracy(classifier, test_data)

        # classifier.show_most_informative_features()
        print 'TEST#%d: accuracy: %lf' % (idx, score)
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
    save_model(DictVec, 'dictvect_'+file_id+'.pickle')
    save_dict_words(DictVec.get_feature_names(), 'wordlist_'+file_id+'.txt')

    return datasets, DictVec


def import_training_data(filename):
    datasets = []
    with open(filename,'r') as fin:        
        for line in fin:
            num,words,result = line.split(",",2)
            
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
    file_id = filename[filename.index('train-model')+11: filename.index('.csv')]
    print "========= TRAIN MODEL :: Category #%s (%s) =========" % (file_id,result_labels[int(file_id)-1]) 
    start_time = time.time()
    
    # Import datasets
    raw_datasets = import_training_data(filename)
        
    # Preprocess data
    datasets, DictVec = process_data(raw_datasets)

    # Train and save models
    classifier = train_model(datasets)
    save_model(classifier, "model_"+file_id+".pickle")

    # K-Fold Cross Validation (Accuracy test)
    # accuracy_test(datasets)
    print "--- %s seconds ---" % (time.time() - start_time)

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

