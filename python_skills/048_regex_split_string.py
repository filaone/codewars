#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

string_2 = u"彩吧论坛- 首页_彩票论\n    \n坛|福彩论坛|体彩  \n  论坛|3D彩票论坛"

print "use regex to split"
pattern_1 = re.compile(r'\n[ \t\s\r]+\n')
lis = pattern_1.split(string_2)
for m in lis:
    print "-------------hello--------------"
    print m.encode('utf-8')


l = re.compile(r'\n[ \t\s\r]+\n').split(string_2)
print l
