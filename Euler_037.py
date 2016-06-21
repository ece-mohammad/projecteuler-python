#ans: 748'317
from time import time as t
from bool_prime_sieve import prime_sieve

ss=t()

limit = int(1e6)
nums = prime_sieve(limit)

def gp(sieve):
	for prime in xrange(len(sieve)):
		if sieve[prime]: 
			pass

def trp(prime):
	#right trunc check
	p=prime
	power=0
	while prime>0:
#		print prime,'rtp'
		if not nums[prime]: return False
		else:
			#print prime
			prime/=10
			power+=1
	
	#left trunc check
	while power>0:
#		print p,'ltp'
		if not nums[p]: return False
		else:
#			print power,'power'
			p=p%(10**(power-1))
			#print p
			power-=1
	return True


print sum(filter(trp,[prime for prime in xrange(len(nums)) if nums[prime] and prime>10]))



print t()-ss
