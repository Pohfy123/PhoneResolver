#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import re
from LexTo import LexTo

lexto = LexTo()
def removeStopWords(wordArr):
    th_stopWord = ["ไว้","ไม่","ไป","ได้","ให้","ใน","โดย","แห่ง","แล้ว","และ","แรก","แบบ","แต่","เอง","เห็น","เลย","เริ่ม","เรา",\
    "เมื่อ","เพื่อ","เพราะ","เป็นการ","เป็น","เปิดเผย","เปิด","เนื่องจาก","เดียวกัน","เดียว","เช่น","เฉพาะ","เคย","เข้า","เขา","อีก","อาจ",\
    "อะไร","ออก","อย่าง","อยู่","อยาก",	"หาก","หลาย","หลังจาก","หลัง","หรือ","หนึ่ง","ส่วน","ส่ง","สุด","สําหรับ","ว่า","วัน","ลง",\
    "ร่วม","ราย","รับ","ระหว่าง","รวม","ยัง","มี","มาก","มา","พร้อม","พบ","ผ่าน","ผล","บาง","น่า","นี้","นํา","นั้น","นัก","นอกจาก",\
    "ทุก","ที่สุด","ที่","ทําให้","ทํา","ทาง","ทั้งนี้","ทั้ง","ถ้า","ถูก","ถึง","ต้อง","ต่างๆ","ต่าง","ต่อ","ตาม","ตั้งแต่","ตั้ง","ด้าน","ด้วย",\
    "ดัง","ซึ่ง","ช่วง","จึง","จาก","จัด","จะ","คือ","ความ","ครั้ง","คง","ขึ้น","ของ","ขอ","ขณะ","ก่อน","ก็","การ","กับ","กัน","กว่า","กล่าว",\
    ":",",","&","amp","/",";",".","(",")","\"","-","@","\n"," ","\r","facebook"]
    return [word for word in wordArr if word not in th_stopWord]

def warpToArray(txt, delimeter="|"):
    words, types = lexto.tokenize(txt)
    return [word.encode('utf-8','ignore') for word in words]

def filterChar(content):
    content_no_special_char = re.subn(r'0-9!#$%?=:·\'+\[\]\^]', '', content)[0]
    return content_no_special_char

def parseAllDocuments(path_in, path_out, delimeter='|'):
    for dirpath, dirs, files in os.walk(path_in):
        for f in files:
            finname = os.path.join(dirpath, f)
            foutname = os.path.join(path_out, f)
            print "fname=", finname
            with open(finname) as pearl:
                o = open(foutname, 'w')

                # Read content from a document
                content = pearl.read().decode('utf-8', 'ignore')

                # Remove dont needed character
                content_no_special_char = filterChar(content)

                # Parse words
                words = warpToArray(content_no_special_char)
                # Remove stop words
                words = removeStopWords(words)
                    
                o.write(delimeter.join(words))

                o.close()