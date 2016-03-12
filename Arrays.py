# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 12:36:17 2016

@author: Aditya
"""
#Array Trasposition
import numpy as np
arr1 = np.arange(50).reshape((5,10))
print(arr1)
arr2 = arr1.T
np.dot(arr1,arr2)
np.dot(arr2,arr1)

arr3 = np.arange(50).reshape(2,5,5)
print(arr3)
arr4 = arr3.T
print(arr4)

#Matplotlib
import numpy as np
import matplotlib.pyplot as mp
points = np.arange(-5,5,0.01)
dx,dy = np.meshgrid(points,points)
dx
z = (np.sin(dx)+np.sin(dy))
z
mp.imshow(z)
mp.colorbar()
mp.title("Plot for z")
##
A = np.array([1,2,3,4])

B= np.array([100,200,300,400])

#Now a boolean array
condition = np.array([True,True,False,False])

#Using a list comprehension
answer = [(A_val if cond else B_val) for A_val,B_val,cond in zip(A,B,condition)]

#Show the answer
answer

#Problems include speed issues and multi-dimensional array issues
import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr.sum(1)

#Pandas 
import pandas as pd
a = pd.Series([3,6,9,12])
print(a)
a.values
a.index

import webbrowser
website = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'
webbrowser.open(website)
nfl_frame = pd.read_clipboard()
nfl_frame

from numpy.random import randn
dframe = pd.DataFrame(randn(25).reshape((5,5)),index=['A','B','D','E','F'],columns=['col1','col2','col3','col4','col5'])
dframe2 = dframe.reindex(["A", "B","C","D","E","F"])
dframe2
new_columns = ["col1","col2","col3","col4","col5","col6"]
dframe2.reindex(columns=new_columns)
dframe2
dframe2.ix[['A','B','C','D','E','F'],new_columns]