#!/usr/bin/python
#-*- coding:utf-8 -*-

def whoIsNext(names, r):
    while r > 5:
        r = (r - 4) / 2
    return names[r-1]


def whoIsNext2(names, r):
    n = len(names)
    k = 2 ** int(math.log(1 + (r - 1) // n, 2))
    s = 1 + (k - 1) * n
    return names[(r - s) // k]

def whoIsNext_my(names, r):
    # your code
    count = 0;
    while (r > (pow(2,count + 1) - 1)*len(names)):
        count+=1
    new_r = int((r - (pow(2, count) - 1) * len(names) - 1)/pow(2, count))
    return names[new_r]