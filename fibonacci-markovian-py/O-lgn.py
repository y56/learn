#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:41:00 2019

@author: y56
"""

import numpy

def F(n):
    if n==0:
        return 1
    O = numpy.array([[1,1], [1,0]])  # Markovian operator
    v = numpy.array([[1], [1]])  # initial condition
    A = numpy.array([[1,0], [0,1]])  # identity
    #print(bin(n))
    while n != 0:
        if n & 1 == 1:  # if the LSB/right-most bit is 1
            A = numpy.dot(O,A)
        n >>= 1  # n = n // 2
        O = numpy.dot(O,O)
        #print(bin(n))
    
    v = numpy.dot(A,v)
    
    return v[0][0]

for i in range(1,100):
    print(F(i))