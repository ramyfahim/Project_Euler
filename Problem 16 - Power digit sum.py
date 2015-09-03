# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:37:03 2015

@author: Ramy
"""


number = str(2**1000)

length = len(number)

sum = 0

for i in range(length):
    sum += int(number[i])

print sum