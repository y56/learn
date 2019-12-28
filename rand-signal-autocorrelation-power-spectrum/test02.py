#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 19:30:32 2019

@author: y56
"""
import numpy as np
import matplotlib.pyplot as plt


t = np.arange(256)  # time 
dt = t[1] - t[0]
N = len(t)
x = np.cos(0.25 * t)  # cos() omega_0 = 0.25

plt.figure()
plt.plot(t, x, '.-')
plt.show()

sp = np.fft.fft(x)

myfreq =[]
for k in range(0,len(t)):
    myfreq.append(2*np.pi/dt/N*k)

freq = np.fft.fftfreq(t.shape[-1])
freq *= 2*np.pi

plt.figure()
plt.plot(freq, sp.real, freq, sp.imag)
plt.show()

plt.figure()
plt.plot(myfreq, sp.real, label="Re")
plt.plot(myfreq, sp.imag, label="Im")
plt.legend()
plt.show()