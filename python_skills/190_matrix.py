#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 190_matrix.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-02 16:31:26
#Last Modifieda: 2016-11-02 16:31:26
#*********************************************************

print "http://stackoverflow.com/questions/568962/how-do-i-create-an-empty-array-matrix-in-numpy"
import numpy
a = numpy.zeros(shape=(5,2))
print a
print a[0][1]
a[0][1] = 1
print a[0][1]
