#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 126_calss_inherit.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-07 09:53:57
#Last Modifieda: 2016-10-07 09:53:57
#*********************************************************

class Mydict(dict):
    def __init__(self):
        dict.__init__({'m': 12})
    def helloworldl(self):
        print "Hello World!"


d = Mydict()
x = [chr(x) for x in range(97,111)]
y = range(97,111)

for a,b in zip(x,y):
    d[a] = b


print d
d.helloworldl()
print "http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/"
