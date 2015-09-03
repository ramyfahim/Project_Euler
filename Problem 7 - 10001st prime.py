# -*- coding: utf-8 -*-
"""
Created on Tue May 19 08:59:48 2015

@author: Ramy
"""

import math

run = True

count = 0

check = 2

while run:
    isPrime = True
    for i in range(2, int(math.sqrt(check)) + 1):
        if (check % i == 0):
            isPrime = False
            break
    if isPrime:
        count += 1
    if count == 10001:
        prime = check
        run = False
    check += 1

print (prime)
