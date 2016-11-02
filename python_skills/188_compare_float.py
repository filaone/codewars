#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 188_compare_float.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-02 12:09:16
#Last Modifieda: 2016-11-02 12:09:16
#*********************************************************

print "http://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python"

f1 = 1.23456789123456
f2 = 1.23456788123456

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
    #return abs(f1 - f2) <= allowed_error

def isbiger(a,b):
    if isclose(a,b):
        return False
    elif a - b > 0:
        return True
    return False;

def issmaller(a,b):
    if isclose(a,b):
        return False
    elif a - b < 0:
        return True
    return False;

print abs(f1)*1e-09
print abs(f2)*1e-09
print abs(f1 - f2)

print isclose(f1,f1)
print isclose(f1,1.23456789123456)

print f1 - f2
print f2 - f1

print isbiger(f1,f2)
