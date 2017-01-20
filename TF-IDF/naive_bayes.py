#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
from sklearn import cross_validation
import pickle
import time
from sklearn.feature_extraction import DictVectorizer

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


def accuracy_test(datasets, nfolds=2):
    # Construct each model (each category)
    for result_idx in range( len(datasets[0]['result']) ):
        print "========= TEST FEATURE #%d (%s) =========" % (result_idx+1,result_labels[result_idx]) 
        featuresets = [ (DictVec.inverse_transform(data['words'])[0], data['result'][result_idx]) for data in datasets ]
                
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
        print 'TOTAL ACCURACY: %lf' % (sum(scores)/len(scores)) 


def train_model(datasets):
    # Construct each model (each category)
    print 'all categories ::', result_labels
    for result_idx in range( len(datasets[0]['result']) ):
        start_time = time.time()
        print "========= TRAIN FEATURE #%d (%s) =========" % (result_idx+1,result_labels[result_idx]) 
        
        # Convert to labeled_featuresets: A list of tuples ``(featureset, label)``.
        train_data = [ (DictVec.inverse_transform(data['words'])[0], data['result'][result_idx]) for data in datasets ]
        
        # Train model
        classifier = nltk.NaiveBayesClassifier.train(train_data)

        model_name = "model_"+str(result_idx+1)+".pickle"
        save_model(classifier, model_name)
        
        print "--- %s seconds ---" % (time.time() - start_time)


print "Start processing . . ."

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
            'words' : dict.fromkeys(words.split(" "), 1),
            'result' : results  
        })

# Convert word freq to Sparse matrix
v = DictVectorizer(sparse=True)
DictVec = v.fit([document['words'] for document in datasets])
for document in datasets:
    document['words'] = DictVec.transform(document['words'])
save_model(DictVec, 'dictvect_xxx.pickle')
save_dict_words(DictVec.get_feature_names())

# Train and save models
train_model(datasets)

# K-Fold Cross Validation (Accuracy test)
# accuracy_test(datasets, 5)


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

