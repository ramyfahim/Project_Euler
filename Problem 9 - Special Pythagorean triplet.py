import math

sum = 1000

for a in range(1, int(sum/3)):
	for b in range(1, int(sum/2)):
		c = int(math.sqrt(a**2 + b**2))
		if a**2 + b**2 == c**2:
			if a + b + c == sum:
				product = a * b * c

print (product)

