# -*- coding: utf-8 -*-
"""
Created on Mon May 25 10:38:29 2015

@author: Ramy
"""


rightRemaining = 20
downRemaining = 20


def count_routes(rr, dr):
    if rr == 0 and dr == 0:
        return 1
        
    routes = 0
    
    if rr > 0 and dr == 0:
        routes += count_routes(rr - rr, dr)
    elif rr > 0:
        routes += count_routes(rr-1, dr)
        
    if dr > 0 and rr == 0:
        routes += count_routes(rr, dr - dr)
    elif dr > 0:
        routes += count_routes(rr, dr-1)
    
    return routes


print (count_routes(2, 2))



# analytic solution: 40 choose 20 = 137846528820

# Explanation or crude proof: describe a route as a sequence of R's and D's (for right and down).
# There will be 40 R's and D's together.
# Choose 20 to be R's and the rest will automatically be D's.
# All combinations describe all possible routes.