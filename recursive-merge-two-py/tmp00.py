#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:07:08 2019

@author: y56
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def f(cur, l1, l2):
            if l1 != None and l2 != None:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
                f(cur, l1, l2)
            
        hd = ListNode(-1)
        cur= hd  # dummy head
        f(cur, l1, l2)
        
        
        if l1 == None:
            print("no l1",l2)
            cur.next = l2
        if l2 == None:
            cur.next = l1
            print("no l2",l1)
            
        return hd.next