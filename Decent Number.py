# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 00:53:38 2016

@author: Aditya
"""
#Largest number decent number
#A Decent Number has the following properties:
#Its digits can only be 3's and/or 5's.
#The number of 3's it contains is divisible by 5.
#The number of 5's it contains is divisible by 3.
#If there are more than one such number, we pick the largest one.

t = int(input().strip())
for a in range(t):
    n = int(input().strip())
    z = n
    while(z%3!=0):
        z -=5 
    if(z<0):
        print ('-1') 
    else: 
        print (z*'5'+(n-z)*'3')