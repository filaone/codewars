#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 142_create_symbolic_link.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-10 13:38:29
#Last Modifieda: 2016-10-10 13:38:29
#*********************************************************

import os
import shutil
import glob

def  bulk_create_symlink(src_target, dst_target):
    doc_list = glob.glob(src_target)
    for doc in doc_list:
        os.symlink(doc, dst_target)


print glob.glob("./*")


shutil.copy(__file__, "./addon/142")
print os.path.realpath(__file__)
pwd = os.path.dirname(os.path.realpath(__file__))
os.symlink(pwd+"/addon/142", pwd+"/addon/142_link")

