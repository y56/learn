#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:20:53 2019

@author: y56
"""



tab32 = [
     0,  9,  1, 10, 13, 21,  2, 29,
    11, 14, 16, 18, 22, 25,  3, 30,
     8, 12, 20, 28, 15, 17, 24,  7,
    19, 27, 23,  6, 26,  5,  4, 31]

def log2_32(value):
    value |= value >> 1;
    value |= value >> 2;
    value |= value >> 4;
    value |= value >> 8;
    value |= value >> 16;
    print(bin(value))
    print(bin(value*0x07C4ACDD))
    print([(value*0x07C4ACDD) >> 27])
    print(bin((value*0x07C4ACDD) >> 27))
    

    return tab32[((value*0x07C4ACDD) >> 27) % 32];

print(log2_32(2**31))

             