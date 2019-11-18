#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:30:48 2019

@author: y56
"""

import heapq

def f(l, n, k): 
    
    total = 0
    
    if len(l) >= 2 * k:  
        # Do heapification once, 
        # if long enough such that there are non-empty middle.
        
        middle = l[k:-k]
        frontHeap = l[0:k]
        backHeap = l[-k:]
        
        heapq._heapify_max(frontHeap)
        heapq._heapify_max(backHeap)
        
    else:  # not long enough, to wait to be merged
        
        middle = []
        frontHeap = []
        backHeap = l  # to be the same format as line-65
    
    hasDoneBefore = False
    
    for _ in range(n):
        
        if len(middle) > 0:
            
            front_most_neg = frontHeap[0]
            back_most_neg = backHeap[0]
            
            if front_most_neg <= back_most_neg:
                
                total += front_most_neg

                # heapreplace = pop-then-push
                heapq._heapreplace_max(frontHeap, middle[0])  
                del middle[0]
                
            else:
                
                total += back_most_neg
                
                # heapreplace = pop-then-push
                heapq._heapreplace_max(backHeap, middle[-1])
                del middle[-1]
                
        else:  # Now middle is empty, merge all to a single heap.
            
            if hasDoneBefore == False:
                wholeHeap = frontHeap + backHeap  # Pour all stuff to backHeap
                heapq._heapify_max(wholeHeap)  # and then heapify it only once
                hasDoneBefore = True
                
            pick = heapq._heappop_max(wholeHeap)
            total += pick
            
    return total 