#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 1.04_largest_smallest_n_items.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-15 21:45:44
#Last Modifieda: 2016-12-15 21:45:44
#*********************************************************

# Finding the Largest or Smallest N items
# Python 2 and Python 3
# 本节的难点在于lambda的应用，暂时理解的意思就是，函数会对元素进行排序，如果没有KEY那么就对元素本身排序
# KEY的作用是从元素中抽取或者转化出比较因子，以比较因子的次序决定总体次序。

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key = lambda s:s['price'])
print((lambda s:s['price'])({'name': 'IBM', 'shares': 100, 'price': 91.1}))

heap = list(nums)
print(heap)
heapq.heapify(heap)
print(heap)
heapq.heappop(heap)
print(heap)
