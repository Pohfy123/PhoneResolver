#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import textCrawling
import keywordCrawling
import sys
import os

def search(path_in,path_out):
    for dirpath, dirs, files in os.walk(path_in):
        for f in files:
            finname = os.path.join(dirpath, f)
            foutname = os.path.join(path_out, f)
            print "fname=", finname
            with open(finname) as pearl:
                o = open(foutname, 'w')
                # Read url from a document
                urls = pearl.read().decode('utf-8', 'ignore')
                url_array = urls.split()
                text = keywordCrawling.fetchKeyword(url_array)                
                o.write(text)
                o.close()


