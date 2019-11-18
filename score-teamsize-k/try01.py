#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:34:38 2019

We will look for the max in the first k elements and last k elements.
If we are have two equal values, we will choose the one with a lower index.
Those chosen will be removed from the list.
If the list is shorter than k, use the whole list.


`l` is a list
We will chose `n` elements. 
`k` is the length of the range.

@author: y56
"""

import heapq

def f(l, n, k): 
    
    # python3 has only min-heap
    neg_l = [-x for x in l]
#    print(neg_l)
    neg_sum = 0
    
    if len(neg_l) >= 2 * k:  # Anyway, do heapification once if long enough
        # long enough such that there are non-empty middle
        
        frontHeap = neg_l[0:k]
        backHeap = neg_l[-k:]
        heapq.heapify(frontHeap)
        heapq.heapify(backHeap)
        middle = neg_l[k:-k]
#        print(frontHeap, middle, backHeap)
        
    else:  # not long enough, to wait to be merged
        
        middle = []
        frontHeap = []
        backHeap = neg_l
    
    hasDoneBefore = False
    
    for _ in range(n):
        
        
        if len(middle) > 0:
#            print(frontHeap, middle, backHeap)
            
            front_most_neg = frontHeap[0]
            back_most_neg = backHeap[0]
            
            if front_most_neg <= back_most_neg:
                
                neg_sum += front_most_neg
#                print("pick:", front_most_neg)
#                print(middle)

                heapq.heapreplace(frontHeap, middle[0])
                del middle[0]
                
            if front_most_neg > back_most_neg:
                
                neg_sum += back_most_neg
#                print("pick: --back--", back_most_neg)
#                print(middle, backHeap)
                
                heapq.heapreplace(backHeap, middle[-1])
                del middle[-1]
                
#                print(middle, backHeap)
                
#            print(frontHeap, middle, backHeap)
            
        else:  # Now middle is empty, merge all to a single heap.
            
            if hasDoneBefore == False:
                backHeap = frontHeap + backHeap  # to pour all stuff to backHeap
                heapq.heapify(backHeap)
                hasDoneBefore = True
                
#            print(backHeap)
            pick = heapq.heappop(backHeap)
            neg_sum += pick
#            print("pick:", pick)
#            print(backHeap)
            
    return -neg_sum 

#l = [1, 9, 6, 3, 8, 0, 56, 98]
#print(f(l, 5, 3))