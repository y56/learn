#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 19:41:49 2019

@author: y56
"""

import numpy as np
import random 
import matplotlib.pyplot as plt

t = np.arange(256)  # time 
dt = t[1] - t[0]
N = len(t)
omega = 2*np.pi / N * 10.4  # k=10.4 --> omega=0.2552544

sum_ = np.zeros(N)  # pre-allocation

for i in range(1000):
    Theta = random.random() * 2 * np.pi  # [0,1) * 2 * pi
    G = np.random.normal(0, 1)  # mean=0, sigma=1
    
    x = G * np.cos(omega * t + Theta)
    
    x_i_0_x_i_tau = x[0] * x
    
    sum_ += x_i_0_x_i_tau
    
autocorrelation = sum_/1000

plt.figure()
plt.plot(t, autocorrelation, '.-')
plt.show()

powerspectrum = np.fft.fft(autocorrelation)

freq = np.fft.fftfreq(t.shape[-1])
freq *= 2*np.pi

plt.figure()
plt.plot(freq, powerspectrum.real, label="Re")
plt.plot(freq, powerspectrum.imag, label="Im")
plt.legend()
plt.show()

plt.figure()
plt.plot(freq, abs(powerspectrum), label="Abs")
plt.legend()
plt.show()
