#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 00:19:55 2019

@author: y56
"""

import numpy as np
import random
import matplotlib.pyplot as plt

t = np.linspace(0, 210, 1001)

x = []
for _ in range(len(t)):
    x.append(random.random())
x = np.cos(t)

tau = t
a = []
for i_tau in range(0, len(t)-10):
    sum_ = 0
    #check = 0
    for j in range(0, len(t) - i_tau):
        sum_ += (x[j + i_tau] * x[j])/(len(t)-i_tau)
        #check += 1
    #print(check)
    a.append(sum_)
    
plt.plot(t,x)
plt.show()
plt.plot(a)
plt.show()