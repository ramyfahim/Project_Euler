

def length_of_chain(num):
	length = 1
	while num != 1:
		if num % 2 == 0:
			num = num/2
			length += 1
		elif num % 2 == 1:
			num = 3*num + 1
			length += 1
	return length



longestChain = 1
numOfLongestChain = 0
for i in range(1, 1000000):
	if length_of_chain(i) > longestChain:
		longestChain = length_of_chain(i)
		numOfLongestChain = i

print(numOfLongestChain)