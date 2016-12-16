#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 1.06_multiple_dict.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-16 16:50:10
#Last Modifieda: 2016-12-16 16:50:10
#*********************************************************

# 1.06 Mapping Keys to Multiple Values in a Dictionary
# use defaultdict  defaultdict(list)可以保存

from collections import defaultdict

d_list = defaultdict(list)
d_set  = defaultdict(set)

d_list['a'].append(1)
d_list['a'].append(2)
d_list['a'].append(3)
d_list['a'].append(4)
d_list['b'].append(4)
d_list['b'].append(4)
d_list['b'].append(4)

print(d_list)


d_set['a'].add(1)
d_set['a'].add(2)
d_set['a'].add(3)
d_set['a'].add(4)
d_set['b'].add(4)
d_set['b'].add(4)
d_set['b'].add(4)

print(d_set)
