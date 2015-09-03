import math

def numDivisors(number):
	divisors = 0
	for i in range(1, int(math.sqrt(number)) + 1):
		if number % i == 0:
			divisors += 2
	if int(math.sqrt(number))**2 == number:
		divisors -= 1 # undo double count in the case of a perfect square number
	return divisors

triangular = 1
count = 1

while numDivisors(triangular) <= 500:
	count += 1
	triangular += count

print(triangular)