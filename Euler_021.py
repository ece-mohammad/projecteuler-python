'''
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10 000.
'''
# (220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368)
#ans: 31 626
from time import *
s=time()


def div_sum(num):
	ttl = 1
#ttl = 1 : as xrange starts form 2, so 1 won't be added
#xrange starts from 2 so that num/div doesn't add the number to its divisors
	for div in xrange(2,int(num**0.5)+1):
		if not num%div: ttl += (div + num/div)
	return ttl


def amic_sum(limit):
	ttl = 0
	for num in range(1,limit):
		x = div_sum(num)
#check if d(a) == d(b) and a =/= b
		if div_sum(x) == num and x != num:
			ttl+= num
			
	return ttl


print  amic_sum(100000)
print
print time()-s
#----------------------------------------------------------------------
'''
from time import *
s = time()
x=10000
import math

def sOD(x):
	s = 1
	for i in xrange(2, int(math.sqrt(x)) + 1):
		if (x % i == 0):
			s += i
			s += x / i
	return s

def findSum():

	sum = 0
	for i in xrange(1, 10000):
		x = sOD(i)
		if (sOD(x) == i):
			if (i != x):
				sum += i
	return sum

print findSum()


print time()-s

'''
'''
def divsum(n):return sum([k+n/k for k in range(1,int(n**.5 + 1)) if n%k == 0])-n
print sum([n for n in range(1,10000) if n==divsum(divsum(n)) if n!=divsum(n)])
'''
'''

v=[0]*10000
sum = 0

for value in range(1,10000):
	i = 2*value
	while i < 10000:
		v[i] += value
		i += value
for i in range(1,10000):
	if v[i] < 10001:
		if i == v[v[i]] and i != v[i]:
			sum += i

print(sum)
'''
