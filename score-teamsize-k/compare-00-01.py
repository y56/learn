#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:56:11 2019

@author: y56
"""

import try00
import try01
import try01_pretty
import try02

import time

import random


absum = 0
for _ in range(1000):
    
    len_l = random.randint(1,1000)

    n = random.randint(1, len_l)
    k = random.randint(1, len_l)
    
    l = []
    for _ in range(len_l):
        l.append(int(random.random()))
#    l = [35, 65, 21, 46, 59]
    
    l0 = l[:]
    tic = time.time()
    a = try00.f(l0, n, k)
    dt0 = time.time() - tic    
    
    l1 = l[:]
    tic = time.time()
    b = try02.f(l1, n, k)
    dt1 = time.time() - tic    

#    print(len_l, n, k)
#    print(a-b)
    absum += (a-b)

print(dt0/dt1)
print(absum)