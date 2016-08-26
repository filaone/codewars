#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 038_Parse_string_float_or_int.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-08-25 23:00:58
#Last Modifieda: 2016-08-25 23:00:58
#*********************************************************
import os

string_1 = "1234"
string_2 = "12.34567346456756745634"


print float(string_1)
print float(string_2)
print int(string_1)
try:
    print int(string_2)
except ValueError , e:
    print "you can use ValueError as e or , e"
    print "ValueError: ",e

print "a good method is using int(float())"
print int(float(string_2))

print format(1233245, 'b')
print bin(1233245)
print bin(-1233245)
print format(12341, 'x'),": hex"
print format(12345, 'o'),": Oct"
print hex(1234) 
oct_num=oct(12354)
print "oct_num is a string"
print int(oct_num, 8)

print "2-binary"
print "8-octal"
print "10-decimal"
print "16-hex"

string_3 = "777"
i = int(string_3, 8)
print i == 0777
print int(oct(i))
print i
oct_num = oct(int("0777", 8))
print oct_num == 0777


os.chmod("./037_string_of_integer.py", 0644)

i = int("0644",8)
print i
os.chmod("./038_Parse_string_float_or_int.py", i)
