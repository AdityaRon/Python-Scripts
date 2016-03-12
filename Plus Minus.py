# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 01:39:37 2016

@author: Aditya
"""

import sys

n = int(input().strip())
arr = map(int,input().strip().split(' '))
mylist = [float(i) for i in arr]

zero = sum(j == 0 for j in mylist)
ng = sum(j < 0 for j in mylist)
ps = sum(j > 0 for j in mylist)
print (round(float(ps)/len(arr), 3))
print (round(float(ng)/len(arr), 3))
print (round(float(zero)/len(arr), 3))