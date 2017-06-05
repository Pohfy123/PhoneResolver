#!/usr/bin/env python
# -*- coding: utf-8 -*-
import httplib, urllib, base64
import json
import os

BING_API_KEY = 'FILL-BING-KEY-HERE'


def searchBing(search_term):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': BING_API_KEY,
    }

    params = urllib.urlencode({
        # Request parameters
        'q': search_term,
        'count': '50',
        'offset': '0',
        'mkt': 'en-us',
        'safesearch': 'Moderate',
    })

    try:
        conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v5.0/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        data = json.loads(data)
        # print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        search_result = data['webPages']['value']
        return search_result
    except Exception as e:
        # print "[Errno {0}] {1}".format(e.errno, e.strerror)
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        print message
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
            urlList = [link['url'] for link in result]
            titleList = [link['name'] for link in result]
            resultList = ['|||'.join(row) for row in zip(urlList,titleList)] 
            o.write('\n'.join(resultList).encode('utf-8'))

        # save to .csv database file
        fileDBname = os.path.join(output_path, db_file_name)
        with open(fileDBname, 'a') as oResult:
            for link in result:
                row = []
                row.append(search_term) # Phone Number
                row.append(link['name']) # title
                row.append(urllib.unquote(link['displayUrl'])) # url
                row.append(link['snippet']) # description
                row.append(link['id']) # id
                row.append(link['url']) # meta.uri
                row.append(link['dateLastCrawled']) # date

                oResult.write('|||'.join(row).encode('utf-8')) # print each row
                oResult.write('\n')


def readPhoneNoList(path_input_file,done_list):
    with open(path_input_file, "r") as fi:  
        nums = fi.read()
        if len(nums.strip()) == 0:
            numArr = []
        else:
            numArr = nums.strip().split("\n")
        # print 'done',done_list
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
    # print phoneNoList
    print('Use API Quota = ' + str(len(phoneNoList)) + ' Phone numbers')
    while True:
        inputConfirm = raw_input('Are you sure? [Y/N]: ')
        if(inputConfirm.upper()=='Y'):
            searchRelatedLinks(phoneNoList, path_url)
            break
        elif(inputConfirm.upper()=='N'):
            print 'Good Bye!'
            break

if __name__ == "__main__":
    runBingSearch('test_output_bing/police.txt','test_output_bing/00_url')