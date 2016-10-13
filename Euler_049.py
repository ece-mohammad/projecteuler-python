#---------- comments

#solution

#---------- modules

from time import time as t
from bool_prime_sieve import prime_sieve
from itertools import takewhile
from itertools import permutations as perm

#----------- global variables

ss=t()

limit= int(1e4)

#list of True, False for indices represnting primes up to limit
bool_primes= prime_sieve(limit)

#list of primes up to limit
primes= [ind for ind in xrange(1000,10000) if bool_primes[ind]]

#------------ functions

def main():
	
	a=len(primes)
	
	for ind in xrange(a):
		
		n1=primes[ind]
		
		for ind2 in xrange(ind+1,a):
			
			n2=primes[ind2]
			
			b=abs(n1-n2)
			#b=3330
			if (n2+b)>limit:
			#if n2-n1 != b or n2+b>limit:
				continue
			
			else:
				if bool_primes[(n2+b)]:
					n3=(n2+b)
					#print n1,n2,n3
					
					p1,p2,p3 = str(n1),str(n2),str(n3)
					
					p1,p2,p3= set(p1), set(p2), set(p3)
					
					if p1==p2==p3:
						print n1,n2,n3

print main()


#print primes,len(primes)

print t()-ss

'''
from time import time as t
import time
ss= t()


#----- set initial values
import time
import itertools
from math import sqrt


def isprime(number):  # dual purpose - determines primality, and, if so adds to primes array
    index = 0
    sqrt_number = sqrt(number)
    while primes[index] <= sqrt_number:
        if number % primes[index] == 0:
            return False
        index += 1
    primes.append(number)
    return True


def alldone(x):
    if isprime(x):
        permutations = set()
        for item in (itertools.permutations(str(x), 4, )):
            permutations.add(int(''.join(item)))

        if 1487 not in permutations:
            for permutation in permutations.copy():
                if permutation not in primes:
                    if not (isprime(permutation)):
                        permutations.remove(permutation)
            size = len(permutations)
            if size > 2:
                permutation_list = list(permutations)
                for a in range(0, size):
                    for b in range(a + 1, size):
                        for c in range(b + 1, size):
                            if permutation_list[c] - permutation_list[b] == permutation_list[b] - permutation_list[a]:
                                print(permutation_list[a], permutation_list[b], permutation_list[c],
                                      '(', permutation_list[c] - permutation_list[b], ')')
                                return True
    return False


startTime = time.clock()
maxPrime = int(sqrt(9999))  # max needed prime for primality determination of a 4-digit #
primes = [2]  # "prime" (ha-ha) the set to avoid a repeated 'if-null' check

for x in range(3, maxPrime):
    isprime(x)

for x in range(1000, 10000):  # we're technically not told whether "1487" is the first or the last such triple
    if alldone(x):
        break

print(time.clock() - startTime, 'seconds')
#---- test

print t()-ss


'''
