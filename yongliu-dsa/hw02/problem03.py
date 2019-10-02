#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:09:52 2019

@author: y56
"""

def maxHeapify(A, i):
    
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2
    print("heapify", "me", i, "left", leftChild, "right", rightChild)
    
    largestSoFar = i
    
    if leftChild < len(A):  # index may go out of range!
        if A[leftChild] > A[i]:
            largestSoFar = leftChild
        
    if rightChild < len(A):  # index may go out of range!
        if A[rightChild] > A[largestSoFar]: 
            largestSoFar = rightChild
            
    if largestSoFar != i:
        A[i], A[largestSoFar] = A[largestSoFar], A[i]  # put the largest at i
        maxHeapify(A, largestSoFar)  # Go check the following subtree

def buildMaxHeap(A):
    for i in range(len(A) // 2 - 1, -1, -1):
        print(i, "build")
        maxHeapify(A, i)
        
A = [1, 7, 9, 3, 100, 13, 12, 5, 14]
buildMaxHeap(A)
print(A)
