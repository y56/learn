#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 23:52:00 2019

@author: y56
"""

class Node(object):
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,data): #this method adds node at head
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def traverse(self):
        current = self.head
        while current:
            if current.next:
                print(current.data,end="->")
            else:
                print(current.data)
            current = current.next

    def reverse(self,item):
        if item.next == None:
            self.head = item
            return
        self.reverse(item.next)
        temp = item.next
        temp.next = item
        item.next = None


def main():
    mylist = LinkedList()
    mylist.add(15)
    mylist.add(20)
    mylist.add(25)
    mylist.add(30)
    mylist.traverse()
    mylist.reverse(mylist.head)
    mylist.traverse()
    print(mylist.head.data)

if __name__ == "__main__":
    main()