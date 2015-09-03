# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:24:17 2015

@author: Ramy
"""



l1 = '75'.split()
l2 = '95 64'.split()
l3 = '17 47 82'.split()
l4 = '18 35 87 10'.split()
l5 = '20 04 82 47 65'.split()
l6 = '19 01 23 75 03 34'.split()
l7 = '88 02 77 73 07 63 67'.split()
l8 = '99 65 04 28 06 16 70 92'.split()
l9 = '41 41 26 56 83 40 80 70 33'.split()
l10 = '41 48 72 33 47 32 37 16 94 29'.split()
l11 = '53 71 44 65 25 43 91 52 97 51 14'.split()
l12 = '70 11 33 28 77 73 17 78 39 68 17 57'.split()
l13 = '91 71 52 38 17 14 91 43 58 50 27 29 48'.split()
l14 = '63 66 04 68 89 53 67 30 73 16 69 87 40 31'.split()
l15 = '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'.split()

lines = []
lines.append(l1)
lines.append(l2)
lines.append(l3)
lines.append(l4)
lines.append(l5)
lines.append(l6)
lines.append(l7)
lines.append(l8)
lines.append(l9)
lines.append(l10)
lines.append(l11)
lines.append(l12)
lines.append(l13)
lines.append(l14)
lines.append(l15)


sum = 0
sums = []

def route_sums(l, i, sum):
    global lines
    global sums
    
    sum += int(lines[l][i])
    
    if l == 14:
        sums.append(sum)
        return 1
    
    route_sums(l+1, i, sum)
    
    route_sums(l+1, i+1, sum)
    
    
    
route_sums(0, 0, sum)

#print len(sums)

print max(sums)

