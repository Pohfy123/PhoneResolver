#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import os
from nltk import ngrams

def wordSplit(sentence):
    # print(sentence)
    wordArr = sentence.split("|")
    newWordArr = []
    for x in wordArr:
        if x.strip():
            newWordArr.append(x.strip())
    return newWordArr

def removeStopWord(wordArr):
    th_stopWord = ["ไว้","ไม่","ไป","ได้","ให้","ใน","โดย","แห่ง","แล้ว","และ","แรก","แบบ","แต่","เอง","เห็น","เลย","เริ่ม","เรา",\
    "เมื่อ","เพื่อ","เพราะ","เป็นการ","เป็น","เปิดเผย","เปิด","เนื่องจาก","เดียวกัน","เดียว","เช่น","เฉพาะ","เคย","เข้า","เขา","อีก","อาจ",\
    "อะไร","ออก","อย่าง","อยู่","อยาก",	"หาก","หลาย","หลังจาก","หลัง","หรือ","หนึ่ง","ส่วน","ส่ง","สุด","สําหรับ","ว่า","วัน","ลง",\
    "ร่วม","ราย","รับ","ระหว่าง","รวม","ยัง","มี","มาก","มา","พร้อม","พบ","ผ่าน","ผล","บาง","น่า","นี้","นํา","นั้น","นัก","นอกจาก",\
    "ทุก","ที่สุด","ที่","ทําให้","ทํา","ทาง","ทั้งนี้","ทั้ง","ถ้า","ถูก","ถึง","ต้อง","ต่างๆ","ต่าง","ต่อ","ตาม","ตั้งแต่","ตั้ง","ด้าน","ด้วย",\
    "ดัง","ซึ่ง","ช่วง","จึง","จาก","จัด","จะ","คือ","ความ","ครั้ง","คง","ขึ้น","ของ","ขอ","ขณะ","ก่อน","ก็","การ","กับ","กัน","กว่า","กล่าว",\
    ":",",","&","amp","/",";",".","(",")","\"","-","@"]
    newWordArr = []
    for word in wordArr:
        if word not in th_stopWord :
            newWordArr.append(word)
    return newWordArr

def ngram(wordArr,n):
    my_ngrams = ngrams(wordArr, n)
    return my_ngrams

def parseAllDocuments(path_in, path_out):
    token_dict = {}
    for dirpath, dirs, files in os.walk(path_in):
        for f in files:
            finname = os.path.join(dirpath, f)
            foutname = os.path.join(path_out, f)
            print("fname=", finname)
            o = open(foutname, 'w', encoding="utf8")
            with open(finname,encoding="utf-8-sig") as pearl:
                sentence = pearl.read()
                wordArr = wordSplit(sentence)
                word_removed = removeStopWord(wordArr)
                word_ngram = ngram(word_removed,3)
                for w in word_ngram:
                    gram = "|".join(w)
                    o.write(gram+" ")
            o.close()


split_path = './split/'
split_out_path = './split_out/'
parseAllDocuments(split_path, split_out_path)

