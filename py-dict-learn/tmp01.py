#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 03:51:58 2019

@author: y56
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        s = '' # not []
        r1dict = {1:'I',10:'X',100:'D',1000:'M',10000:'only-to-prevent-KeyError'}
        r5dict = {1:'V',10:'L',100:'M',1000:'only-for-consistency'}
        for d in [1000,100,10,1]: # d is for decimal base
            r1 = r1dict[d]  # roman digit for 1*d
            r5 = r5dict[d]  # roman digit for 5*d
            r10 = r1dict[d*10]
            myDict = {0:'',1:r1, 2:r1*2,3:r1*3, 4:r1+r5, 5:r5,6:r5+r1, 7:r5+r1*2, 8:r5+r1*3, 9:r1+r10}
            x = num//d
            num = num - x * d
            s += myDict[x]  # not s.append(myDict[x])
        return s


       
