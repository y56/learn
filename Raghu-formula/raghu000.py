#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 22:40:14 2019

@author: y56
"""

from matplotlib import pyplot as plt 

def me(n):
    l = 0.77
    return l**(n-1) * (l ** n-1)/(l-1)
def r(n):
    l = 0.77
    sum = 0
    for i in range(n-1, 2*n-2+1):
        sum += l ** i
    return sum

l = []
me_coll = []
r_coll = []
for i in range(1,100):
    l.append(i)
    me_coll.append(me(i))
    r_coll.append(r(i))

plt.plot(l, me_coll, 'o ',  l, r_coll)
    