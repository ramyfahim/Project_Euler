# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:11:06 2015

@author: Ramy
"""

num1 = 1
num2 = 1

term = 0

sum = 0

while (num1 + num2) < 4000000:
    term = num1 + num2
    if term % 2 == 0:
        sum += term
    num1 = num2
    num2 = term

print sum


# slightly different way

num_1 = 1
num_2 = 1

termA = num_1 + num_2

sumA = 0

while termA < 4000000:
    if termA % 2 == 0:
        sumA += termA
    
    num_1 = num_2
    num_2 = termA
    termA = num_1 + num_2

print sumA