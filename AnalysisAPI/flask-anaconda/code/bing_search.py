#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from py_bing_search import PyBingWebSearch
import urllib

# Init value
bing_api_key = "u5aItWFoT3raVTFVYQ/E8gPIOuATj3JWqnxz6Wnm628" # Enter your Bing API Key
custom_params = "&Market='th-TH'"
CAT_NAME = 'Airline Companies'

def searchBing(search_term):
    try:
        bing_web = PyBingWebSearch(bing_api_key, search_term, web_only=True, custom_params=custom_params)
        search_result = bing_web.search(limit=50, format='json')
        return search_result
    except:
        print "============== cannot search :: API expired ==============="
        fout = open('not_search_input.txt','a')
        fout.write(search_term+'\n')
        return ""

def searchRelatedLinks(search_term_list, output_path, db_file_name="bing-search-result.csv"):    
    for search_term in search_term_list:
        print(search_term)
        fout_path = os.path.join(output_path, search_term+'.txt')

        result = searchBing(search_term)

        # save to each phone no file
        with open(fout_path, 'w') as o:
            urlList = [link.url for link in result]
            titleList = [link.title for link in result]
            resultList = ['|||'.join(row) for row in zip(urlList,titleList)] 
            o.write('\n'.join(resultList).encode('utf-8'))

        # # save to .csv database file
        # fileDBname = os.path.join(output_path, db_file_name)
        # with open(fileDBname, 'a') as oResult:
        #     for link in result:
        #         row = []
        #         row.append(search_term) # Phone Number
        #         row.append(link.title) # title
        #         row.append(urllib.unquote(link.url)) # url
        #         row.append(link.description) # description
        #         row.append(link.id) # id
        #         row.append(link.meta.uri) # meta.uri
        #         row.append(link.meta.type) # meta.type

        #         oResult.write(','.join(row).encode('utf-8')) # print each row
        #         oResult.write('\n')


def readPhoneNoList(path_input_file,done_list):
    with open(path_input_file, "r") as fi:
        nums = fi.read()
        numArr = nums.split("\n")
        new_num_arr = [num for num in numArr if num+'.txt' not in done_list]
    return new_num_arr

def runBingSearch(path_number_list='./number_input.txt',path_url='./temp-processing-data/00_url/'):
    done_list = []
    for dirpath, dirs, files in os.walk(path_url):
        for f in files:
            fin_ext = os.path.splitext(os.path.basename(f))[1]
            if fin_ext == '.txt':
                done_list.append(f)
    phoneNoList = readPhoneNoList(path_number_list,done_list)
    print('Use API Quota = ' + str(len(phoneNoList)) + ' Phone numbers')
    # while True:
        # inputConfirm = raw_input('Are you sure? [Y/N]: ')
        # if(inputConfirm.upper()=='Y'):
    searchRelatedLinks(phoneNoList, path_url)
        # break
        # elif(inputConfirm.upper()=='N'):
        # print 'Good Bye!'
        # break

if __name__ == "__main__":
    runBingSearch('./temp-processing-data_'+CAT_NAME+'/difference_files.txt','./temp-processing-data_'+CAT_NAME+'/00_url_'+CAT_NAME+'_diff/')