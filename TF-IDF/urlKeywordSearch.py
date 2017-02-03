#!/usr/bin/env python
# -*- coding: utf-8 -*-
import keywordCrawling

import sys
import os
import threading, urllib, urlparse
import pandas as pd

limitSemaphore = threading.Semaphore(1) # Limit 20 files
class CrawlerThread(threading.Thread):
    def __init__(self, limitSemaphore, path_out,path_raw_data_keyword,path_raw_data_content,include_content,finname,f     ,fp):
        self.limitSemaphore = limitSemaphore
        self.threadId = hash(self)
        self.path_out = path_out
        self.path_raw_data_keyword = path_raw_data_keyword
        self.path_raw_data_content = path_raw_data_content
        self.include_content = include_content
        self.finname = finname
        self.f = f

        self.fp = fp

        threading.Thread.__init__(self)

    def run(self):
        self.limitSemaphore.acquire() # wait
        print ">>>>>>>>>>>>>>>> Start :: ",self.finname
        ## Processing each filles
        crawl(self.path_out,self.path_raw_data_keyword,self.path_raw_data_content,self.include_content,self.finname,self.f      ,self.fp)
        self.limitSemaphore.release()
        print "<<<<<<<<<<<<<<<< Finish :: ",self.finname

def crawl(path_out,path_raw_data_keyword,path_raw_data_content,include_content,finname,f     ,fp):
    foutname = os.path.join(path_out, f)
    foutname_keyword = os.path.join(path_raw_data_keyword, f)
    foutname_content = ""
    if include_content:
        foutname_content = os.path.join(path_raw_data_content, f)

    # print ""
    # print "fname=", finname
    with open(finname) as pearl:
        o = open(foutname, 'w')
        o_keyword = open(foutname_keyword, 'w')
        o_content = ""
        if include_content:
            o_content = open(foutname_content, 'w')
        # Read url from a document
        urls = pearl.read().strip()
        url_title_array = urls.split("\n")

        # Remove empty line
        url_title_array = map(str.strip, url_title_array)
        url_title_array = filter(None, url_title_array)

        textArr = keywordCrawling.fetchKeyword(url_title_array,include_content       ,fp)
        keyword = textArr[0]
        content = textArr[1]

        o_keyword.write(keyword)
        o_keyword.close()
        
        if include_content:
            o_content.write(content)
            o_content.close()
        
        o.write(keyword+'\n'+content)

def search(path_in='./temp-processing-data/00_url/',path_out='./temp-processing-data/01_raw-data/',path_raw_data_keyword='./temp-processing-data/01_raw-data-keyword/',path_raw_data_content='./temp-processing-data/01_raw-data-content/',include_content=True):
    done_list = []
    for dirpath, dirs, files in os.walk(path_out):
        for f in files:
            fin_ext = os.path.splitext(os.path.basename(f))[1]
            if fin_ext == '.txt':
                done_list.append(f)
    
    threadPool = []

    ## write txt for debug                    
    fp = open('web_crawling_log-'+str(path_in.split('/')[2])+'.txt','a')
    
    for dirpath, dirs, files in os.walk(path_in):
        for f in files:
            # Skip done list
            if(f in done_list):
                continue

            finname = os.path.join(dirpath, f)
            fin_ext = os.path.splitext(os.path.basename(finname))[1]
            if fin_ext != '.txt':
                continue

            # Create crawler
            t = CrawlerThread(limitSemaphore, path_out,path_raw_data_keyword,path_raw_data_content,include_content,finname,f      ,fp)
            threadPool.append(t)
            
    
    # Start all crawler threads Finish
    for t in threadPool:
        t.start()

    # Wait all crawler threads finish
    for t in threadPool:
        t.join()
    fp.close()
    


