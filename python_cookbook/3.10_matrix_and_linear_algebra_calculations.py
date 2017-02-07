#!/usr/bin/python
#-*- coding:utf-8 -*-

# 3.10 Performing Matrix and Linear Algebra Calculations

import numpy as np
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print('m : ', m)

# Return transpose
print('transpose m.T : \n', m.T)

# Return inverse
print('inverse m.I : \n', m.I)

# Create a vector and multiply
v = np.matrix([[2],[3],[4]])
print('m * v', m * v)

import numpy.linalg

# Determinant
print('numpy.linalg.det(m)', numpy.linalg.det(m))

# Eigenvalues
print('numpy.linalg.eigvals(m)', numpy.linalg.eigvals(m))

# Solve for x in mx = v
x = numpy.linalg.solve(m,v)
print('x', x)
print('x * m', m * x)
print('v', v)
