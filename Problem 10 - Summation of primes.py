
import math

sum = 0

check = 2

while check < 2000000:
    isPrime = True
    for i in range(2, int(math.sqrt(check)) + 1):
        if (check % i == 0):
            isPrime = False
            break
    if isPrime:
        sum += check
    check += 1

print (sum)