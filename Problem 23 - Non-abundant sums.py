# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 12:08:25 2015

@author: Ramy
"""

import math

def find_proper_divisors(n):
    div_list = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            div_list.append(i)
            if i != n/i:
                div_list.append(n/i)
    
    return div_list

def check_if_abundant(n):
    sum = 0
    div_list = find_proper_divisors(n)
    for i in div_list:
        sum += i
    if sum > n:
        return True
    else:
        return False

abundant_numbers = []

i = 1
while i < 28123:
    abundant = check_if_abundant(i)
    if abundant:
        abundant_numbers.append(i)
    i += 1


check = []
for i in range(0, 28123 + 1):
    check.append(i)


for j in abundant_numbers:
    for k in abundant_numbers:
        if j + k > 28123: continue
        check[j + k] = 0
    

theSum = 0
for i in check:
    theSum += i
    
print theSum
    