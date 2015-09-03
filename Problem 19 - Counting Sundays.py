# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:51:55 2015

@author: Ramy
"""


#0 is sunday
#1 is monday
#2 is tuesday
#etc

#given: 1 Jan 1900 was Monday
#find: 1 Jan 1901
day = 1
day = (day + 365)%7

sundays = 0


for year in range(1901, 2001):
    leapyear = False
    if year % 4 == 0:
        leapyear = True
        if year % 100 == 0:
            leapyear = False
            if year % 400 == 0:
                leapyear = True
    ## other way: if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0): leapyear = True
    
    for month in range(1, 13):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            day += 31
            if day % 7 == 0:
                sundays += 1
        elif month == 4 or month == 6 or month == 9 or month == 11:
            day += 30
            if day % 7 == 0:
                sundays += 1
        elif month == 2:
            if leapyear:
                day += 29
            elif not leapyear:
                day += 28
            if day % 7 == 0:
                sundays += 1
    
    if year == 2000 and day % 7 == 0:
        sundays -= 1
    
    

print sundays
                