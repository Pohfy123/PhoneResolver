#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup

def fetchKeyword(url):
    searchkey = ""
    try: 
        html = urlopen(url).read()
        soup = BeautifulSoup(html,"lxml")
        search = soup.findAll('meta',attrs={ 'name':'keywords'})
        if len(search) > 0:
            searchkey = str(search[0]['content'].encode('utf-8')) 
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except:
        print "Something Error"
    return(searchkey)

searchkey = fetchKeyword("https://www.instagram.com/plaavydessertcafe/")
o = open("keyword.txt", 'w')
o.write(searchkey)
o.close()