#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:32:16 2020

@author: y56
"""

def f(s):
    tot=sum(map(int,s))
    ans = int(tot%3==0)
    for c in s:
        for i in range(10):
            if i==int(s):
                continue
            if (tot+i-int(c))%3==0:
                ans+=1
    return ans
print(f('01'))
        