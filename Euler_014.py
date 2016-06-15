'''
collatz sequence:
n = n/2 (n is even)
n = 3*n + 1 (n is odd)
Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
#The starting number 837799 produces a sequence of 525.

from time import *
s=time()

solved = False
#-------- n: starting number
#-------- dict of (start number:list of its chain) to save all chains
#-------- maxi : var to save longest chain so far
#-------- res : list of the longest chain so far
n = 3
q = {}
maxi = 0
res = []

while n < 1000000:
#add a new entry in q for n	
	q[n]=[]
#add a temp variable equals n, as n is the key in q to its chain
	a = n
	while a > 1:
#check if even
		if a%2 == 0:
			a/=2
#check if a's chain was calculated before (if a in q)
#then add a's chain to current n and break to next n
#else continue
			if a in q:
				q[n].extend(q[a])
				break
			else:
				q[n].append(a)
				
		else:
#check if odd			
			a = (a*3)+1
#same as the even part			
			if a in q:
				q[n].extend(q[a])
				break
			else:
				q[n].append(a)

#check the length of n's chain				
	if len(q[n])> maxi:
		maxi = len(q[n])
		res = (n,q[n])
	
	n+=2

print res
print
print maxi
print
#print q

print time() - s

'''
from time import *
s = time()

def main(limit = 10**6):
    cache = {1:0}

    def dist(nr):
        if nr in cache: return cache[nr]
        else:
            distance = 1 + (dist(3*nr+1) if nr%2 else dist(nr/2))
            cache[nr] = distance
            return distance

    longest, winner = 0, 1
    for candidate in range(2, limit + 1):
        distance = dist(candidate)
        if distance > longest: longest, winner = distance, candidate
    return winner

print main()

print time() - s
'''
