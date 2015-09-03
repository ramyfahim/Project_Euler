# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:39:42 2015

@author: Ramy
"""


sum = 0
sumOfSquares = 0

for i in range(1,101):
    sum += i
    sumOfSquares += i*i

squareOfSum = sum*sum

print squareOfSum - sumOfSquares