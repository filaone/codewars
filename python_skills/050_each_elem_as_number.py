#!/usr/bin/python
#-*- coding:utf-8 -*-
#**********************************************************
#Filename: 050_each_elem_as_number.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-09-05 21:09:25
#Last Modifieda: 2016-09-05 21:09:25
#*********************************************************

string_1 = "Hello world"
x = lambda y:unichr(y)
m = lambda n:ord(n) # accept char
f = lambda x:chr(x) # accept number
print x(97)
print m("a")

