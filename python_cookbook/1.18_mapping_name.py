#!/usr/bin/python
#-*- coding:utf-8 -*-

# 1.18 Mapping Names to Sequence Elements

from collections import namedtuple

Subscriber = namedtuple('Subscriber',['addr','joined'])
sub = Subscriber('buaa_wsg@163.com','2016-12-23')
print(sub.addr," ", sub.joined)

Stock = namedtuple('Stock', ['name','shares','price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

def compute_cost_old(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

records = (['uniS',60,432],['HG',500,23222],['Cd',55.333,22323])
print(compute_cost(records))
print(compute_cost_old(records))
HG = Stock(*records[1])
print(HG.name)
# HG = HG._replace ! cannot set attr BUT use the _replace
HG = HG._replace(name="HHGG")
# no influence to HG
HG.replace(name="HHHGGG")
print(HG)
print(HG.name)
