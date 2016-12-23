#!/usr/bin/python
#-*- coding:utf-8 -*- 

# 2.03 Matching String using Shell Wildcard Patterns

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('spam.txt','*.txt'))
print(fnmatch('Dat45.tx','Dat[1-9]*'))
print(fnmatch('foo.app','?oo.app'))


print(fnmatchcase('spam.txt','*.txt'))

addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]

print([addr for addr in addresses if fnmatch(addr,'*CLARK*')])
