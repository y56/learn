#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:09:52 2019

@author: y56
"""

def maxHeapify(A, i):
    leftChild = 2 * i
#    leftChildValue = A[2 * i]
    rightChild = 2 * i + 1
#    rightChildValue = A[2 * i + 1]
    if i <= len(A) and A[leftChild] > A[i]:
        largestSoFar = leftChild
    else:
        largestSoFar = i
    if rightChild <= len(A) and A[rightChild] > A[largestSoFar]:
        largestSoFar = rightChild
    if largestSoFar != i:
        A[i], A[largestSoFar] = A[largestSoFar], A[i]  # put the largest at i
        maxHeapify(A, largestSoFar)  # Go check the following subtree

def buildMaxHeap(A):
    for i in range(len(A) // 2, 0, -1):
        maxHeapify(A, i)
        


A = [1, 7, 9, 3, 100, 13, 12, 5, 14]
buildMaxHeap(A)