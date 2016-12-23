#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 1.10_remove_duplicate.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-22 02:06:06
#Last Modifieda: 2016-12-22 02:06:06
#*********************************************************

# 1.10 Removing Duplicates from a Sequence while Maintaining Order

def dedup(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
    print(seen)


# 原文章在这一部分有错误，如果在未更改key的情况下依然是unhashable的话还是会出现错误。
def dedup_2(items, key = None):
    seen = list()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            print(val)
            yield item
            seen.append(val)
        print(seen)




a = [1,5,1,2,6,8,4,6,2,9,0,1]
print(list(set(a)))
template = dedup(a)
a = list(template)
print(a)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

print(a)
print("1,2,3")
template  = dedup_2(a, key = lambda d:(d['x'],d['y']))
new_a = list(template)
print(new_a)
template = dedup_2(a,key = lambda d:d['y'])
new_a = list(template)
print(new_a)
template = dedup_2(a)
new_a = list(template)
print(new_a)

a = [1,2,5,34,3,4,5,6,34,2,5,1,1,2,3,4,4,2,2,4,5,8]
# not keep order
print(set(a))

#with open('somefile.py','r') as f :
#    for line in dedup(f):
#        ..._

