#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 23:03:21 2020

@author: y56
"""
import random
import itertools


def bruteforce(li):
    n = len(li)

    # by exhaustion, list all 2^(n-1)
    # n numbers, n-1 break point
    # each point, to cut or not to cut
    split_methods = list(
        reversed([format(x, '#0' + str(n + 1) + 'b')[2:] for x in range(2**(n - 1))]))

#    print(split_methods)

    for split_method in split_methods:
        splitted = []
        start = 0
        for i, x in enumerate(split_method):
            if x == '1':
                splitted.append(li[start:i + 1])  # start~i
                start = i + 1

        if start != len(li):
            splitted.append(li[start:])

#        print(split_method)
#        print(splitted)

        # to join a list of lists into one list
        # https://stackoverflow.com/questions/716477/join-list-of-lists-in-python
        cand = list(itertools.chain.from_iterable(map(sorted, splitted)))

        if sorted(li) == cand:
            return len(splitted)


def soln1(li):
    sorted_li = sorted(li)
    cur_max = 0  # since all nums in li>=0, safe
    ans = 0
    for x, y in zip(li, sorted_li):
        cur_max = max(cur_max, x)
        if cur_max == y:
            ans += 1
    return ans


for _ in range(10):
    L = random.randint(1, 20)
    test = []
    while len(test) < L:
        n = random.randint(1, 1000)
        if n not in test:
            test.append(n)
#    print(test)
    if soln1(test) != bruteforce(test):
        print(test)
#    print(soln1(test))
#    print(bruteforce(test))


print(bruteforce([2, 1, 6, 4, 3, 7]))
print(soln1([2, 1, 6, 4, 3, 7]))
# 3
print(bruteforce([4, 3, 2, 6, 1]))
print(soln1([4, 3, 2, 6, 1]))
# 1
print(bruteforce([2, 4, 1, 6, 5, 9, 7]))
print(soln1([2, 4, 1, 6, 5, 9, 7]))
# 3
