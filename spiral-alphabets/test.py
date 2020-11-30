"""
see test.png
"""

N = 39  # len of edge of squre
ct = 0
head = []  # from left-up corner to center
tail = []  # from right-buttom corner to center
while N > 1:
    head.append(ct % 26)  # alphabet cycle in 26
    tail.append((ct + 2 * N - 2) % 26)
    ct += 4 * N - 4  # go thru all box of this layer
    N -= 2  # go to next layer

if N == 1:  # the very center if original N is odd
    head.append((ct + 1) % 26)
    for x in head + tail[::-1]:
        print(chr(ord('A') + x), end='')
