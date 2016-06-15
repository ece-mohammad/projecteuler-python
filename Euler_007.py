'''What is the 10 001st prime number?'''

from time import *
s=time()

from primes_euler import *
res = list()
for i in gen_primes():
	res.append(i)
	if len(res) == 10001:
		break
print res[-1]

print time() - s

'''
from primes_euler import *
res = list()
count = 0
for i in gen_primes():
	prime = i
	count+=1
	if count == 10001:
		break
print prime
'''
