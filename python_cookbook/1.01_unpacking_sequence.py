#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 1.01_unpacking_sequence.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-15 13:59:38
#Last Modifieda: 2016-12-15 13:59:38
#*********************************************************

# 1.01 Unpacking a sequence into Separate Variables

data = [ 'ACME', 50,91.1, (2012, 12, 21)]
name, shares, price, date = data
print name
print shares
print price
print date

name_1, shares_1, price_1, (date_Y, date_M, date_D) = data
print date_Y
print date_M
print date_D

# error number
#a,b,c,d = 'Hello'
#print d

a,b,c,d,e = 'Hello'
print d


# use a throwaway variable name such as _ (_ is a variable as a,b,c)
_,b,_,d,e = 'Hello'
print d
