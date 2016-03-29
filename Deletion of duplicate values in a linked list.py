# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 12:17:14 2016

@author: Aditya
"""

#Deletion of duplicate values in a linked list

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        self.head = head
        if head == None or head.next == None:
            return head
        a = head
        while(a !=None and a.next !=None):
            if a.val == a.next.val :
                a.next = a.next.next
            else:
                a = a.next
        return head