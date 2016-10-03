#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 083_create_ltsd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-03 12:23:50
#Last Modifieda: 2016-10-03 12:23:50
#*********************************************************

# create list tuple set dict

#list [a,b,c,d]
#tuple (a,)
#set
#dict {'a' : 1}

a = list("Hello World!")
b = tuple("Hello World!")
c = set("Hello World!")
d = dict((['x',1],['y',2]))
d2= {}.fromkeys(('x','y'),-1) # default None

print a
print b
print c
print d
print d2
