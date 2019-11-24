#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 21:04:15 2019

# binary tree

## print in level order: root to leaf, left to right

## TODO:
- create test cases
- complete functions
- time/space analysis

@author: y56
"""


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def printtree(root):

    print("\nStart printing >>>")
    result = []

    if root is None:
        print(">>> Finish printing")
        return result

    fifoQueue = []
    fifoQueue.append(root)
    
    
    while len(fifoQueue) > 0:

        print(fifoQueue[0].data)
        result.append(fifoQueue[0].data)
        currentNode = fifoQueue.pop(0)

        if currentNode.left is not None:
            fifoQueue.append(currentNode.left)

        if currentNode.right is not None:
            fifoQueue.append(currentNode.right)
    
    print(">>> Finish printing")
    return result


if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    result = printtree(root)
