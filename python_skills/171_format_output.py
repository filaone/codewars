#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 171_format_output.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-01 22:35:22
#Last Modifieda: 2016-11-01 22:35:22
#*********************************************************

print "https://pyformat.info/"
print "{1} {0}".format("one","two")
print '{:_>10}'.format("test")
print '{:10}'.format("testtesttesttest")
print '{:_<10}'.format("test")
print '{:_^10}'.format("test")
print '{:.5}'.format("telephone")
print '{:_^10.5}'.format("telephone")
print '{:d}'.format(42)
print '{:f}'.format(2.1512324535567567567)
print '{:06.2f}'.format(2.1512324535567567567)
print "total length = 6, after point = 2"
print '{:05d}'.format(56)
