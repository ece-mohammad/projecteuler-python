#---------- comments

#solution

#---------- modules

from time import time as t
from bool_prime_sieve import prime_sieve
from itertools import takewhile
from itertools import permutations as perm

#----------- global variables

ss=t()

limit= int(1e6)

#list of True, False for indices represnting primes up to limit
bool_primes= prime_sieve(limit)

#list of primes up to limit
primes= [ind for ind in xrange(limit) if bool_primes[ind]]
#print primes
#------------ functions

def main():
	
	indices=set()
	ind1 = 0
	b=len(primes)
	maxim=0
	
	while ind1<b:
		
#		print '*'*50
#		print 'ind1',ind1
		
		ind2=ind1+1
		while ind2<b:
#			print 'ind2',ind2
			
			a= sum(primes[ind1:ind2])
#			print 'sum',a
			
			if a>limit: break
			else:
				if bool_primes[a]:
					indices.add((ind2-ind1,primes[ind1],primes[ind2],a))
					
			ind2+=1
			
		ind1+=1
		
	return max(indices)

print main()

#print primes,len(primes)

print t()-ss
