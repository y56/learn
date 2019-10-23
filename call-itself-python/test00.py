#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 22:54:00 2019

@author: y56
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 1
        return self.climbStairs(n-1)+self.climbStairs(n-2)

def main():
    for i in range(10):
        ret = Solution().climbStairs(i)
        print(ret)

if __name__ == '__main__':
    main()