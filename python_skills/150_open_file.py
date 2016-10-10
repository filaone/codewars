#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 150_open_file.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-10 22:08:27
#Last Modifieda: 2016-10-10 22:08:27
#*********************************************************


with open("150_open_file.py","r") as f:
    for line in f:
        print line.strip()
