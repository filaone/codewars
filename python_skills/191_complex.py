#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 191_complex.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-02 16:37:12
#Last Modifieda: 2016-11-02 16:37:12
#*********************************************************

import cmath

print "http://stackoverflow.com/questions/8370637/complex-numbers-usage-in-python"
complex_a = complex()
complex_a = complex(2,3)
print complex_a
complex_b = 2 + 3j
print complex_b
print complex_b * complex_b
print complex_b.real
print complex_b.imag
print complex_b.conjugate()

print cmath.sin(complex_b)
