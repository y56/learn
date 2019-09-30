#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:44:24 2019

@author: y56
"""

import myProblem01Function
import otherProblem01Function01
import random

check = []
wrongCase = []

for _ in range(1000):
    
    A = []
    for i in range(10):
        r = random.randint(-20, 20)
        A.append(r)
    my = myProblem01Function.myProblem01Function(A)
    other = otherProblem01Function01.maxSubArraySum(A, len(A))
    if my - other != 0:
        wrongCase = A
        print(my, other, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        break
        
        

print(A)
[17, -17, -20, -7, 19, -15, -1, 2, -6, -4]