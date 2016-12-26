#!/usr/bin/python
#-*- coding:utf-8 -*-

#2.09 Normalizing Unicode Text to a Standard Representation

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

#print(s1)
#print(s2)

import unicodedata

# NFC是全组成，如果有可能就一定要用单个代码点
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1))
print(ascii(t2))

# NFD表示应该使用组合字符，每个字符是能完全分解开的
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print(ascii(t3))
print(ascii(t4))

s = '\ufb01'
print(ascii(s))
print(ascii(unicodedata.normalize('NFD',s)))
print(ascii(unicodedata.normalize('NFKC',s)))
print(ascii(unicodedata.normalize('NFKD',s)))
