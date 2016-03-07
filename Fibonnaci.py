# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 09:15:57 2016

@author: Aditya
"""
#Fibanocci series
a = 0
b = 1
i = 0
c = 0
while(c<100):
    if a == 0:
        print (a)
        print (b)
    c = a + b
    print (c)
    a = b
    b = c
    i = i + 1

#Fibanocci seriers
a= 0
b= 1
i = 0
while(i < 10):
    if a == 0:
        print (a)
        print (b)
    a,b = b, a+b
    print (b)
    i = i+1

#Palindrome
a = "Madam"
a = a.lower()
if a[::-1] == a :
    print (a, "is a palindrome" )
else:
    print(a, "is not a palindrome")

#Set
a = "AdityaAditya"
a = a.lower()
set(a)

#Dictionaries
Pairs = {}
Pairs["Puttapa"] = "Gamya"
Pairs["Puttapa1"] = "Divya"
Pairs["Aditya"] = "Sravani"
Pairs["Ganapriya"] = "Manas"
Pairs["Sukirti"] = "Vikas"

#List
a = [100,229,313,11,2312,44,55,6]
a.sort()
print (a)

#Bitwise operations
a = 4
b = 2
a & b
#' '.join(a) - Used to convert list to a string.
#reversed
print ("Hello!")
for i in reversed(range(1,11)):
      if i%2 == 0:
        print (i)
