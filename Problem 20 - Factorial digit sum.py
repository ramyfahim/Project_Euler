# -*- coding: utf-8 -*-
"""
Created on Sat May 30 00:18:43 2015

@author: Ramy
"""

import math


number = math.factorial(100)

snumber = str(number)

sum = 0

for i in snumber:
    sum += int(i)
    

print sum