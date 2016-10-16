#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
import sys
import re

def CssJsStrip(html):
    pureHtmlCss = re.subn(r'<(script).*?</\1>(?s)', '', html)[0]
    pureHTML = re.subn(r'<(style).*?</\1>(?s)', '', pureHtmlCss)[0]
    return pureHTML

def fetchHTML(url):
    searchtext = ""
    try: 
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html,"lxml")
        search = soup.findAll('body')
        if len(search) > 0:
            searchtext = str(search[0].encode('utf-8')) 
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except:
        print "Something Error"
    return(searchtext)

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def fetchText(urlArr):
    text = ""
    for url in urlArr:
        html = fetchHTML(url)
        pureHTML = CssJsStrip(html).decode('utf-8')
        text = text+"\n=================\n"+strip_tags(pureHTML).encode('utf-8')
    return text


# url = sys.argv[1]
# f = open("text.txt","w")
# html = fetchHTML(url)
# pureHTML = CssJsStrip(html).decode('utf-8')
# text = strip_tags(pureHTML).encode('utf-8')
# f.write(text)




