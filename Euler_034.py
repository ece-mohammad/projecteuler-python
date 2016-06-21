'''
Factorions
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145

upper bound: 9!*7 as 9!*7 < 9'999'999
approximated to 50'000
'''
from time import time as t
s=t()

sol=[]

cache = [0]*10

def factor(n):
	res = n
	if (n == 0) or (n == 1):
		return 1
	while (n > 1):
		n -= 1
		res *= n
	return res

for num in xrange(10):
	cache[num] = factor(num)

for x in xrange(3,50000):
	ttl=0
	for i in str(x): ttl+= cache[int(i)]
	if x==ttl: sol.append(x)

print sol,sum(sol)

print t()-s

