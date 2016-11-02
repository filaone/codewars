#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 189_get_random_number.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-11-02 15:55:27
#Last Modifieda: 2016-11-02 15:55:27
#*********************************************************

import random
#default is time
#print random.getrandbits(1000000)
random.seed(2)
print random.random()
print random.randint(1,100)
print random.randint(1,100)
print random.randint(1,100)

with open("/dev/random","rb") as file:
    print [ord(x) for x in file.read(10)]
print "http://stackoverflow.com/questions/14720799/how-to-get-numbers-from-dev-random-using-python"
