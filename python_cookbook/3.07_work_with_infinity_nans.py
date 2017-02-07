#!/usr/bin/python
#-*- coding:utf-8 -*-

# 3.07 Working with Infinity and Nans

import math
a = float('inf')
b = float('-inf')
c = float('nan')
print(a,b,c)

print('math.isinf(a)', math.isinf(a))
print('math.isinf(b)', math.isinf(b))
print('math.isnan(c)', math.isnan(c))

print('a+45', a + 45)
print('a/a', a / a)
print('a + b', a + b)

d = float('nan')
print('c == d', c == d)
print('c is d', c is d)

print('math.isnan(d)', math.isnan(d))
