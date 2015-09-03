# -*- coding: utf-8 -*-
"""
Created on Tue Jun 02 17:57:01 2015

@author: Ramy
"""



def generate_permutations(digits, permutation):
    global allPermutations
    if len(permutation) == len(digits):
        allPermutations.append(permutation)
    else:
        for d in digits:
            if d not in permutation:
                permutation += d
                generate_permutations(digits, permutation)
                permutation = permutation[0:-1]



allPermutations = []
digits = '0123456789'
perm = ''


generate_permutations(digits, perm)


print allPermutations[999999]