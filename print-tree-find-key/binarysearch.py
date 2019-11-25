#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:15:05 2019

@author: y56
"""




def binarysearch(sortedlist, key):
    
    def binarysearchhelper(sortedlist, key, low, high):
        
        if low < high:
            return -1
            
        mid = (low + high) // 2
        
        if (key == sortedlist[mid]): 
            return mid 
  
        if (key > sortedlist[mid]): 
            return binarysearchhelper(sortedlist, 
               (mid + 1), high, key) 
      
        return (binarysearchhelper(sortedlist, low, 
               (mid -1), key)) 
    
    return binarysearchhelper(sortedlist, key, 0, len(sortedlist))

if __name__ == '__main__':
    
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    result = binarysearch(a, 1)
    print(result)
        
        