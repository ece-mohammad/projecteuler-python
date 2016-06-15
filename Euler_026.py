from time import time
from primes_euler import gen_primes as p
s=time()

#---------notes-----------------------------
#Taking advantage of the fact that the period of a number n's reciprocal is the smallest (k) such that (n) divides (10^k - 1).
#For fractions (1/n), the decimal representation only repeats for (n) that are relatively prime to (10).
#Furthermore, the number of repeating digits is equal to the multiplicative order of (10 modulo n.)
#Finally, the maximum number of repeating digits is (n-1).

#When a rational number m/n with (m,n)==1 is expanded,
#the period begins after (s) terms and has length (t), 
#where (s) and (t) are the smallest numbers satisfying
#( 10^s=10^(s+t) (mod n)).

limit = 1000

max_len, max_n=0,0

#dividing (1/n) = decimal, (10/n) = decimal, when repeated a specific number of times
#  (10**k)*(1/n)=decimal = (1/n) as the remaider of (10**k)%n starts to repeat.
# so keep dividing (10**k)%n and append remainderds to a list until a remainder repeats
# this indicates a start of a repeating decimal, and the length of the list = the repetend length.

for num in xrange(2,limit):
	remainders = []
	div=1
	while 1:
		div*=10
		rem = div%num
		if rem in remainders: break
		else: remainders.append(rem)
	if len(remainders)>max_len: max_len,max_num = len(remainders),num

print max_num,max_len

print time()-s


'''

#loop over (k) where (k= length of repeating decimal), break
#at first k satisfying the condition.
def deci_len(num):
	for k in xrange(1,num):
		if not ((10**k)-1)%num:
			return k
			break

maxi = (0,0)

#loop over numbers, check if their repetend is longer than the current maximum,
#looping over primes yield a much faster solution.

#for num in xrange(2,limit):
for num in p():
	if num > limit: break
	else:
		if deci_len(num) > maxi[1]:
			maxi = (num,deci_len(num))

print maxi



'''
'''

from time import *
s=time()

limit = 1000
max_len = 0
max_num=0

def rep_dec(num):
	x=1
	rem=[]
	lens=0
	for i in xrange(num):
		x*=10
		r=x%num
		if r not in rem:
			rem.append(r)
		else:
			lens=len(rem)
	return lens,num

for num in xrange(2,limit):
	lens,cnum = rep_dec(num)
	if lens > max_len: max_num,max_len = num,lens

print max_num,max_len
print time()-s

'''


'''
s= time()

import itertools
def recur_len(n):
    # digits for unit fraction 1/n
    r = 10 # initial remainder (10/n)/10
    seen = {} # remainder -> first pos
    for i in itertools.count(0):
        if r == 0:
            return 0  # divides evenly.
        elif r in seen:
            return i-seen[r] # curpos - firstpos
        seen[r] = i
        r= 10*(r % n)

len,i = max((recur_len(i),i) for i in range(2,1000))
print i
'''

'''

def problem26():
    """Find the value of d < 1000 for which 1/d contains the longest recurring 
    cycle in its decimal fraction part."""
    def division(numerator, denominator):
        """Return (quotient, (decimals, cycle_length)) for numerator / denomominator."""
        def recursive(numerator, denominator, quotients, remainders):
            q, r = divmod(numerator, denominator)
            if r == 0:
                return (quotients + [q], 0)
            elif r in remainders:
                return (quotients, len(remainders) - remainders.index(r))
            else:       
                return recursive(10*r, denominator, quotients + [q], remainders + [r])
        decimals = recursive(10*(numerator % denominator), denominator, [], [])            
        return (numerator/denominator, decimals)

# A smarter (and much faster) solution: countdown from 1000 getting cycles length,
# and break when a denominator is lower than the current maximum length
# (since a cycle cannot be larger than the denominator itself).
    return max(xrange(2, 1000), key=lambda d: division(1, d)[1][1])

print problem26()
'''

'''
import math
def frac(n):
   s,hist,rem,point,freeshift,loopfound = '',[],1.,1,0,0
   while (rem > 0.):
      if (rem < n):
         if (freeshift == 0):
            s += '0'
         else:
            freeshift = 0
         if (point):
            point = 0
            s += '.'
         rem *= 10.
      else:
         if (not (rem in hist)):
            hist.append(rem)
            dig = int(math.floor(rem/n))
            s += str(dig)
            rem -= n*dig
            freeshift = 1
         else:
            s += "!!!"
            if (not (loopfound)):
               loopfound = 1
               hist = [rem]
            else:
               return s
            dig = int(math.floor(rem/n))
            s += str(dig)
            rem -= n*dig
            freeshift = 1              
   return s

maxn,maxl = 0,0
for x in range(1,1000):
   f = frac(x)
   if ('!!!' in f):
      seq = f.split('!!!')[1]
      if (len(seq) > maxl):
         maxn,maxl = x,len(seq)

print maxn
'''

'''
import re, numpy
print numpy.argmax(map(lambda n: len([['def' for ln in [str((10**(n-1))+(10**(n-1))/n)[:0:-1]] for e in [re.match("(?P<full>(?P<r>.+?)(?P=r){1,})(?!(?P<rem>.+)(?P=full)(?P=rem).*).*$",ln)] for main in [lambda : ln[::-1] if e is None else e.group('r')]], main()][-1]),range(1,1000)))+1
'''
