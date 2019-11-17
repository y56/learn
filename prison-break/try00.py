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
def maxSuccessiveLen(h):
    if len(h) == 1:
        return 1
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

def maxCellArea(m, n, h, v):
    return (maxSuccessiveLen(h) + 1) * (maxSuccessiveLen(v) + 1) 

print(maxCellArea(10, 10, [1], [1]))
print(maxCellArea(10, 10, [1], [1]))
print(maxCellArea(10, 10, [1, 3, 5, 7, 9], [1, 2]))