#!/usr/bin/python
#-*- coding:utf-8 -*-
from collections import Counter

string_1 = u'abc def ghi'
string_2 = u'abc def ghi'
string_3 = u'ghi def abc'

print string_1 == string_2
print string_2 == string_3
print Counter(string_1) == Counter(string_2)

set_2 = set(string_1.split(' '))
set_3 = set(string_3.split(' '))

print set_2 == set_3
