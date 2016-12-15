#!/usr/bin/python
#-*- coding:utf-8 -*-

#**********************************************************
#Filename: 1.02_unpacking_arbitrary_length.py
#Author: Andrew Wang - shuguang.wang1990@gmail.com
#Description: ---
#Create: 2016-12-15 14:32:33
#Last Modifieda: 2016-12-15 14:32:33
#*********************************************************

# 1.02 Unpacking Elements from Iterables of Arbitrary Length

recorder = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)

print(type(recorder))

def drop_first_last(recorders):
    first, *middle, last = recorders
    return avg_2(middle, len(middle))

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

def avg(recorder, length):
    sum = 0
    for i in range(length):
        sum += recorder[i]
    return sum / length

def avg_2(recorder, length):
    return sum(recorder) / length

print(drop_first_last(recorder), 'hello', end='')


record = ('Dave', 'dave@example.com','773-555-1212', '843-463-9383')
name, email, *phone_number = record
print(name)
print(email)
print("pay attention phone number is a list")
print(phone_number)

records = [
        ('foo',1,2),
        ('bar','Hello'),
        ('foo',3,4)
        ]
def do_foo(x,y):
    print('FOO', x, y)

def do_bar(s):
    print('BAR',s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    else:
        do_bar(*args)
