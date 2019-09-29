#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 21:28:12 2019
DSA HW 2
problem 1
@author: y56
"""
def G(A, p, q, r):

    print("G", p, q, r)

    if (p > q) or ((q + 1) > r):
        return -9999

    
    # grow left from q-1 until p to maximize 
    # grow right from q until r-1 to maximize
    # p <--- q || q+1 ---> r
    

    leftSum = A[q] 
    leftMax = leftSum
    i = q - 1
    while i >= p:
        leftSum += A[i]
        if leftSum > leftMax:
            leftMax = leftSum
        i -= 1
    
    rightSum = A[q + 1]  
    rightMax = rightSum
    i = q + 2
    while i < r:
        rightSum += A[i]
        if rightSum > rightMax:
            rightMax = rightSum
        i += 1
        
    return leftMax + rightMax

def H(A, p, q, r, l):

    if (p > q) or ((q + 1) > r) or ((r + 1) > l):
        return -9999

    print("H", p, q, r, l)
    


    # grow left from q-1 until p to maximize 
    # grow right from q until r-1 to maximize
    # p <--- q || q+1 ~ r || r+1 ---> l
    leftSum = A[q] 
    leftMax = leftSum
    i = q - 1
    while i >= p:
        leftSum += A[i]
        if leftSum > leftMax:
            leftMax = leftSum
        i -= 1
    
    rightSum = A[r + 1]  
    rightMax = rightSum
    i = r + 2
    while i <= l:
        rightSum += A[i]
        if rightSum > rightMax:
            rightMax = rightSum
        i += 1
    
    return leftMax + rightMax + sum(A[q + 1 :r + 1])

def F(A, p, l):  # flavored by [p, l)  
    print("F", p, l)
    # [p ~ q)
    # [q ~ r)
    # [r ~ l)
    # I until-now realize that [x, y) is a great design,
    # e.g., in range(x, y), y will not be reached.
    # The great point is that we merge two pieces smoothly.
    # We can do foo(a, b) foo(b, c),
    # rather than boo(a, b) boo(b+1, c).
    if p > l:  # should never happen
        print("ERROR!!!")
        return -99999
    
    if p == l:
        return A[p]

    q = int(p + (l - p) * 1 / 3)
    r = int(p + (l - p) * 2 / 3)
    print("            ", p, q, r, l) 
    
    s1 = F(A, p, q)
    s2 = F(A, q + 1, r)
    s3 = F(A, r + 1, l)
    s12 = G(A, p , q, r)
    s23 = G(A, q + 1, r, l)
    s123 = H(A, p, q, r, l)
    
    return max(s1, s2, s3, s12, s23, s123)

A = [-2, -3, 4, -1, -2, 1, 5, -3]
print(F(A, 0, len(A) - 1))
