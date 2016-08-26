#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

pattern_1 = re.compile(r"ab(...)(.)(..)")
pattern_2 = re.compile(r"kk")
string_1 = u"abdjsjgjscskdjgiabfdksjgjcslkdjgioabcjaskdl;jtabc"
print re.match(pattern_1, string_1).group(1)
print re.search(pattern_1, string_1).group(1)
print re.search(pattern_1, string_1).group()
print "groupdict:"
print re.match(pattern_1, string_1).groupdict()
print "groups:"
print re.search(pattern_1, string_1).groups()

print re.findall(pattern_2,string_1)

print (re.findall(pattern_1,string_1))[2]

print re.match(pattern_2, string_1)


print "How to get one part of the regex match?????"
print "http://stackoverflow.com/questions/4666973/how-to-extract-a-substring-from-inside-a-string-in-python"

