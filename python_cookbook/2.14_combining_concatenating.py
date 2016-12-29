#!/usr/bin/python
#-*- coding:utf-8 -*-

# 2.14 Combining and Concatenating Strings

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)

print('{} {}'.format(a,b))
a = 'Hello' 'World'
print(a)

s = ''
# not recommend
for item in parts:
    s += item

new_a = " ".join(str(item) for item in parts if item != 'Is')
new_b = " ".join(str(item) if 'i' in item else 'NNN' for item in parts)
print(new_a)
print(new_b)

import re
pat = re.compile(r'[iI]')
new_c = " ".join(str(item) if pat.findall(item) else 'NNN' for item in parts)
print(new_c)


data = ['ACME', 50, 91.1]
print(data[0],data[1],data[2], sep=':')

def combine(source, maxsize=3):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield "".join(parts)
            parts = []
            size = 0
    yield "".join(parts)

def sample():
    yield "Is"
    yield "Chicago"
    yield "Not"
    yield "Chicago"
    yield "?"

for part in combine(sample()):
    print(part)
