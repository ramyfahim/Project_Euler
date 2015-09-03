# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:59:13 2015

@author: Ramy
"""


sum = 0

for i in range(1,1000):
    if i % 3 == 0:
        sum += i
    elif i % 5 == 0:
        sum += i

print sum


# another way

sumA = 0

for j in range(1,1000):
    if (j % 3 == 0 or j % 5 == 0):
        sumA += j

print sumA