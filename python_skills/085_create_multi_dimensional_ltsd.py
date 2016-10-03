
#**********************************************************
#Filename: 085_create_multi_dimensional_ltsd.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-03 16:48:19
#Last Modifieda: 2016-10-03 16:48:19
#*********************************************************

import copy

l = ['a','b','c','d','e']
t = ('a','b','c','d','e','e')
s = set(['a','b','c','d','e','e',])
d = {'a':1, 'b':2, 'c':3}

l2 = copy.copy(l)
l2[1] = t
l2[2] = s
l2[3] = d
l2[4] = l2
print l2

# set cannot add dict
s.add(t)
print s
