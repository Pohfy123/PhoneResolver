# -*- coding: utf-8 -*-

import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

import PyICU
import nltk
import random

def isThai(chr):
    cVal = ord(chr)
    if (cVal >= 3584 and cVal <= 3711):
        return True
    return False


def warp(txt):
    bd = PyICU.BreakIterator.createWordInstance(PyICU.Locale("th"))
    bd.setText(txt)
    lastPos = bd.first()
    retTxt = ""
    try:
        while (1):
            currentPos = next(bd)
            retTxt += txt[lastPos:currentPos]
            # เฉพาะภาษาไทยเท่านั้น
            if (isThai(txt[currentPos - 1])):
                if (currentPos < len(txt)):
                    if (isThai(txt[currentPos])):
                        # คั่นคำที่แบ่ง
                        retTxt += "|"
            lastPos = currentPos
    except StopIteration:
        pass
        # retTxt = retTxt[:-1]
    return retTxt

N = 2
numberOfRows = 250
dict = {}
word_features_taste = [] #word_features_taste = ['รสชาติ','อร่อยมาก','มาก','สุด']
f = open('./data/data250_1000.csv', newline='', encoding='utf-8')
segmentedArr = []
reviewList = []
i = 0
for line in f:
    if (i is numberOfRows):break
    i = i+1
    id, review, n_taste, n_env, n_service = line.strip().split(',')
    if n_service == '1': #TODO : EDIT
        segmented = warp(review).split('|')
        for i in range(0, len(segmented)):
            wordGrammed = ''
            for j in range(0, N):
                if i + j in range(0, len(segmented)):
                    wordGrammed += segmented[i + j]
            reviewList.append(wordGrammed)
word_counter = {}
for word in reviewList:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1
popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
word_features_taste = popular_words[:20]
print(word_features_taste)

def document_features(document):
    document = document.replace(' ','|')
    segmented = warp(document).split('|')
    document_words = []

    for i in range(0,len(segmented)):
        wordOfDocument = ''
        for j in range(0,N):
            if i+j in range(0,len(segmented)):
                wordOfDocument += segmented[i+j]
        document_words.append(wordOfDocument)


    features = {}
    i = 0

    for i in range(0,len(word_features_taste)):
        word = ''
        for j in range(0,N):
            if i+j in range(0, len(word_features_taste)):
                word += word_features_taste[i+j]
        features['contains({})'.format(word)] = (word in document_words)
#    print(features)
    return features



f = open('./data/data250_1000.csv',encoding='utf8')
reviewArr = []
featuresets = []
i = 0
for line in f:
    if (i is numberOfRows):break
    i = i+1
    id,review,n_taste, n_env,n_service = line.strip().split(',')
    featuresets += [(document_features(review),n_service)] #TODO : EDIT
    reviewArr.append(review)


print(featuresets)

train_set, test_set = featuresets[:200], featuresets[200:]
classifier = nltk.NaiveBayesClassifier.train(train_set)
'''

for i in reviewArr:
    print(i)
    print(classifier.classify(document_features(i)))
    print('-------')
'''
print('Service model, N = 2')
print(nltk.classify.accuracy(classifier, test_set))
print(classifier.show_most_informative_features(5))