#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 03:53:38 2019

@author: y56
"""

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def printList(self):
        ptr = self
        while ptr:
            print(ptr.data)
            ptr = ptr.next
            
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, data):
        newNode = ListNode(data)
        newNode.next = self.head
        self.head = newNode
    def printList(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
            
def mergeTwo(l1: ListNode, l2:ListNode) -> ListNode:
    dummyHead = ListNode(-1)  # dummy head
    tail = dummyHead
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            tail = tail.next
            l1 = l1.next
        else:
            tail.next = l2
            tail = tail.next
            l2 = l2.next
    if l1:
        tail.next = l1
    else:
        tail.next = l2
    return dummyHead.next

def mergeMany(listOfListNode):
    tempNode = None
    while listOfListNode:
        tempNode = mergeTwo(listOfListNode[-1], tempNode)
        listOfListNode.pop()
    return tempNode
def mergeMany_revision(listOfListNode):
    while len(listOfListNode) > 1:
        n = len(listOfListNode) // 2
        for i in range(0, n):
            listOfListNode[2 * i] = mergeTwo(listOfListNode[2 * i], 
                                             listOfListNode[2 * i + 1])
            listOfListNode.pop(2 * i + 1)
    return listOfListNode

myLinkedList1 = LinkedList()
myLinkedList1.append(5)
myLinkedList1.append(4)
myLinkedList1.append(1)
myLinkedList1.printList()
print("--")

myLinkedList2 = LinkedList()
myLinkedList2.append(6)
myLinkedList2.append(2)
myLinkedList2.printList()
print("--")

myLinkedList3 = LinkedList()
myLinkedList3.append(4)
myLinkedList3.append(3)
myLinkedList3.append(1)
myLinkedList3.printList()
print("--")

mergeResult = mergeMany(
        [myLinkedList1.head, myLinkedList2.head, myLinkedList3.head])

mergeResult.printList()
print("--")
myLinkedList1.printList()
print("--")
myLinkedList2.printList()
print("--")
myLinkedList3.printList()

# 
print("========")

myLinkedList1 = LinkedList()
myLinkedList1.append(5)
myLinkedList1.append(4)
myLinkedList1.append(1)
myLinkedList1.printList()
print("--")

myLinkedList2 = LinkedList()
myLinkedList2.append(6)
myLinkedList2.append(2)
myLinkedList2.printList()
print("--")

myLinkedList3 = LinkedList()
myLinkedList3.append(4)
myLinkedList3.append(3)
myLinkedList3.append(1)
myLinkedList3.printList()
print("--")
mergeResult = mergeMany_revision(
        [myLinkedList1.head, myLinkedList2.head, myLinkedList3.head])

mergeResult[0].printList()
print("--")
myLinkedList1.printList()
print("--")
myLinkedList2.printList()
print("--")
myLinkedList3.printList()