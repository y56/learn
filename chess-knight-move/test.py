#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 23:03:13 2020

square chess board N*N

have to move exactly 20 times

find all possible ending postions

start_i,start_j=0,0

@author: y56
"""
N=50
tot_moves = 20
start_i=0
start_j=0
def moves(i,j):
    a=[(i+ii,j+jj) 
       for iii,jjj in [(1,-1),(-1,1),(-1,-1),(1,1)]
       for ii,jj in [(1*iii,2*jjj),(2*iii,1*jjj)]
       if 0<=i+ii<N and 0<=j+jj<N]
    return a

board=[[0]*N for _ in range(N)]
board[start_i][start_j]=1
    
for _ in range(tot_moves):
    tmp_board=[[0]*N for _ in range(N)]
    for i,r in enumerate(board):
        for j,x in enumerate(r):
            if x:
                for ii,jj in moves(i,j):
                    tmp_board[ii][jj]=1
    board=tmp_board
    
print(sum(map(sum,board)))