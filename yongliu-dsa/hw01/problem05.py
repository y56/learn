#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:58:59 2019

@author: y56
"""

def T(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return T(n/4) + T(n/2) + n ** 2

for i in range(0,11):
    print(2**i, T(2**i))