#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
string_1 = """helloo
  hello    
helloooo
 world world worlds world"""
pattern_1 = re.compile(r'\Ahello+')
pattern_2 = re.compile('^hello+')
pattern_3 = re.compile(r'hello')
pattern_4 = re.compile(r'hello$')
pattern_5 = re.compile(r'hello\Z')
print pattern_1.findall(string_1)
print pattern_2.findall(string_1)
print pattern_3.findall(string_1)
print pattern_4.findall(string_1)
print pattern_5.findall(string_1)
print "it seems \\A and ^ is the same"
print "So as the \\Z and $"
print pattern_3.search(string_1).group()
print pattern_3.finditer(string_1)
for m in pattern_3.finditer(string_1):
    print m.group(),m.start(),m.end()
