#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 03:43:16 2019

@author: y56
"""

r1dict = {1:'I',10:'X',100:'D'}
r5dict = {1:'V',10:'L',100:'M'}
for d in [1,10,100]: # d is for decimal base
    r1 = r1dict[d]  # roman digit 1
    r5 = r5dict[d]  # roman digit 5
    myDict = {1*d:r1, 2*d:r1*2,3*d:r1*3, 4*d:r1+r5, 5*d:r5,6*d:r5+r1, 7*d:r5+r1*2, 8*d:r5+r1*3, 9*d:r1+r5}
    print(myDict)