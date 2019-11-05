#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:48:52 2019

@author: y56
"""

def maxScorePath(grid):
    if not grid:
        return 0
    if len(grid) == 1 and len(grid[0]) == 2:
        return 0
    if len(grid) == 2 and len(grid[0]) == 1:
        return 0
    
    for j in range(2, len(grid[0])):
        if j == len(grid[0]) - 1:
            if len(grid) == 1:
                grid[0][j] = grid[0][j-1]
            else:
                grid[0][j] = min(grid[0][j-1],grid[0][j])
        else:
            grid[0][j] = min(grid[0][j-1],grid[0][j])
    
    for i in range(2, len(grid)):
        if i == len(grid) - 1:
            if len(grid[0]) == 1:
                grid[i][0] = grid[i-1][0]
            else:
                grid[i][0] = min(grid[i-1][0],grid[i][0])
        else:
            grid[i][0] = min(grid[i-1][0],grid[i][0])
    
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            if i == len(grid)-1 and j == len(grid[0])-1:
                grid[i][j] = max(grid[i-1][j],grid[i][j-1])
            else:
                grid[i][j] = max(min(grid[i-1][j],grid[i][j]),min(grid[i][j-1],grid[i][j]))
                
    return grid[len(grid)-1][len(grid[0])-1]

grid1 =    [ [5, 1], 
             [4, 5] ]

grid2 =    [ [5, 1, 7], 
             [4, 8, 5] ]

grid3 =    [ [1, 9, 9], 
             [9, 9, 9], 
             [9, 9, 9] ]

grid4 =    [ [10, 7, 3], 
             [12, 11, 9], 
             [1, 2, 8] ]

grid5 =    [ [20, 20, 3], 
             [20, 3, 20], 
             [3, 20, 20] ]

grid6 =    [ [1, 2, 3], 
             [4, 5, 1]]

print(maxScorePath(grid1))
print(maxScorePath(grid2))
print(maxScorePath(grid3))
print(maxScorePath(grid4))
print(maxScorePath(grid5))
print(maxScorePath(grid6))