#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk

fin = open('./train-data/train.csv','r')
all_words = ""
number_of_train = 50
for line in fin:
    num,words,cat = line.split(",")
    all_words = all_words+" "+words
all_words = set(all_words.split(" "))
fin.close()

fin = open('./train-data/train.csv','r')
train = []
for line in fin:
    num,words,cat = line.split(",")
    cat = cat.replace("\n","")
    train.append((words,cat))
fin.close()

dataset = [({word: (word in x[0].split(" ")) for word in all_words}, x[1]) for x in train]

train_data = dataset[:number_of_train]
test_data = dataset[number_of_train:]
classifier = nltk.NaiveBayesClassifier.train(train_data)

print "accuracy is ",nltk.classify.accuracy(classifier, test_data)

fin = open('./train-data/train.csv','r')
count = 0
for line in fin:
    count += 1
    if count >= number_of_train: 
        num,words,cat = line.split(",")
        test_word = words.split(" ")
        test_sent_features = {word: (word in test_word) for word in all_words}
        cat = cat.replace("\n","")
        dist = classifier.prob_classify(test_sent_features)
        print num
        # diff = 0
        # for label in dist.samples():
        #     print "\tlabel >>>",label," prob >>>" , dist.prob(label)
        #     diff = abs(dist.prob(label)-diff)
        # print "\tdiff",diff
        print "\tpred =",dist.max(),"\tans =", cat, (dist.max()==cat)
fin.close()

