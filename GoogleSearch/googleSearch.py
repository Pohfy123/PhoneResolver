import urllib
import mechanize
import sys
from bs4 import BeautifulSoup
import re

def getGoogleLinks(link):
    # print link
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent','chrome')]

    term = link.replace(" ","+")
    query = "http://www.google.com/search?num=100&q="+term
    htmltext = br.open(query).read()
    # print htmltext

    soup = BeautifulSoup(htmltext)
    search = soup.findAll('div',attrs={ 'id':'search'})
    searchtext = str(search[0])  

    # print searchtext

    soupSearch = BeautifulSoup(searchtext)
    searchR = soupSearch.findAll('h3',attrs={ 'class':'r'})

    regexURL = "\?q=.*&amp;"
    patternURL = re.compile(regexURL)
    # regexHeader = "<a[^>]*>(.*?)<\/a>"
    # patternHeader = re.compile(regexHeader)
    
    url_array = []
    # header_array = []
   
    for x in searchR:
        tmpUrl = str(re.findall(patternURL,str(x))).replace("?q=","")
        tmpUrl = tmpUrl.replace("&amp;","")
        tmpUrl = tmpUrl.replace("[]","")
        tmpUrl = tmpUrl.replace("[\'","")
        tmpUrl = tmpUrl.replace("\']","")  
        # tmpHeader = str(re.findall(patternHeader,str(x)))
        # tmpHeader = tmpHeader.replace("[]","")
        # tmpHeader = tmpHeader.replace("[\'","")
        # tmpHeader = tmpHeader.replace("\']","")
        if tmpUrl:
            url_array.append(tmpUrl)
            # header_array.append(tmpHeader)
            # print tmpUrl
            # print tmpHeader
    # print url_array
    # print header_array
    return url_array

def getGoogleTitle(link):
    # print link
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent','chrome')]

    term = link.replace(" ","+")
    query = "http://www.google.com/search?num=100&q="+term
    htmltext = br.open(query).read()
    # print htmltext

    soup = BeautifulSoup(htmltext)
    search = soup.findAll('div',attrs={ 'id':'search'})
    searchtext = str(search[0])  

    # print searchtext

    soupSearch = BeautifulSoup(searchtext)
    searchR = soupSearch.findAll('h3',attrs={ 'class':'r'})

    regexURL = "\?q=.*&amp;"
    patternURL = re.compile(regexURL)
    regexHeader = "<a[^>]*>(.*?)<\/a>"
    patternHeader = re.compile(regexHeader)
    
    url_array = []
    header_array = []
   
    for x in searchR:
        tmpUrl = str(re.findall(patternURL,str(x))).replace("?q=","")
        tmpUrl = tmpUrl.replace("&amp;","")
        tmpUrl = tmpUrl.replace("[]","")
        tmpUrl = tmpUrl.replace("[\'","")
        tmpUrl = tmpUrl.replace("\']","")  
        tmpHeader = str(re.findall(patternHeader,str(x)))
        tmpHeader = tmpHeader.replace("[]","")
        tmpHeader = tmpHeader.replace("[\'","")
        tmpHeader = tmpHeader.replace("\']","")
        if tmpUrl:
            # url_array.append(tmpHeader)
            header_array.append(tmpHeader)
            # print tmpUrl
            # print tmpHeader
    # print url_array
    # print header_array
    return header_array



 