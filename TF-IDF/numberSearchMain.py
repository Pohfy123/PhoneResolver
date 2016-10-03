#!/usr/bin/env python
# -*- coding: utf-8 -*-
import googleSearch
import textCrawling
import sys
import os
import time

# phoneNo = sys.argv[1]

def readPhoneNumber(input_path,output_path):
    fi = open(input_path,"r")
    nums = fi.read()
    numArr = nums.split("\n")

    for num in numArr:
        print ">>>> %s" % num
        url_array = googleSearch.getGoogleLinks(num)
        fn = os.path.join(os.path.dirname(__file__), output_path+num+".txt")
        fo = open(fn,"w")
        textCrawling.fetchText(url_array,fo)
        fo.close()
        time.sleep(30)

input_path = "number_input.txt"
output_path = "raw_data/"

readPhoneNumber(input_path,output_path)




