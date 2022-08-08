#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 01:15:59 2022

Environment:
    Python 3.6.9 (default, Oct  8 2020, 12:12:24)
    IPython 7.13.0 -- An enhanced Interactive Python.

Conclusion:
    Using slice in for-loop takes 5% extra time.


@author: y56
"""


import time
start_time = time.time()
for _ in range(1000):
    li=list(range(100000))
    x=1
    for i in li[1:]:
        x+=1
print("--- %s seconds ---" % (time.time() - start_time))

#--- 7.620156764984131 seconds ---
#--- 7.646716833114624 seconds ---
#--- 7.757232904434204 seconds ---
#--- 7.043309688568115 seconds ---
#--- 6.985918283462524 seconds ---
#--- 7.086709976196289 seconds ---
"""ave: 7.36"""

import time
start_time = time.time()
for _ in range(1000):
    li=list(range(100000))
    x=1
    for i in li:
        x+=1
print("--- %s seconds ---" % (time.time() - start_time))

#--- 7.111480712890625 seconds ---
#--- 7.424499988555908 seconds ---
#--- 7.283886909484863 seconds ---
#--- 6.7081990242004395 seconds ---
#--- 6.807111978530884 seconds ---
#--- 6.736523866653442 seconds ---
"""ave: 7.01"""
