# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 20:37:40 2016

@author: Aditya
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        result = 0
        for char in s:
            result = result*26 +(ord(char) - ord('A') + 1)
        return result
        