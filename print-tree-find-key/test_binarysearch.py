#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:06:03 2019

Unit test of binarysearch.binarysearch()

@author: Yu-Jen (Eugene) Wang, yjwang.y56@gmail.com
"""


import binarysearch
import unittest


class TestBinarySearch(unittest.TestCase):

    def test_int_hit(self):

        sortedlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 1

        testResult = binarysearch.binarysearch(sortedlist, target)
        correctAnswer = 0

        self.assertEqual(testResult, correctAnswer)

    def test_char_miss(self):

        sortedlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        target = 'a'

        testResult = binarysearch.binarysearch(sortedlist, target)
        correctAnswer = -1

        self.assertEqual(testResult, correctAnswer)

    def test_empty_list(self):

        sortedlist = []
        target = 0

        testResult = binarysearch.binarysearch(sortedlist, target)
        correctAnswer = -1

        self.assertEqual(testResult, correctAnswer)

    def test_not_list(self):

        sortedlist = 1
        target = 1

        with self.assertRaises(TypeError):
            binarysearch.binarysearch(sortedlist, target)

    def test_mismatched_type(self):

        sortedlist = [1, 2, 3, 4, 5, 6, 7, '8', 9]
        target = 9

        with self.assertRaises(TypeError):
            binarysearch.binarysearch(sortedlist, target)

    def test_none_input(self):

        sortedlist = None
        target = 0

        with self.assertRaises(TypeError):
            binarysearch.binarysearch(sortedlist, target)

    def test_none_target(self):

        sortedlist = ['a', 'b', 'c']
        target = None

        with self.assertRaises(TypeError):
            binarysearch.binarysearch(sortedlist, target)


if __name__ == "__main__":
    unittest.main()
