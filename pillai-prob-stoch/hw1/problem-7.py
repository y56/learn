#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:40:34 2019

@author: y56
"""
import numpy as np 
from matplotlib import pyplot as plt 
import math

def C(a,b):
    return math.factorial(a)/math.factorial(a-b)/math.factorial(b)
p = np.arange(0, 1, 0.01) 
def P_func(n, p):
    q = 1-p
    sum = 0
    for k in range(0, int((n+1)/2)):
        sum += C((n+1)/2-1+k, k) * p**((n+1)/2-1) * q**k * p
    return sum
P7 = []
for p_item in p:
    P7.append(P_func(7, p_item))
P9 = []
for p_item in p:
    P9.append(P_func(9, p_item))
P11 = []
for p_item in p:
    P11.append(P_func(11, p_item))
    
P111 = []
for p_item in p:
    P111.append(P_func(111, p_item))
P211 = []
for p_item in p:
    P211.append(P_func(211, p_item))
plt.title("P(p;n)") 
plt.xlabel("p, for winning a single game") 
plt.ylabel("P, for winning the series")
plt.plot(p,P7) 
plt.plot(p,P9) 
plt.plot(p,P11) 
plt.plot(p,P111)
plt.plot(p,P211) 
plt.legend(["n=7","n=9","n=11", "n=111", "n=211"])
plt.grid()
plt.show()
