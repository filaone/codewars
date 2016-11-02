#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 192_rational.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-02 16:44:59
#Last Modifieda: 2016-11-02 16:44:59
#*********************************************************

from fractions import Fraction
from decimal import Decimal
print "https://docs.python.org/2/library/fractions.html"
print type(Fraction(16, -10))
print Fraction(16, -10)
print Fraction(123)
print Fraction(3.1415926)
print Decimal('1.1')
print Fraction(3.3*2.0)
print Fraction(2.0*3.3)
print 2.222222 * 3.3333333333 == 3.3333333333 * 2.222222
print str(Fraction(2.2222)).split('/')
