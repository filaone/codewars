#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 145_do_file_rescuit.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-10 19:06:52
#Last Modifieda: 2016-10-10 19:06:52
#*********************************************************

import os
import shutil

#shutil.copytree("./addon/144_dir","./addon/145_dir")

for root, subdir, files in  os.walk("./addon/145_dir",False):
    print "the False means topdown mode"
    print root
    print subdir
    print files
    for doc in files:
        os.rename("")
