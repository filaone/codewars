#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 3.01_round_numerical_value.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2017-01-18 11:31:18
#Last Modifieda: 2017-01-18 11:31:18
#*********************************************************

print(round(1.23,1))
print(round(1.27,1))
print(round(-1.27,1))
print(round(1.23,1))
print(round(1.25361,3))
print(round(1.25361,-3))
a = 1627731
print(round(a,-1))
print(round(a,-2))
print(round(a,-3))

x = 1.234567
print(format(x, '0.2f'))
st = 'value is {:0.3f}'.format(x)
print(st)
