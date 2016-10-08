#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 121_list_dict_sort.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-06 18:46:19
#Last Modifieda: 2016-10-06 18:46:19
#*********************************************************


data = [[1,5,5], [2,4,7], [3,3,2]]
data2 = [(1,5,5), (2,4,7), (3,3,2)]

print sorted(data, key = lambda l : l[1], reverse=False)
data2.sort(key = lambda t : t[2], reverse = True)
print data2
print "http://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples"


d = dict()
x = [chr(x) for x in range(97,111)]
y = range(97,111)

for a,b in zip(x,y):
   d[a] = b
print d
print [(k, d[k]) for k in sorted(d.keys())]

# dict 本身是无序的，需要用defaultdict来解决

print sorted(d.items(), lambda x, y: cmp(x[1],y[1]), reverse = True)
print type((d.items())[1]) # tuple

print "key items : ",sorted(d.items(), key = lambda x : x[1], reverse = True)

