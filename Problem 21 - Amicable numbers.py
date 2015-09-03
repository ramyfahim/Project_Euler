# -*- coding: utf-8 -*-
"""
Created on Sat May 30 09:34:40 2015

@author: Ramy
"""

import math

def listsum(List):
    sum = 0
    for i in List:
        sum += i
    return sum

amicableNum = []

amicableSum = 0

for a in range(2, 10000):
    new = True
    for check in amicableNum:
        if a == check:
            new = False
    if not new:
        continue
    
    aDiv = []
    for i in range(1, int(math.sqrt(a)) + 1):
        if a % i == 0:
            aDiv.append(i)
            if i == math.sqrt(a) or i == 1:
                continue
            aDiv.append(a/i)
    b = listsum(aDiv)
    bDiv = []
    for j in range(1, int(math.sqrt(b)) + 1):
        if b % j == 0:
            bDiv.append(j)
            if j == math.sqrt(a) or j == 1:
                continue
            bDiv.append(b/j)
            
    if listsum(bDiv) == a and a != b:
        amicableNum.append(a)
        amicableSum += a
        if b < 10000:
            amicableNum.append(b)
            amicableSum += b

print (amicableSum)