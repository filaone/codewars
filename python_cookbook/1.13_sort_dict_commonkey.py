#!/usr/bin/python
#-*- coding:utf-8 -*-

# 1.13 Sorting a List of Dictionaries by a Common Key

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003, 'cid':1000},
    {'fname': 'Wang', 'lname': 'Shu', 'uid': 1003, 'cid':1001},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002, 'cid':1000},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001,'cid':1000},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004,'cid':1000}
]

from operator import itemgetter

print(itemgetter('lname'))
print(sorted(rows, key=itemgetter('uid','cid')))
print(sorted(rows, key=lambda k:k['uid']))
