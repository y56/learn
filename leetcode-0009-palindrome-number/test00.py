#!/usr/bin/python3

import sys

x = int(sys.argv[1])

y = 0

while x > y:
    y = y * 10 + x % 10
    x = x // 10
    print(x)
    print(y)
    print("--")
