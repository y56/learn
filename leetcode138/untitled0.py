#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:47:41 2019

@author: y56
"""

import math 

anti_hash_table = [0,1,3,7,15,31,30,28,24,17,2,4,9,18,5,10,
              21,11,22,12,25,19,6,13,27,23,14,29,26,20,8,16]

def log2_32(value):
    value |= value >> 1
    value |= value >> 2
    value |= value >> 4
    value |= value >> 8
    value |= value >> 16
    return anti_hash_table.index((((
                (value*0x7c4acdd - (value>>1)*0x7c4acdd)
                ) >> 27 ) % 32))
check = 0

for x in range(1,2**10):
    check += abs(log2_32(x) - math.floor(math.log2(x)))

print(check)