#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sklearn.datasets
import util
import sklearn.svm
from termcolor import colored
import time

def test_classifier(X, y, clf, test_size=0.4, y_names=None, confusion=False):
    # train-test split
    print 'test size is: %2.0f%%' % (test_size * 100)
    X_train, X_test, y_train, y_test = sklearn.cross_validation.train_test_split(X, y, test_size=test_size,random_state=1000)

    clf.fit(X_train, y_train)
    y_predicted = clf.predict(X_test)

    if not confusion:
        print colored('Classification report:', 'magenta', attrs=['bold'])
        print sklearn.metrics.classification_report(y_test, y_predicted, target_names=y_names)
    else:
        print colored('Confusion Matrix:', 'magenta', attrs=['bold'])
        print sklearn.metrics.confusion_matrix(y_test, y_predicted)

global_start_time = time.time()
## Load train data
dir_path = "./traindata"
datasets = sklearn.datasets.load_files(dir_path,random_state=1000)

## Word Counts
word_counts = util.bagOfWords(datasets.data)

## TF
tf_transformer = sklearn.feature_extraction.text.TfidfTransformer(use_idf=False).fit(word_counts)
X = tf_transformer.transform(word_counts)

## TEST
clf = sklearn.svm.LinearSVC(random_state=1000)
test_classifier(X, datasets.target, clf, test_size=0.2, y_names=datasets.target_names, confusion=False)
print "--- Total time: %s seconds ---" % (time.time() - global_start_time)