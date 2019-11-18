#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 02:29:23 2019

We will look for the max in the first k elements and last k elements.
If we are have two equal values, we will choose the one with a lower index.
Those chosen will be removed from the list.
If the list is shorter than k, use the whole list.


`l` is a list
We will chose `n` elements. 
`k` is the length of the range.

@author: y56
"""
# We are doing in a naive way
def f(l, n, k): 
    sum = 0
    for _ in range(n):
#        print(l)
        if len(l) > k: # still possible to have fist k and last k
            # list.index(x) will only return the index in the list of the first
            # item whose value is x
            f = l[0:k]  # front
            b = l[-k:]  # back
            
#            print(f,b)
            
            fmax = max(f)
            findex = f.index(fmax)
            
            bmax = max(b)
#            print(fmax,bmax,b.index(bmax))
            bindex = b.index(bmax) + len(l) - k
#            print(fmax,bmax,b.index(bmax),bindex)
            
            if fmax > bmax:
#                print("pick:", fmax)
                sum += fmax
                del l[findex]
            if fmax < bmax:
#                print("pick:", bmax)
                sum += bmax
                del l[bindex]
            if fmax == bmax:
                if bindex < findex:
#                    print("pick:", bmax)
                    sum += bmax
                    del l[bindex]
                else:
#                    print("pick:", fmax)
                    sum += fmax
                    del l[findex]
        else:
            tmax = max(l) # tamx: total max
            tindex = l.index(tmax)
            sum += tmax
#            print("pick:", tmax)
            del l[tindex]
    return sum 

#l = [1, 9, 6, 3, 8, 0, 56, 98]
#print(f(l, 5, 3))