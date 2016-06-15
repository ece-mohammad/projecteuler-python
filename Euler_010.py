'''
Find the sum of all the primes below two million.
'''
from time import *
s=time()

import primes_euler
l = []
for i in primes_euler.gen_primes():
	if i < 2000000:
		l.append(i)
	else:
		break
print sum(l)

'''
marked = [0] * 2000000
value = 3 
a = 2 
while value < 2000000: 
	if marked[value] == 0: 
		a += value
		i = value 
		while i < 2000000: 
			marked[i] = 1 
			i += value 
	value += 2 
print a
'''
print time() - s
