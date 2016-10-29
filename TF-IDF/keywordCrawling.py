#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup
import socket

socket.setdefaulttimeout(30)

def isPhoneWeb(url):
    phoneList = ["phonespamfilter.co.nz","kodifikant.ru","forum.thailandfans.com","whois-il.com","anruferauskunft.de",\
                "anrufer.info","merinfo.se","determinecaller.com","vemsnummer.se","quemliga.com.br","anrufercheck.com",\
                "lovenumbersphone.it","shareyot.co.il","superforte.netsons.org","telefonforsaljare.nu","whotocall.ru",\
                "vorwahl-index.de","publicrecordssn.com","ssn-records.org","violetsmile.com","chichiama.com","sync.me",\
                "b.411note.com","mouser.com","serials.ws","docplayer.pl","serialsws.org","e-stat.go.jp","mottles-heer.de",\
                "whosnumber.com"]
    for phone in phoneList:
        if phone in url:
            return True
    return False

def fetchKeyword(urlTitleArr):
    searchkey = ""
    for urlTitle in urlTitleArr:
        url,title = urlTitle.strip().split("|||",1)
        if isPhoneWeb(url):
            continue
        print "  + "+url
        try: 
            html = urlopen(url).read()
            soup = BeautifulSoup(html,"lxml")
            search_key = soup.findAll('meta',attrs={ 'name':'keywords'})
            search_desc = soup.findAll('meta',attrs={ 'name':'description'})
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
    return(searchkey)

# searchkey = fetchKeyword("https://www.instagram.com/plaavydessertcafe/")
# o = open("keyword.txt", 'w')
# o.write(searchkey)
# o.close()