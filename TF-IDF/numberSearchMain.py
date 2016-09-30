#!/usr/bin/env python
# -*- coding: utf-8 -*-
import googleSearch
import textCrawling
import sys
import os

phoneNo = sys.argv[1]
url_array = googleSearch.getGoogleLinks(phoneNo)

fn = os.path.join(os.path.dirname(__file__), "raw_data/"+phoneNo+".txt")
f = open(fn,"w")
textCrawling.fetchText(url_array,f)
f.close()
