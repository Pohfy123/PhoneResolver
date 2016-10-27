import urllib
import mechanize
import sys
from bs4 import BeautifulSoup
import re
import os
import time
import random

def getGoogleLinks(link,fo):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent','chrome')]

    term = link.replace(" ","+")
    query = "http://www.google.com/search?num=20&q="+term
    htmltext = br.open(query).read()

    soup = BeautifulSoup(htmltext,"lxml")
    search = soup.findAll('div',attrs={ 'id':'search'})
    searchtext = ""
    if len(search) > 0:
        searchtext = str(search[0])  

    soupSearch = BeautifulSoup(searchtext,"lxml")
    searchR = soupSearch.findAll('h3',attrs={ 'class':'r'})
    url_array = []

    if not searchR:
        return url_array

    regexURL = "\?q=.*&amp;"
    patternURL = re.compile(regexURL)

    for x in searchR:
        tmpUrl = str(re.findall(patternURL,str(x))).replace("?q=","")
        tmpUrl = tmpUrl.replace("&amp;","")
        tmpUrl = tmpUrl.replace("[]","")
        tmpUrl = tmpUrl.replace("[\'","")
        tmpUrl = tmpUrl.replace("\']","")
        tmpUrl = re.subn(r'sa=.*', '', tmpUrl)[0]
        # print tmpUrl
        if tmpUrl:
            tmpUrl = urllib.unquote(tmpUrl)
            url_array.append(tmpUrl)
            fo.write(tmpUrl+"\n")
    return url_array


fi = open("number_input.txt","r")
nums = fi.read()
numArr = nums.split("\n")
for num in numArr:
    print ">>>> %s" % num
    fn = os.path.join(os.path.dirname(__file__), "./temp-processing-data/00_url/"+num+".txt")
    fo = open(fn,"w")
    getGoogleLinks(num,fo)
    fo.close()
    ranTime = random.randint(40, 60)
    time.sleep(ranTime)



 