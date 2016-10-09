#!/usr/bin/python
#-*-coding: utf-8 -*-

from LexTo import LexTo


lexto = LexTo()
text = u"ร้านอาหารจีน"
words, types = lexto.tokenize(text)

f = open("text.txt","w")
f.write('|'.join(words).encode('utf-8'))
f.close()
