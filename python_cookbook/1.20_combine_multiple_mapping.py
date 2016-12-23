#!/usr/bin/python
#-*- coding:utf-8 -*-

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])
#If there are duplicate keys, the values form the first mapping get used
print(c['z'])

print(c)

c['z'] = 10
c['w'] = 20
del c['x']
print(a)


