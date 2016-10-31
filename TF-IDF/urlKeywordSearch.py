#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import textCrawling
import keywordCrawling
import sys
import os

def search(path_in,path_out):
    done_list = []
    for dirpath, dirs, files in os.walk(path_out):
        for f in files:
            fin_ext = os.path.splitext(os.path.basename(f))[1]
            if fin_ext == '.txt':
                done_list.append(f)
    
    for dirpath, dirs, files in os.walk(path_in):
        for f in files:
            # Skip done list
            if(f in done_list):
                continue
            
            finname = os.path.join(dirpath, f)
            fin_ext = os.path.splitext(os.path.basename(finname))[1]
            if fin_ext != '.txt':
                continue
            foutname = os.path.join(path_out, f)
            print ""
            print "fname=", finname
            with open(finname) as pearl:
                o = open(foutname, 'w')
                # Read url from a document
                urls = pearl.read().strip()
                url_title_array = urls.split("\n")

                # Remove empty line
                url_title_array = map(str.strip, url_title_array)
                url_title_array = filter(None, url_title_array)

                text = keywordCrawling.fetchKeyword(url_title_array)                
                o.write(text)
                o.close()


