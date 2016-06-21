#from time import time as t
#ss=t()

#limit = int(1e7)


def prime_sieve(limit):
#	limit = int(limit)
	#list of True's of len(limit)
	sieve=[True for i in xrange(int(limit+1))]
	#set 0,1 as False, not primes
	sieve[0]=sieve[1]=False
	#prime limit, i,e. the largest possible prime which has multiplicants
	plim = int(limit/2)+1
	#loop over the list starting from 2 end at plim, if it's a prime, set multiplicants as False
	#then continue to next number, the rest of list is prime (not multiplicants of any previous number)
	for prime in xrange(2,plim):
		if sieve[prime]:
			for mult in xrange(prime*2,limit+1,prime):
				sieve[mult]=False

	return sieve

#a=prime_sieve(limit)


'''
from math import sqrt
def getPrimeArray(limit):
#	limit=int(limit)

#Get a boolean array whose entries are true
#if the corresponding index is a prime number,
#false otherwise.
#@param limit The integer upper limit of the array

	isPrime = [True for i in range(0,limit+1)]
	isPrime[0] = isPrime[1] = False
	upperBound = int(sqrt(limit)+1)
	for i in range(2,upperBound):
		if isPrime[i]:
			ub = limit//i
			for j in range(i,ub+1):
				isPrime[i*j]=False
	return isPrime

b= getPrimeArray(limit)

print len(a)==len(b),'equality in len check'

j = zip(a,b)
for i in xrange(len(j)):
	if j[i][0] != j[i][1]: print j[i],i



print t()-ss
'''
