#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 17:34:03 2019

@author: y56
"""

import math 

hash_table = [     0,  9,  1, 10, 13, 21,  2, 29,
    11, 14, 16, 18, 22, 25,  3, 30,
     8, 12, 20, 28, 15, 17, 24,  7,
    19, 27, 23,  6, 26,  5,  4, 31]

def log2_32(value):
    value |= value >> 1
    value |= value >> 2
    value |= value >> 4
    value |= value >> 8
    value |= value >> 16
    return hash_table[((
                (value * 0x7c4acdd
                ) >> 27 ) % 32)]
check = 0

for x in range(1,2**10):
    check += abs(log2_32(x) - math.floor(math.log2(x)))

print(check)