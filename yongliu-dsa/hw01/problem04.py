#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:18:50 2019

@author: y56
"""

def T(n):
    if n == 1:
        print(1)
        return 1
    a = 2 * T(2/3*n) + n
    print(a)
    return a

T((3/2)**10)


from math import log as log

a = log(2)/log(1.5)

def f(n):
#    return n**(log(2)/log(1.5)) + 3*n**(1+log(4/3)/log(3/2))-3*n    
    return 4*n**a - 3*n    
for i in range(0,11):
    print(f((3/2)**i))

for i in range(0,11):
    print((5*((3/2)**i)**a-5*(3/2)**i))

for i in range(0,11):
    print(f((3/2)**i) - (5*((3/2)**i)**a-5*(3/2)**i)  )


for i in range(0,11):
    print((3/2)**i  )