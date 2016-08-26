#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

def f_lower(s):
    pattern_lower = re.compile(r"[a-z]")
    if pattern_lower.match(s):
        return True
    return False    

def f_upper(s):
    pattern_upper = re.compile(r"[A-Z]")
    if pattern_upper.match(s):
        return True
    return False    

def f_string_lower(s):
    pattern_lower = re.compile(r"\A[a-z]*\z")
    if re.match(pattern_lower,s):
        return True
    return False
    
print f_lower("s")
print f_lower("S")
print f_upper("s")
print f_upper("S")


pattern_lower = re.compile(r"[a-z]")
print re.findall(pattern_lower, "eeeeee")

print "s".isupper()
print "e".islower()
print "E".islower()

letters = "asdfssdEJKHIHIEHF"
uppers = [l for l in letters if l.isupper()]
print uppers
print "".join(uppers)

print f_string_lower(letters)
