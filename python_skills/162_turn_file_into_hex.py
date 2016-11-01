#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 162_turn_file_into_hex.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-31 20:18:17
#Last Modifieda: 2016-10-31 20:18:17
#*********************************************************

import sys
import binascii

def hexdump(filename):
    with open(__file__, "r") as f:
        content = f.read()
    print (binascii.hexlify(content))
hexdump(sys.argv[0])
