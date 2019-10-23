#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 22:33:06 2019

@author: y56
"""

import dis

def f():
    return 0.2**0.5

print(dis.dis(f))