#!/usr/bin/python
#-*- coding:utf-8 -*- 

# 2.13 Aligning Text Strings

text = 'Hello World'
print(text.rjust(20))
print(text.ljust(20))
print(text.center(20))
print(text.rjust(20,'='))
print(text.ljust(20,'-'))
print(text.center(20))

print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
print(format(text, '=>20'))
print(format(text, '*<20'))
print(format(text, '^20'))

print('{:>10s}{:>10s}'.format('Hello', 'World'))

x = 1.23456
print(format(x, '^10.2f'))
