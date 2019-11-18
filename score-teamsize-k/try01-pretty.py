#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:11:01 2019

We will look for the max in the first k elements and last k elements.
If we are have two equal values, we will choose the one with a lower index.
Those chosen will be removed from the list.
If the list is shorter than k, use the whole list.

@author: y56
"""

import heapq

def f(l, n, k): 
    
    # python3 has only min-heap, so take minus on all element 
    # and then take minus again when return it
    neg_l = [-x for x in l]
    neg_sum = 0
    
    if len(neg_l) >= 2 * k:  
        # Do heapification once, 
        # if long enough such that there are non-empty middle.
        
        middle = neg_l[k:-k]
        frontHeap = neg_l[0:k]
        backHeap = neg_l[-k:]
        
        heapq.heapify(frontHeap)
        heapq.heapify(backHeap)
        
    else:  # not long enough, to wait to be merged
        
        frontHeap = []
        backHeap = neg_l  # to be the same format as line-65
    
    hasDoneBefore = False
    
    for _ in range(n):
        
        if len(middle) > 0:
            
            front_most_neg = frontHeap[0]
            back_most_neg = backHeap[0]
            
            if front_most_neg <= back_most_neg:
                
                neg_sum += front_most_neg

                # heapreplace = pop-then-push
                heapq.heapreplace(frontHeap, middle[0])  
                del middle[0]
                
            else:
                
                neg_sum += back_most_neg
                
                heapq.heapreplace(backHeap, middle[-1])
                del middle[-1]
                
        else:  # Now middle is empty, merge all to a single heap.
            
            if hasDoneBefore == False:
                wholeHeap = frontHeap + backHeap  # Pour all stuff to backHeap
                heapq.heapify(wholeHeap)  # and then heapify it only once
                hasDoneBefore = True
                
            pick = heapq.heappop(wholeHeap)
            neg_sum += pick
            
    return -neg_sum 
