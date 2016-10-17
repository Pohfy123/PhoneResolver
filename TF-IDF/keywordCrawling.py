#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup

def fetchKeyword(urlArr):
    searchkey = ""
    for url in urlArr:
        try: 
            html = urlopen(url).read()
            soup = BeautifulSoup(html,"lxml")
            search_key = soup.findAll('meta',attrs={ 'name':'keywords'})
            search_desc = soup.findAll('meta',attrs={ 'name':'description'})
            if len(search_key) > 0:
                searchkey = searchkey+"\n"+str(search_key[0]['content'].encode('utf-8'))
            else:
                if len(search_desc) > 0:
                    searchkey = searchkey+"\n"+str(search_desc[0]['content'].encode('utf-8'))
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except:
            print "Something Error"
    return(searchkey)

# searchkey = fetchKeyword("https://www.instagram.com/plaavydessertcafe/")
# o = open("keyword.txt", 'w')
# o.write(searchkey)
# o.close()