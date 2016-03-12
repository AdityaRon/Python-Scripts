# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 01:33:02 2016

@author: Aditya
"""

def diagonal_difference(matrix):
    l = sum(matrix[i][i] for i in range(N))
    r = sum(matrix[i][N-i-1] for i in range(N))
    return abs(l - r)

matrix = []
N = input()
for _ in range(N):
    matrix.append(map(int, raw_input().split()))

print diagonal_difference(matrix)