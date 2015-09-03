# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:13:06 2015

@author: Ramy
"""

num1 = 1
num2 = 1

term = num1 + num2
index = 3

while len(str(term)) < 1000:
    num1 = num2
    num2 = term
    term = num1 + num2
    index += 1

print index