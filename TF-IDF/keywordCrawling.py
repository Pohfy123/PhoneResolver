#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup
import socket
from HTMLParser import HTMLParser
import re


socket.setdefaulttimeout(30)

def isPhoneWeb(url):
    phoneList = ["phonespamfilter.co.nz","kodifikant.ru","forum.thailandfans.com","whois-il.com","anruferauskunft.de",\
                "anrufer.info","merinfo.se","determinecaller.com","vemsnummer.se","quemliga.com.br","anrufercheck.com",\
                "lovenumbersphone.it","shareyot.co.il","superforte.netsons.org","telefonforsaljare.nu","whotocall.ru",\
                "vorwahl-index.de","publicrecordssn.com","ssn-records.org","violetsmile.com","chichiama.com","sync.me",\
                "b.411note.com","mouser.com","serials.ws","docplayer.pl","serialsws.org","e-stat.go.jp","mottles-heer.de",\
                "whosnumber.com","phonenumber.cmcm.com"]
    for phone in phoneList:
        if phone in url:
            return True
    return False

### For content crawling
def CssJsStrip(html):
    pureHtmlCss = re.subn(r'<(script).*?</\1>(?s)', '', html)[0]
    pureHTML = re.subn(r'<(style).*?</\1>(?s)', '', pureHtmlCss)[0]
    return pureHTML

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
### End For content crawling

def fetchKeyword(urlTitleArr,include_content):
    searchkey = ""
    searchtext = ""
    for urlTitle in urlTitleArr:
        url,title = urlTitle.strip().split("|||",1)
        if isPhoneWeb(url):
            continue
        print "  + "+url
        try: 
            uopen = urlopen(url)
            # Avoid downloadable file (Only HTML)
            if 'text/html' not in uopen.headers.get('Content-Type'):
                print "Skip downloadable file"
                continue
            html = uopen.read()

            soup = BeautifulSoup(html,"lxml")
            search_key = soup.findAll('meta',attrs={ 'name':'keywords'})
            search_desc = soup.findAll('meta',attrs={ 'name':'description'})

            ## Include Content
            if include_content:
                search = soup.findAll('body')
                html = ""
                if len(search) > 0:
                    html = str(search[0].encode('utf-8'))
                pureHTML = CssJsStrip(html).decode('utf-8')
                searchtext = searchtext+strip_tags(pureHTML).encode('utf-8')
            ## End Include Content

            searchkey = searchkey+title+"\n"
            if len(search_key) > 0:
                searchkey = searchkey+"\n"+str(search_key[0]['content'].encode('utf-8'))
            elif len(search_desc) > 0:
                searchkey = searchkey+"\n"+str(search_desc[0]['content'].encode('utf-8'))
            else:
                print "No metadata"
            
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except:
            print "Something Error"
            
        searchtext = searchtext.replace('\n', ' ')
    return([searchkey,searchtext])

# searchkey = fetchKeyword("https://www.instagram.com/plaavydessertcafe/",True)
# o = open("keyword.txt", 'w')
# o.write(searchkey)
# o.close()