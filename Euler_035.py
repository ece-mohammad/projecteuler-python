'''
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145
[2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371, 193939, 199933, 319993, 331999, 391939, 393919, 919393, 933199, 939193, 939391, 993319, 999331]
'''
from time import time as t
from primes_euler import gen_primes

ss=t()
cache = []
cp=set()
limit = 10**6

#cache primes under 10**6
for prime in gen_primes(): 
	if prime > limit: break
	else: cache.append(str(prime))

#circularity check
def cir_prime(prime):
	a=len(prime)
	for x in xrange(a):
		#if circulated is prime
		if (prime in cache):
			prime=prime[1:]+prime[0]
		else: return False
	return True


#skip primes with even numbers
for prime in cache:
	if ('2' not in prime) and ('4' not in prime) and ('6' not in prime)\
	 and ('8' not in prime) and('5' not in prime) and (prime not in cp) and (cir_prime(prime)): cp.add(prime)

cp.add('5')
cp.add('2')


print len(cache)
print set(cp),len(set(cp))
print len(cp)

print t()-ss
