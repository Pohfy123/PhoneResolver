#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk

fin = open('./train-data/train.csv','r')
all_words = ""
for line in fin:
    num,words,cat = line.split(",")
    all_words = all_words+" "+words
fout = open('./train-data/output.txt','w')
all_words = set(all_words.split(" "))

fin = open('./train-data/train.csv','r')
train = []
for line in fin:
    num,words,cat = line.split(",")
    cat = cat.replace("\n","")
    train.append((words,cat))
fin.close()

t = [({word: (word in x[0].split(" ")) for word in all_words}, x[1]) for x in train]
classifier = nltk.NaiveBayesClassifier.train(t)

fin = open('./train-data/test.csv','r')
for line in fin:
    num,words = line.split(",")
    test_word = words.split(" ")
    test_sent_features = {word: (word in test_word) for word in all_words}
    print num," >>> ",classifier.classify(test_sent_features)
