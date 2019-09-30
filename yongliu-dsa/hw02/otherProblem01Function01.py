#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:41:48 2019

https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

@author: y56
"""

from sys import maxint 
def maxSubArraySum(a,size): 
       
    max_so_far = -maxint - 1
    max_ending_here = 0
       
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0   
    return max_so_far 
   
# Driver function to check the above function  

# print("Maximum contiguous sum is", maxSubArraySum(a,len(a)) 
   
#This code is contributed by _Devesh Agrawal_ 