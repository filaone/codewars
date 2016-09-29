#!/usr/bin/python
#-*- coding:utf-8 -*-

import xmltodict

with open('./addon/example.xml') as fd:
    doc = xmltodict.parse(fd.read())

print doc['mydocument']['@has']
print doc['mydocument']['and']['many']
print doc['mydocument']['plus']['@a']
print doc['mydocument']['plus']['#text']
