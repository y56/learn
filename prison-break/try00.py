#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 01:32:36 2019

The prison is m by n

    
   ____
m |    |
  |____|
 
    n
    
@author: y56
"""
def longestSuccessiveLength(h):
    dh = [latter - former for former, latter in zip(h[0:-1], h[1:])]
    # print(dh)
    count = 0
    countCollect = []
    for item in dh:
        if item == 1:
            count += 1
        else:
            countCollect.append(count)
            count = 0
    if count != 0:
        countCollect.append(count)    
    # print(countCollect)
    return max(countCollect) + 1

def f(m,n,h,v):
    return (longestSuccessiveLength(h) + 1) * (longestSuccessiveLength(v) + 1) 
    