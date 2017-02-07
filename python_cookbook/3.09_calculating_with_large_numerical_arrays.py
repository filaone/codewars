#!/usr/bin/python
#-*- coding:utf-8 -*-

import numpy as np
x = [1,2,3,4]
y = [5,6,7,8]
print('x*2', x*2)

print('x + y', x  + y)

ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])
print('ax * 2', ax * 2)
print('ax + 10', ax + 10)
print('ax + ay', ax + ay)
print('ax * ay', ax * ay)

print('np.sqrt(ax)', np.sqrt(ax))
print('np.cos(ax)',np.cos(ax))

grid = np.zeros(shape=(1000,10),dtype=float)
print('grid', grid)
grid += 10
print('grid + 10', grid)
print('np.sin(grid)', np.sin(grid))

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print('a', a)
print('Select row 1 : a[1]', a[1])
print('Select Column 1', a[:,1])
print('Select a subregion and change it \n', a[1:3, 1:3])
# the edit of the subregion will be save in the origin matrix
a[1:3,1:3] *= 10
print(a)

# Broadcast a row vector across an operation on all rows
print('a + [100,101,102,103]\n', a + [100,101,102,103])

# Conditional assignment on an array
print('np.where(a<10,a,10)\n', np.where(a<10,a,10))
