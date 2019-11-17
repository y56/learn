#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:16:13 2019
AVL tree
@author: y56
"""
class treeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0
        
    def insert(self, root, val):
        if root is None:
            root = treeNode(val)
        elif val < root.val:
            self.insert(root.left, val)
        else:
            self.insert(root.right)
            
myTree = None
treeNode.insert(myTree, 1)

        
        
