#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 182_gcd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-02 11:17:09
#Last Modifieda: 2016-11-02 11:17:09
#*********************************************************

print "http://angellin0.iteye.com/blog/1811248"
def gcd(a,b):
    if a < b:
        a,b = b,a
    if a % b == 0:
        return b
    return gcd(b,a%b)

def lcm(a,b):
    return a*b/gcd(a,b)

import math
print gcd(35,100)
print lcm(35,100)
