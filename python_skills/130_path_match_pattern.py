#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 130_path_match_pattern.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-07 10:55:24
#Last Modifieda: 2016-10-07 10:55:24
#*********************************************************

import fnmatch
import os

for file in os.listdir('./'):
    if fnmatch.fnmatch(file, '[12][34][12]*.py'):
        print file
    else:
        print "not : ",file


