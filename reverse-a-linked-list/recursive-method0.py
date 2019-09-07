#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 20:17:30 2019

@author: y56
"""
class Node:
    def __init__(self, x):
        self.data = x
        self.next  =  None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, x):
        newNode = Node(x)
        newNode.next = self.head
        self.head = newNode
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data,  "-> " , end = '')
            curr = curr.next
        print("null")
    def reverse(self, node):
    
        # the condition to stiop the recurrence 
        if node == None or node.next == None: 
            # node == None is for empty l-lists
            # node.next == None is for non-empty l-lists, 
            # it is the point of bouncing-back, bottum of recurrence
            return node
        
        headOfRest = self.reverse(node.next)

        node.next.next = node    
        node.next = None
      
        return headOfRest
            
myLinkedList = LinkedList()
myLinkedList.push(4)
myLinkedList.push(3)
myLinkedList.push(2)
myLinkedList.push(1)

myLinkedList.printList()
myLinkedList.head = myLinkedList.reverse(myLinkedList.head)
myLinkedList.printList()
