# -*- coding: utf-8 -*-
"""
Created on Sun May 31 10:05:41 2015

@author: Ramy
"""


fh = open('p022_names.txt')


string = fh.read()

names = string.split(',')

for i, s in enumerate(names):
    s = s.replace('"', '')
    names[i] = s


names.sort()
# OTHER WAY: newlist = sorted(names)


letterScores = {'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'F':'6', 'G':'7', 'H':'8', 'I':'9', 'J':'10', 'K':'11',
                    'L':'12', 'M':'13', 'N':'14', 'O':'15', 'P':'16', 'Q':'17', 'R':'18', 'S':'19', 'T':'20',
                    'U':'21', 'V':'22', 'W':'23', 'X':'24', 'Y':'25', 'Z':'26'}

sum = 0

for i, n in enumerate(names):
    letterSum = 0
    for j in n:
        letterSum += int(letterScores[j])
    sum += letterSum * (i+1)

print sum