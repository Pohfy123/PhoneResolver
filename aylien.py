# -*- coding: utf-8 -*-

from aylienapiclient import textapi
import json
import sys
from pprint import pprint

client = textapi.Client(" 29bc232d", "53054f1de3f2d79315fb6436eaaf6e19")

def getCategoryTaxonomy(link):
    url = link
    classifications = client.ClassifyByTaxonomy({"url": url, "taxonomy": "iab-qag"})
    for category in classifications['categories']:
        print '%s\t%s' % (category['label'], category['score'])


def getCategorySpecific(link):
    url = link
    classes = ['food', 'bakery', 'ice-cream', 'travel', 'hotel']
    classifications = client.UnsupervisedClassify({'url': url, 'class': classes})
    for category in classifications['classes']:
        if(category['score'] is not None):
            print '%s , %s' % (category['label'], category['score'])


base_url = "https://translate.google.com/translate?hl=th&sl=th&tl=en&u="
getCategoryTaxonomy(base_url+sys.argv[1])