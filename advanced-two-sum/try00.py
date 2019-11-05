#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:23:31 2019

@author: y56
"""
# problem 1, we can find two movie time to sum up as (flight time - 30)
mt = [1, 5, 25, 35, 55, 60]
mt = [1, 10, 25, 35, 60]
mt = [20, 50, 40, 25, 30, 10]
mt = []
def f(mt):
    f = 90
    mtu = f - 30
    md  = {}
    
    maxtime = -1
    maxpair = []
    
    for i in range(len(mt)):
        if mtu-mt[i] in md:
           j = md[mtu-mt[i]]  
           if mt[i]>maxtime or mt[j]>maxtime:
               maxtime = max(mt[i],mt[j])
               maxpair = [j,i]
        if mt[i] not in md:
            md[mt[i]] = i
    print(md)
    if maxpair==[]:
        return []
    if maxpair[0] > maxpair[1]:
        return maxpair[::-1]
    return maxpair

a=f(mt) 
print(a)

# problem 2, we cannot find two movie time to sum up as (flight time - 30)
# we will use (flight time-30) as the upper bound to find a longest movie time

