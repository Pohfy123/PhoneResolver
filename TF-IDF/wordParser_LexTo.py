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
    "facebook","กรุงเทพมหานคร","ถูกใจ","กำลัง","พูดถึง","คน","กำลัง","ที่นี่","ตา","แก","ส","อิน","รม","ดารา",\
    "ดีไซน์","ตกแต่ง","นะ","ครับ"]
    return [word for word in wordArr if word.strip() not in th_stopWord]

def isThai(chr):
    cVal = ord(chr)
    if(cVal >= 3584 and cVal <= 3711):
        return True
    return False

def isEnglish(chr):
    cVal = ord(chr)
    if (cVal >= 97 and cVal <= 122 ) or (cVal >= 65 and cVal <= 90):
        return True
    return False

def warpToArray_LexTo(txt, delimeter="|"):
    words, types = lexto.tokenize(txt)
    return [word.encode('utf-8','ignore') for word in words]

def warpToArray_PyICU(txt, delimeter="|"):
    bd = PyICU.BreakIterator.createWordInstance(PyICU.Locale("th"))
    bd.setText(txt)
    lastPos = bd.first()
    retList = []
    try:
        while(1):
            currentPos = next(bd)
            retList.append(txt[lastPos:currentPos].encode('utf-8'))
            lastPos = currentPos
    except StopIteration:
        pass
    return retList

def filterChar(content):
    # Only Thai & English
    content_no_special_char = ''.join([c for c in content if isThai(c)]) #or isEnglish(c)
    return content_no_special_char

def parseAllDocuments(path_in, path_out, delimeter='|', isPyICU = False):
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
                if isPyICU is True:
                    words = warpToArray_PyICU(content_no_special_char)
                else:
                    words = warpToArray_LexTo(content_no_special_char)
                # Remove stop words
                words = removeStopWords(words)
                    
                o.write(delimeter.join(words))

                o.close()