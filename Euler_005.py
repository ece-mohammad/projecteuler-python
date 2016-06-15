'''
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
from time import *
s=time()

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    D = {}
    q = 2
    
    while True:
        if q not in D:
   
            yield q
            D[q * q] = [q]
        else:
            
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1

#---------------------------------------------
#function to check the divisors of a number
#

def devs(num):
	res = []
	for i in xrange(1,num):
		if num%i == 0:
			res.append(i)
	return res
#--------------------------------------------
"""

"""
limit = 20
res = 1
nums = []
for i in gen_primes():
	if i <= limit:
		p = 1
		while (i**p) <= limit:
			p+=1
		p-=1
		nums.append(i**p)
			
	else:
		for i in nums:
			res *= i
		break

#print nums
print res

#z = devs(res)
#print z
#print len(z)
print time() - s
