#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 215_ctype.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-14 15:13:56
#Last Modifieda: 2016-12-14 15:13:56
#*********************************************************

import ctypes,os

# try to locate the .so file in the same directory as this file
_file = 'addon/libsample.so'
# replace ../../215_ctype.py to ../../libsample.so
_path = os.path.join(*(os.path.split(__file__)[:1] + (_file,)))
_mod  = ctypes.cdll.LoadLibrary(_path)

# int gcd(int, int)
gcd = _mod.gcd
gcd.argtypes = (ctypes.c_int, ctypes.c_int)
gcd.restypes = ctypes.c_int

print gcd(35,42)
