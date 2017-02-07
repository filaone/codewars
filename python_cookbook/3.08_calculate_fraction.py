#!/usr/bin/python
#-*- coding:utf-8 -*-

# 3.08 Calculating with Fractions

from fractions import Fraction
a = Fraction(5,4)
b = Fraction(7,23)
print('a + b', a + b)
print('a * b', a * b)
print('Get numerator', (a*b).numerator)
print('Get numerator', (a*b).denominator)
print('Float a * b', format(float(a*b), '^10.3f'))
print('c.limit_denominator(8)', (a*b).limit_denominator(8))
x = 3.75
print('Converting a float to a fraction', Fraction(*x.as_integer_ratio()))

