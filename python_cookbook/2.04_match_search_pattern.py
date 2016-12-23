#!/usr/bin/python
#-*- coding:utf-8 -*-

# Matching and Searching for Text Patterns

text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
print(text == 'yeah')

# Match at start or end
print(text.startswith('yeah'))

# Search for the location of the first occurrence
print(text.find('no'))

import re
text1 = '11/22/3344, 55/66/7788, 99/00/1122'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
if datepat.match(text1):
    print('yes')


fa = re.findall(datepat,text1)
print(fa)

ma = re.match(datepat, text1)
print(ma.groups())

for month,day,year in re.findall(datepat, text1):
    print('{}-{}-{}'.format(year,month,day))
