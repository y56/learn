#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 03:36:56 2020

given a landscape and a tetris piece, find the max score we can have

@author: y56
"""

import copy


def TetrisMove(strArr):

    def landscape_print(gameboard):  # print to check
        p = copy.deepcopy(gameboard)
        for i, r in enumerate(p):
            for j, x in enumerate(r):
                if x:
                    p[i][j] = "■"
                else:
                    p[i][j] = "□"
        for x in p[::-1]:
            print(x)
        print('==')

    def tetris_print(piece, leftup_corner_r, leftup_corner_c):  # print to check
        p = copy.deepcopy(gameboard)
        for i, r in enumerate(piece):
            for j, x in enumerate(r):
                if x == 1:
                    p[leftup_corner_r+i][leftup_corner_c+j] = 2
        for i, r in enumerate(p):
            for j, x in enumerate(r):
                if x == 1:
                    p[i][j] = "■"
                elif x == 0:
                    p[i][j] = "□"
                elif x == 2:
                    p[i][j] = "★"
        for x in p[::-1]:
            print(x)
        print('==')

    def score(piece, leftup_corner_r, leftup_corner_c):
        filled_gameboard_ = copy.deepcopy(gameboard)
        for r, _row in enumerate(piece):
            for c, x in enumerate(_row):
                if x == 1:
                    filled_gameboard_[leftup_corner_r +
                                      r][leftup_corner_c + c] = 1
        return sum(all(_row) for _row in filled_gameboard_)

    def is_at_buttom(piece, leftup_corner_r, leftup_corner_c):
        for c in range(0, len(piece[0])):
            for r in range(len(piece) - 1, -1, -1):
                if piece[r][c] == 1:
                    if (leftup_corner_r == r ==
                            0) or gameboard[leftup_corner_r + r - 1][leftup_corner_c + c] == 1:
                        return True
        return False

    def overlapped(piece, leftup_corner_r, leftup_corner_c):
        for r in range(len(piece)):
            for c in range(len(piece[0])):
                if gameboard[leftup_corner_r +
                             r][leftup_corner_c +
                                c] == 1 and piece[r][c] == 1:
                    return True
        return False

    def rotate(piece):
        h = len(piece)
        w = len(piece[0])
        res = [[0] * h for _ in range(w)]
        for r in range(w):
            for c in range(h):
                res[r][c] = piece[c][w - 1 - r]
        return res

    gameboard_w = 12
    gameboard_h = 10
    shape_dict = {  # NOTE!! 0th row is at buttom
        'I': [[1, 1, 1, 1]],
        'L': [[1, 1, 1], [0, 0, 1]],
        'J': [[1, 1, 1], [1, 0, 0]],
        'O': [[1, 1], [1, 1]],
        'Z': [[0, 1, 1], [1, 1, 0]],
        'T': [[1, 1, 1], [0, 1, 0]],
        'S': [[1, 1, 0], [0, 1, 1]]}
    piece = shape_dict[strArr[0]]

    gameboard = [[0] * gameboard_w for _ in range(gameboard_h)]
    for c, x in enumerate(strArr[1::]):
        for int_x in range(int(x)):
            gameboard[int_x][c] += 1

    piece_li = [piece]
    for _ in range(3):
        piece = rotate(piece)
        piece_li.append(piece)

    ans = 0
    optimals = []

    for piece in piece_li:
        ph = len(piece)
        pw = len(piece[0])

        for leftup_corner_r in range(0, gameboard_h - ph + 1):
            for leftup_corner_c in range(0, gameboard_w - pw + 1):
                if not overlapped(piece, leftup_corner_r, leftup_corner_c) \
                        and is_at_buttom(piece, leftup_corner_r, leftup_corner_c):

                    this_score = score(piece, leftup_corner_r, leftup_corner_c)
                    if this_score > ans:
                        optimals = [(piece, leftup_corner_r, leftup_corner_c)]
                    elif this_score == ans:
                        optimals.append(
                            (piece, leftup_corner_r, leftup_corner_c))
                    ans = max(ans, this_score)
    for x in optimals:
        tetris_print(*x)
    landscape_print(gameboard)

    return ans


print(TetrisMove(["L", "2", "4", "3", "4", "5",
                  "2", "0", "2", "2", "3", "3", "3"]))  # 2
print(TetrisMove(["O", "4", "3", "2", "3", "5",
                  "1", "0", "1", "2", "4", "3", "4"]))  # 0
print(TetrisMove((['L', '3', '4', '4', '5', '6',
                   '3', '0', '6', '5', '3', '6', '6'])))  # 2
print(TetrisMove(['I', '5', '5', '5', '5', '5',
                  '5', '0', '7', '6', '7', '6', '7']))  # 4
