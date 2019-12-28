#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 22:07:59 2019

12. 
(5 points)
 You are given two arrays A and B, each of length n. Array A contains
distinct numbers sorted in increasing order. Array B contains distinct numbers sorted in
decreasing order. Construct a O(log n) time divide-and-conquer algorithm that computes
the index i, if it exists, so that A[i] equals B[i]. Be precise.

@author: y56
"""

def F(A,B):

    def f(n,A,B,L,R):
        print(L,R)
        
        if L > R: # actually, no need to check: L<0 or R>n-1 
            return -1
        
        i = (L+R)//2
        
        if B[i] == A[i]:
            return i 
        
        # so it is not yet
        if A[i] > B[i]:
            return f(n,A,B,L,i-1)
        else:
            return f(n,A,B,i+1,R)
        
    n=len(A)
    
    return f(n,A,B,0,n-1)

A = [1,2,3,4,5,6,7]
B = [8,8,8,8,8,8,8]
print(F(A,B))
