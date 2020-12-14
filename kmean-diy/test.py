#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 23:34:55 2020

@author: y56
"""
from collections import *
#from itertools import *
from math import *
#from string import *
import random
import numpy as np

def rand_into_k_groups(n,k): # into k group
    # 0 ~ n-1
    li = list(range(n))
    ans=[[] for _ in range(k)]
    while li:
        for kk in range(k):
            if not li:
                return ans
            tmp=random.choice(li)
            ans[kk].append(tmp)
            li.remove(tmp)
    return ans

def dis(center,i,m): # d dim
    vector=m[i]
    ans=0
    for i,j in zip(center,vector):
        ans+=(i-j)**2
    return ans

def nearest_center_in(centers,i,m):
    ans=None
    curmindis=inf
    for ind_center, center in enumerate(centers):
        curdis=dis(center,i,m)
        if curdis < curmindis:
            curmindis=curdis
            ans=ind_center
    return ans
def ave(ind_li,m):
    ans=[0]*len(m[0])
    for i in ind_li:
        for d in range(len(m[0])):
            ans[d]+=m[i][d]
    for i,_ in enumerate(ans):
        ans[i]/=len(ind_li)
    return ans
def kmean(m,k): # m = n by d
    n=len(m)
    d=len(m[0])
    
    centers=[ave(ind_li,m) for ind_li in rand_into_k_groups(n,k)]
    center_for_pt=[-1]*n
    pt_belong_to_center=defaultdict(list)        
    
    ct=0
    while ct<100:
        
        pt_belong_to_center.clear()
        
        for i in range(n): # new center for each pt
            center_ind_for_i = nearest_center_in(centers,i,m)
            center_for_pt[i]=center_ind_for_i
            pt_belong_to_center[center_ind_for_i].append(i)
            
        # update `center`
        for _i,pt_li in enumerate(pt_belong_to_center.values()):
            new_center=ave(pt_li,m)
            centers[_i]=new_center
        
        ct+=1
        
    return pt_belong_to_center,centers
        
m=[]
for _ in range(100):
    tmp=[]
    for _ in range(2):
        tmp.append(random.randint(0,100))
    m.append(tmp)

pt_belong_to_center,centers=kmean(m,4)

import matplotlib.pyplot as plt

for x in m:
    plt.plot(x[0],x[1],'bo')
ss=['r','g','b','k']
for i,x in enumerate(pt_belong_to_center.values()):
    s=ss[i]
    for xx in x:
        plt.plot(m[xx][0],m[xx][1],s+'o')
for c in centers:
    plt.plot(c[0],c[1],'m*',markersize=15)