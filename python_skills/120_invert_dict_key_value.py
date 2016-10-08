#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 120_invert_dict_key_value.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-06 18:37:21
#Last Modifieda: 2016-10-06 18:37:21
#*********************************************************

from collections import defaultdict

d = dict()
x = [chr(x) for x in range(97,111)]
y = range(97,111)

for a,b in zip(x,y):
    d[a] = b
d['p'] = [97,98,100]

dd = defaultdict(list)
for k,v in d.iteritems():
    if type(v) == list:
        for ele in v:
            dd[ele].append(k)
    else:
        dd[v].append(k)
#不仅仅是翻过来，而且要保证key唯一，所以必须要使用append
print dd
print "http://stackoverflow.com/questions/7304980/invert-keys-and-values-of-the-original-dictionary"
