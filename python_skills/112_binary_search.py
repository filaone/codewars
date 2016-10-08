#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 112_binary_search.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-10-04 15:57:36
#Last Modifieda: 2016-10-04 15:57:36
#*********************************************************

def bsearch(l, left, right, num):
    if (left > right):
        return -1
    elif left == right:
        if l[left] == num:
            return left
        else:
            return -1
    else:
        if l[(left + right)/2] > num:
            return bsearch(l, left, (left + right)/2 -1, num)
        elif l[(left + right)/2] < num:
            return bsearch(l, (left + right)/2 + 1, right, num)
        return (left + right)/2


def bsearch2(l, left, right, num):
    while(left <= right):
        mid = (left + right)/2
        if l[mid] > num:
            right = mid - 1
        elif l[mid] < num:
            left = mid + 1
        else:
            return mid
    return -1


l = range(1,100)
print bsearch(l,0,99,8)
print bsearch2(l,0,99,9)
