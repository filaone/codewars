#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 4.01_consuming_iterator.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2017-03-04 09:42:36
#Last Modifieda: 2017-03-04 09:42:36
#*********************************************************


with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass


