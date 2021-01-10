#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 11:48:44 2021

@author: y56
"""

import  sys

file = open(sys.argv[1], 'r') 
lines = file.readlines() 
  
count = 0
pre_is_minus=None

for line in lines: 
    
    cur_is_minus = '-' == line.split()[1][0]
    
    if pre_is_minus != None and pre_is_minus != cur_is_minus:
        count += 1
    
    pre_is_minus = cur_is_minus
    
print(count)
        