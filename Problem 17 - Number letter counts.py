# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:26:23 2015

@author: Ramy
"""


numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
           10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
           16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty',
           40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety',
           100:'hundred', 1000:'onethousand'}

letterCount = 0

for i in range(1, 1001):
    s = str(i)
    if len(s) == 1:
        letterCount += len(numbers[i])
    elif len(s) == 2:
        if i < 20:
            letterCount += len(numbers[i])
        else:
            s1 = int(s) - int(s[1])
            letterCount += len(numbers[s1])
            if s[1] != '0':
                s2 = int(s[1])
                letterCount += len(numbers[s2])
    elif len(s) == 3:
        s1 = int(s[0])
        letterCount += len(numbers[s1])
        letterCount += len(numbers[100])
        if s[1] == '1':
            s2 = int(s[1:3])
            letterCount += len(numbers[s2])
        else:
            if s[1] != '0':
                s2 = int(s[1:3]) - int(s[2])
                letterCount += len(numbers[s2])
            if s[2] != '0':
                s3 = int(s[2])
                letterCount += len(numbers[s3])
        if s[1] != '0' or s[2] != '0':
            letterCount += len('and')
    elif len(s) == 4:
        letterCount += len(numbers[1000])


print letterCount
