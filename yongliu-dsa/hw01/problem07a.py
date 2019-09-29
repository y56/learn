#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:36:45 2019

@author: y56
"""
from math import log2 as lg2
from math import log as log
from math import sqrt as sqrt

r = 2/(3**0.5)

def S_sum(k):
    sum = 0
    r = 2/(3**0.5)
    for i in range(0, int(k)+1):
        sum += r**i * i
    return sum

def S_formula(k):
    print(S_sum(k)-(
            (r+r**(k+1)*k-r**(k+1)-k*r**k)/(1-r)**2
            ))
    return (r+r**(k+1)*k-r**(k+1)-k*r**k)/(1-r)**2
    

    # sqrt
print("--------")

def T(n):
    if n == 1:
        return 1
    return 2*T(n/3) + n**0.5 * lg2(n)
def T_formula(n):
    return n**(log(2,3)) + 1/sqrt(3)*sqrt(n)/(r-1)*(n**(log(r,3))-1)*lg2(n)-sqrt(n)/sqrt(3)/(1-r)**2*(
            r+r**(log(n,3)+1)*log(n,3)-r**(log(n,3)+1)-log(n,3)*r**log(n,3)
            )*log(3,2)
def T_formula_orig(n):
    k = log(n, 3)
    return 2**k \
    + \
    sqrt(n)/sqrt(3)*(
            (r**k-1)/(r-1)*lg2(n) ) \
    - \
    sqrt(n)/sqrt(3) * S_sum(k-1) * lg2(3)

def T_formula_orig_orig(n):
    k = log(n, 3)
    return 2**k + sqrt(n)/sqrt(3)*(
            (r**k-1)/(r-1)*lg2(n) ) - sqrt(n)/sqrt(3) * S_sum(k-1) * lg2(3)
def T_new(n):
    a = log(2,3)
    return n**a + lg2(3)*sqrt(3) / (sqrt(3)-1) * (
            sqrt(n)*log(n,3)-1)


print("--------")
                                                                                                                                                                                                                                                                                                                                                                           
for i in range(0,11):
    print(T(3**i) - T_new(3**i))
 