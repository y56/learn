#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:38:58 2019

@author: y56
"""

import numpy

def F(n):
    if n==0:
        return 1
    O = numpy.array([[1,1], [1,0]])  # Markovian operator
    v = numpy.array([[1], [1]])  # initial condition
    for _ in range(n-1):
        v = numpy.dot(O,v)
    return v[0][0]
for i in range(10):
    print(F(i))
    