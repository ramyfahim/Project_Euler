# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:18:01 2015

@author: Ramy
"""


stillLooking = True

test = 20


while stillLooking:
    aMultiple = True
    for i in range(1,21):
        if test % i != 0:
            aMultiple = False
            break
    if aMultiple == True:
        number = test
        stillLooking = False
    test += 20

print number