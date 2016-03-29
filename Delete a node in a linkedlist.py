# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 15:17:47 2016

@author: Aditya
"""

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        self.node = node
        node.val = node.next.val
        node.next = node.next.next