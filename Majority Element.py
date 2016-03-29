# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 18:12:54 2016

@author: Aditya
"""

def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        if(len(nums) == 1):
            return nums[0]
        nums.sort()
        return nums[len(nums)/2]
        
##Linear Time Majority Vote Alogirthm        
        
def majorityElement1(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 0
        i = 0
        while(i < len(nums)):
            if (a == 0):
                b = nums[i]
                a = 1;
            elif( b == nums[i]):
                a+= 1
            else:
                a-= 1
            i+=1
        return b
            