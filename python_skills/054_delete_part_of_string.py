#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

string_1 = u"goooooooooooooooggggggggglllllllleeeeee"

# delete the part which match the pattern of re
string_2 = re.sub(re.compile(r'o'), "", string_1)
print string_2


#squeeze the characters a great solve method
print "http://stackoverflow.com/users/455276/the-wolf?tab=profile"
print "http://stackoverflow.com/questions/7940619/squeezing-characters-with-python"
string_3 = re.sub(re.compile(r'([a-zA-Z])\1+'), r'\1', string_1)
print string_3


string_4 = "\t\t\t\t\t\t\t\thello wold \t\t\t\t\t\t\nsdfsdfsdf\nhel"
print string_4
string_5 = re.sub(re.compile(r'\s+'),"", string_4)
print string_5

# delete the last element in the string
print "rstrip : ",string_1[:-1]
print "rstrip : ",string_1.rstrip("e")

# delete the first element in the string
print "lstrip : ",string_1[1:]
print "lstrip : ",string_1.lstrip("g")

# strip
print string_4.strip("\t")
print "strip(\"uni or str or none\") remove from both end with uni or str or none "
print "lstrip remove the left and rstrip remove the right"

