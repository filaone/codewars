#!/usr/bin/python
#-*- coding:utf-8 -*-

# 2.20 Performing Text Operations on Byte Strings

data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))

print(data.split(b' '))
print(data.replace(b'He',b'Wa'))

a = "Hello World"
print(a[1])
print(data[1])

print(data)
print(data.decode('utf-8'))
