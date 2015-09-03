# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:36:22 2015

@author: Ramy
"""

import math

num = 600851475143

largestPrimeFactor = 1


for i in range(2, int(math.sqrt(num))): #all factors below square root of number have a corresponding factor above it, and vice versa, so only check below
    if num % i == 0:
        check1 = i
        check2 = num/i
    else:
        continue
    
    check1_is_prime = True
    j = 2
    while j <= (check1)/2:
        if check1 % j == 0:
            check1_is_prime = False
            break
        j += 1
    if check1_is_prime and check1 > largestPrimeFactor:
        largestPrimeFactor = check1
    
    check2_is_prime = True
    k = 2
    while k <= (check2)/2:
        if check2 % k == 0:
            check2_is_prime = False
            break
        k += 1
    if check2_is_prime and check2 > largestPrimeFactor:
        largestPrimeFactor = check2


print largestPrimeFactor