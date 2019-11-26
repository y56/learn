#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:20:46 2019

@author: Yu-Jen (Eugene) Wang, yjwang.y56@gmail.com
"""


import sys


def binarysearch(sortedlist, target):

    global i
    i = 0

    def binarysearchhelper(sortedlist, target, low, high):

        global i
        print('\ni =', i, '\n')
        i += 1

        if low > high:
            return -1

        mid = (low + high) // 2

        print('sortedlist =', sortedlist)
        print("addr is", hex(id(sortedlist)), "sizs is",
              sys.getsizeof(sortedlist))

        print('target =', target)
        print("addr is", hex(id(target)), "sizs is", sys.getsizeof(target))

        print('low =', low)
        print("addr is", hex(id(low)), "sizs is", sys.getsizeof(low))

        print('high =', high)
        print("addr is", hex(id(high)), "sizs is", sys.getsizeof(high))

        print('mid =', mid)
        print("addr is", hex(id(mid)), "sizs is", sys.getsizeof(mid))

        if (target == sortedlist[mid]):
            return mid

        if (target > sortedlist[mid]):
            return binarysearchhelper(sortedlist, target, (mid + 1), high)
        else:
            return binarysearchhelper(sortedlist, target, low, (mid - 1))

    return binarysearchhelper(sortedlist, target, 0, len(sortedlist) - 1)


if __name__ == '__main__':

    sortedlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    result = binarysearch(sortedlist, 1)
    print("\ntarget index is", result)
