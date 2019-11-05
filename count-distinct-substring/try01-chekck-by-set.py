#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:55:05 2019

Input: s = "pqpqs", k = 2
Output: 7
Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]

Input: s = "aabab", k = 3
Output: 0

@author: y56
"""

def f(s,k):
    n=len(s)
    ans=0
    t = [0] * 27
    seen=set()
    for i in range(0,n):
        dc = 0
#        print('i', i)
        t = [0]*27
        for j in range(i,n):
#            print('j', j)
#            print(s[i:j+1])                
            
            if t[ord(s[j])-97]==0:
#                print(s[i:j+1], 'dc=+1')                
                dc+=1
                
            t[ord(s[j])-97]+=1
            if dc==k:
                if s[i:j+1] not in seen:
                    ans+=1
                    seen.add(s[i:j+1])
                else:
                    print("collide", s[i:j+1])
                
#                print("ans + 1 ")                
            if dc>k:
#                print(t)
                break
    print(seen)
    return ans

s1 = "aabaab"
k1 = 2
print(f(s1,k1))