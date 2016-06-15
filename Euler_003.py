'''largest prime factor of 600851475143 '''
from time import *
from primes_euler import *
s = time()

x = 600851475143
p=[]

for i in gen_primes():
	
	if i> x:
		break

	if x%i == 0:
		p.append(i)
		x/=i

print p,max(p)
print time() - s

'''
number = 600851475143
primes = []
runningFactor = 2

while number != 1:
    if number % runningFactor == 0:
        if runningFactor not in primes:
            primes.append(runningFactor)
            
        number/= runningFactor
        runningFactor = 2
    else:
        runningFactor+= 1

print primes
print max(primes)
print time() - s
'''
'''
import time
start_time = time.time()
strt_time = time.clock()
def largestPrimeFactor(n):
    x = 2
    while True:
		print n,x
		if n%x: x += 1
		elif not x == n: n /= x
		else: return x


print largestPrimeFactor(600851475143)
print '%f' %(time.time()-start_time)
print strt_time,time.clock(),'\n',time.clock()-strt_time
'''
