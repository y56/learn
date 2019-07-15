#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 07:11:08 2019

@author: y56

ref = https://hackmd.io/rdTVGkmxSzyTGV9j05qZvw?both

0x077CB531U

00000111011111001011010100110001
l-shamnt  binary  decimal
0         00000         0
1         00001         1
2         00011         3
3         00111         7
4         01110        14
5         11101        29
6         11011        27
7         10111        23
8         01111        15
9         11111        31
10        11110        30
11        11100        28
12        11001        25
13        10010        18
14        00101         5
15        01011        11
16        10110        22
17        01101        13
18        11010        26
19        10101        21
20        01010        10
21        10100        20
22        01001         9
23        10011        19
24        00110         6
25        01100        12
26        11000        24
27        10001        17
28        00010         2
29        00100         4
30        01000         8
31        10000        16

"""
anti_hash_table = [0,1,3,7,14,29,27,23,15,31,30,28,25,18,5,11,22,13,26,
                   21,10,20,9,19,6,12,24,17,2,4,8,16]

# Formally, I shall build a hash table 
# but I am lazy so I use an anti hash table.
# And use `list.index(element_value)`

for x in range(32):
    hash_key = ((0x077CB531 * (2 ** x)) >> 27) % 32
    print(anti_hash_table.index(hash_key))

hash_table = []
for i in range(32):
    hash_table.append(anti_hash_table.index(i))
    
for x in range(32):
    hash_key = ((0x077CB531 * (2 ** x)) >> 27) % 32
    print(hash_table[hash_key])
