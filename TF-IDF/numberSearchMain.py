# -*- coding: utf-8 -*-
import googleSearch
# import aylien
import sys

phoneNo = sys.argv[1]

url_array = googleSearch.getGoogleLinks(phoneNo)
# title_array = googleSearch.getGoogleTitle(phoneNo)

print(url_array)

# for url in url_array:
#     aylien.getCategorySpecific(url)