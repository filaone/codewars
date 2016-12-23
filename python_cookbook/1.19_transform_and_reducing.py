#!/usr/bin/python
#-*- coding:utf-8 -*-


nums = [1,2,3,4,5,6]
print(sum(x*x for x in nums))
# 如果使用下面的方法则会产生额外的列表，浪费空间，用一次就丢弃
print([sum(x*x for x in nums)])

#  Determine if any .py file in a directory
import os
files = os.listdir('./')
if any(name.endswith('.py') for name in files):
    print('There Be Python.')
else:
    print("Sorry, no Python.")


# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}
]

min_shares_1 = min(s['shares'] for s in portfolio)
min_shares_2 = min(portfolio, key=lambda k:k['shares'])
print(min_shares_1)
print(min_shares_2)
