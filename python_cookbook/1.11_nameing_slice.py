#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 1.11_nameing_slice.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-22 02:39:59
#Last Modifieda: 2016-12-22 02:39:59
#*********************************************************

record = '....................100          .......513.25   ..........'
cost = int(record[20:32]) * float(record[40:48])
print(int(record[20:32]))
print(cost)

SHARES = slice(20,32)
PRICE = slice(40,48)

cost = int(record[SHARES]) * float(record[PRICE])
print(cost)
