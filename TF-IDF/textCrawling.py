#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
from HTMLParser import HTMLParser
import sys

def fetchHTML(url):
    html = urllib.urlopen("https://www.wongnai.com/restaurants/158354cD-plaavy-dessert-cafe").read()
    return(html)

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

html = fetchHTML(sys.argv[1])
text = strip_tags(html)
f = open("out.txt","w")
f.write(text)
