#!/usr/bin/python
#-*- coding:utf-8 -*-

# Calculating with Dictionaries

import os

prices = {
'ACME' : 45.23,
'AAPL' : 612.78,
'IBM' : 205.55,
'HPQ' : 37.20,
'FB' : 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print(min_price)
print(max_price)

#zip 返回一个迭代器智能使用一次
#可以保存迭代器的中间结果，但是不能够再次使用迭代器。
#待检测，是否只是PYTHON3的错误
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
#print(max(prices_and_names))

print(min(prices, key = lambda k:prices[k]))
print(sorted(prices, key = lambda k:prices[k]))
End = input("Press Enter to End!")
