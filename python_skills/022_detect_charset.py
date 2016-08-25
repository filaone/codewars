#!/usr/bin/python
#-*- coding:utf-8 -*-
import chardet


def whatisthis(s):
    if isinstance(s,str):
        print "Ordinary string"
    elif isinstance(s,unicode):
        print "Unicode string"
    else:
        print "not a string"

s = 'hello world'
whatisthis(s)
uni = s.decode('utf-8')
whatisthis(uni)
print type(uni).__name__
lat = uni.encode('latin_1')
whatisthis(lat)
print type(lat).__name__

print "isinstance can determin is or not unicode"
print "also type().__name__"

if type(s).__name__!='unicode':
    print chardet.detect(s)
else:
    print "unicode!"
