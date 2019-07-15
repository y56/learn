#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 06:17:25 2019

@author: y56

ref = https://hackmd.io/rdTVGkmxSzyTGV9j05qZvw?both

My small De Bruijn Test of 130329821:

0x07C4ACDD
00000111110001001010110011011101B
bit 31 - bit 27   00000  0
bit 30 - bit 26   00001  1
bit 29 - bit 25   00011  3
bit 28 - bit 24   00111  7
bit 27 - bit 23   01111 15
bit 26 - bit 22   11111 31
bit 25 - bit 21   11110 30
bit 24 - bit 20   11100 28
bit 23 - bit 19   11000 24
bit 22 - bit 18   10001 17
bit 21 - bit 17   00010  2
bit 20 - bit 16   00100  4
bit 19 - bit 15   01001  9
bit 18 - bit 14   10010 18
bit 17 - bit 13   00101  5
bit 16 - bit 12   01010 10
bit 15 - bit 11   10101 21
bit 14 - bit 10   01011 11
bit 13 - bit  9   10110 22
bit 12 - bit  8   01100 12
bit 11 - bit  7   11001 25
bit 10 - bit  6   10011 19
bit  9 - bit  5   00110  6
bit  8 - bit  4   01101 13
bit  7 - bit  3   11011 27
bit  6 - bit  2   10111 23
bit  5 - bit  1   01110 14
bit  4 - bit  0   11101 29
bit  3 - bit 31   11010 26
bit  2 - bit 30   10100 20
bit  1 - bit 29   01000  8
bit  0 - bit 28   10000 16
                  
0x07C4ACDD is 5bit de Bruin Sequence
"""


anti_hash_table = [0,1,3,7,15,31,30,28,24,17,2,4,9,18,5,10,
              21,11,22,12,25,19,6,13,27,23,14,29,26,20,8,16]

# Formally, I shall build a hash table 
# but I am lazy so I use an anti hash table.
# And use `list.index(element_value)`

for x in range(32):
    hash_key = ((0x7c4acdd * (2 ** x)) >> 27) % 32
    print(anti_hash_table.index(hash_key))