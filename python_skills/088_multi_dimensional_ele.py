
#**********************************************************
#Filename: 088_multi_dimensional_ele.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-03 17:25:04
#Last Modifieda: 2016-10-03 17:25:04
#*********************************************************
import copy

l = ['a','b','c','d','e','f']
l2 = copy.copy(l)
for ele in l2:
    ele += '2'

l2[0] = l
print l2

def get_Element(l):
    for ele in  l:
        if type(ele) == list:
            print "Get a list"
            get_Element(ele)
        else:
            print ele

get_Element(l2)
