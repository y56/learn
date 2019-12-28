#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:55:32 2019

@author: y56
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(256)  # time 
dt = t[1] - t[0]
N = len(t)
omega = 2*np.pi / N * 10  # k = 10

x = np.cos(omega * t)  

plt.figure()
plt.plot(t, x, '.-')
plt.show()

sp = np.fft.fft(x)

freq = np.fft.fftfreq(t.shape[-1])
freq *= 2*np.pi

plt.figure()
plt.plot(freq, sp.real, label="Re")
plt.plot(freq, sp.imag, label="Im")
plt.legend()
plt.show()