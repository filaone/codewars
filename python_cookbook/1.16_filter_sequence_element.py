#!/usr/bin/python
#-*- coding:utf-8 -*-


# 1.16 Filtering Sequence Elements

# Use list comprehension
mylist = [1,4,-5,10,-7,-9,2,3,-1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

pos = (n for n in mylist if n < 0)
for item in pos:
    print(item)


values = ['1', '2', '-3', '-', '4', 'N/A', '5']


# Use BOOL function and filter()
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

print(list(filter(is_int,values)))

#Use math to transform
import math
m_mylist = [math.sqrt(n) for n in mylist if n >0]
print(m_mylist)

r_mylist = [n if n > 0 else 0 for n in mylist]
print('r_mylist : ', r_mylist)

addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK',
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]

counts = [0,3,10,4,1,7,6,1]

from itertools import compress

get_temp = lambda k:int(k.split()[0])
more_3100 = [get_temp(n) > 3100 for n in addresses]
print(more_3100)
print(list(compress(addresses,more_3100)))
