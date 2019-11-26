#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:30:13 2019

Unit test of binarytree.printtree()

@author: Yu-Jen (Eugene) Wang, yjwang.y56@gmail.com
"""


import binarytree
import unittest


class TestPrintTree(unittest.TestCase):

    def test_unbalaced_tree(self):

        root = binarytree.TreeNode(1)
        root.left = binarytree.TreeNode(2)
        root.right = binarytree.TreeNode(3)
        root.left.left = binarytree.TreeNode(4)
        root.left.right = binarytree.TreeNode(5)

        testResult = binarytree.printtree(root)
        correctAnswer = [1, 2, 3, 4, 5]

        self.assertEqual(testResult, correctAnswer)

    def test_linear_tree(self):

        root = binarytree.TreeNode(10)
        root.left = binarytree.TreeNode(20)
        root.left.left = binarytree.TreeNode(30)
        root.left.left.left = binarytree.TreeNode(40)

        testResult = binarytree.printtree(root)
        correctAnswer = [10, 20, 30, 40]

        self.assertEqual(testResult, correctAnswer)

    def test_empty_treenode(self):

        root = binarytree.TreeNode(None)
        root.left = binarytree.TreeNode(2)
        root.right = binarytree.TreeNode(3)
        root.left.left = binarytree.TreeNode(None)
        root.left.right = binarytree.TreeNode(5)

        testResult = binarytree.printtree(root)
        correctAnswer = [None, 2, 3, None, 5]

        self.assertEqual(testResult, correctAnswer)

    def test_empty_tree(self):

        root = None

        testResult = binarytree.printtree(root)
        correctAnswer = []

        self.assertEqual(testResult, correctAnswer)

    def test_not_treenode(self):

        root = 1

        with self.assertRaises(AttributeError):
            binarytree.printtree(root)


if __name__ == "__main__":
    unittest.main()
