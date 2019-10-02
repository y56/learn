#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 20:40:47 2019

@author: y56
"""

def maxHeapify(A, i, n):
    
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2
    
    largestSoFar = i
    
    if leftChild <= n:  # index may go out of range!
        if A[leftChild] > A[i]:
            largestSoFar = leftChild
        
    if rightChild <= n:  # index may go out of range!
        if A[rightChild] > A[largestSoFar]: 
            largestSoFar = rightChild
            
    if largestSoFar != i:
        A[i], A[largestSoFar] = A[largestSoFar], A[i]  # put the largest at i
        maxHeapify(A, largestSoFar, n)  # Go check the following subtree

def buildMaxHeap(A):
    for i in range(len(A) // 2 - 1, -1, -1):
        maxHeapify(A, i, len(A) - 1)
        

def heapSort(A):
    print("                                ", "Build")
    buildMaxHeap(A)
    print(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        print("                                ", "Swap", "0,", i)
        print(A)
        print("                                ", "Heaptify", 0, "..", i - 1)
        maxHeapify(A, 0, i - 1)
        print(A)
    
A = [1, 7, 9, 3, 100, 13, 12, 5, 14]
print("                                ", "Initiate")
print(A)
heapSort(A)
print("                                ", "Finish")
print(A)
