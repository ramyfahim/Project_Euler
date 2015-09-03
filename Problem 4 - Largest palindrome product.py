# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:06:42 2015

@author: Ramy
"""


largestpalindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        numstr = str(i*j)
        if numstr == numstr[::-1]:
            if i*j > largestpalindrome:
                largestpalindrome = i*j


print largestpalindrome