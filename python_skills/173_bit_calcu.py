#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 173_bit_calcu.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-01 22:59:09
#Last Modifieda: 2016-11-01 22:59:09
#*********************************************************

b = 0b11001010101010
b2 = bin(b & 0b1111111111)
print type(b2)

print b & 0b1111111111
print int(b2, 2)
