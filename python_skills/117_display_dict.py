#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 117_display_dict.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-04 16:58:44
#Last Modifieda: 2016-10-04 16:58:44
#*********************************************************

d = dict()
x = [chr(x) for x in range(97,111)]
y = range(97,111)

for a,b in zip(x,y):
    d[a] = b

# show directly
print d

# convert to a string
print "http://stackoverflow.com/questions/4547274/convert-a-python-dict-to-a-string-and-back"
print str(d)
# format display
print "http://stackoverflow.com/questions/7409078/iterating-over-dictionary-key-values-corresponding-to-list-in-python"
for key,value in d.iteritems():
    print key,"-----",value
