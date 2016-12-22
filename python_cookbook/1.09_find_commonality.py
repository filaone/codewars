#!/usr/bin/python
#-*- coding:utf-8 -*-

# 1.09 Finding Commonalities in Two Dictionaries

a = {
'x' : 1,
'y' : 2,
'z' : 3
}

b = {
'w' : 10,
'x' : 11,
'y' : 2
}

# Find key in common
print(a.keys() & b.keys())

# Find keys in a that are not in b
print(a.keys() - b.keys())

# Find (key,value) pairs in common
print(type(a.items()))
print(a.items() & b.items())

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - (a.keys() & b.keys())}
print(c)