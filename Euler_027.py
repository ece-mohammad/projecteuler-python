from time import time
from math import sqrt
s=time()
#------------------#notes#--------------------------------------------------

#sol: a= -61, b= 971 , seq_len= 71
# n**2 + a*n + b = prime.
# (b) must be a prime.
# (a) must be odd except when b=2 then (a) must be even.
# (n)'s value can't exceed (b)'s.
# ( a < 2*sqrt(b) ) for all (n) that is a real number
# or (a) ranges from -(2*(sqrt(b)+1)) to (2*(sqrt(b)+1))

#-----------------------------------------------------------------

#maximum length, maximum_a_coefficient, max_b_coefficient.
max_len,max_a,max_b = 0,0,0

#check the primacy of a number.
#used to:
#1- only run b over prime numbers.
#2- check the primacy of equation outputs.

def isprime(n):
	if n<2: return False
	elif n>=2:
		for div in xrange(2,int(sqrt(n))+1):
			if not n%div: return False
	return True


#the prime generating equation.
#loop over the inputs n=[0:b-1],
#keep the consecutive generated sequence of primes in a list,
#break when a number that isn't a prime is generated,
#return the length of the sequence

def euler_prime(a,b):
	prime_seq=[]
	for n in xrange(0,b-1):
		prime = (n**2)+(a*n)+b
		if isprime(prime):
			prime_seq.append(prime)
		elif not isprime(prime): break
	return len(prime_seq),prime_seq


#loop over the possible (b) and (a) values,
#(b)'s start value can be reduced to (41).
#check the sequence length for each pair of (a,b) values,
#if the length is longer than the previous maximum, value are saved
#otherwise, continue the loop.
#break out of (a)'s loop when (a+b > 0).

for b in xrange(41,999):
	if isprime(b):
		for a in xrange(-2*int(sqrt(b)),2*int(sqrt(b))):
			if (a+b>0):
				if euler_prime(a,b)[0] > max_len: max_a,max_b,max_len=a,b,euler_prime(a,b)[0]
			else:
				break
	else:
		continue



#print euler_prime(-79,1601)
#print euler_prime(1,41)
print "a: %d, b: %d, max_seq_length: %d" %(max_a,max_b,max_len),'\n'
print "a*b: %d "%(max_a*max_b),'\n'
print time()-s


'''

from math import sqrt

def isprime(n):
	n = abs(n)
	if n < 1:
		return False
	if n == 1:
		return True
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for t in range(3,int(sqrt(n))+1):
		if n % t == 0:
			return False
	return True
	
def form(a,b):
	n = 1
	while True:
		total = n*(n+a) + b
		if isprime(total) == False:
			return n
		else:
			n += 1


greatest = 0
for a in range(-1000,1000):
	if a == 0: continue
	for b in range(-1000,1000):
		if b == 0: continue
		current = form(a,b)
		if current > greatest:
			greatest = current
			mema = a
			memb = b
print mema
print memb
print mema*memb
'''


'''
#fastest solution in PYTHON so far
from math import sqrt
import time
mil1=time.time()
def prime(n):
    if not n > 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

c=1

for b in range(-999,1000,2):
    if prime(b)==True:
        for a in range(-2*int(sqrt(b)),2*int(sqrt(b))):
            if a%2==1:
                s=0
                n=0
                while prime(n**2+a*n+b)==True:
                    n+=1
                    s+=1
                if s>c:
                    e=a
                    f=b
                    c=s
            
print(e,f,c)
mil2=time.time()
print("Executed Time : ",(mil2-mil1),"Seconds")
'''


'''
import math, collections,time 

stopPt = 1000
cont = True 
ab_list = [] 
nth_list= [0]

mil1= time.time()

def is_prime(num): 
    ans = True 
    stopPt = int(math.sqrt(num))
    for i in range(2, stopPt+1): 
        if num%i == 0: 
            ans = False            
    return ans 
    
def prime_list_under(num):
    ans=[]
    for i in range(2,num +1 ):
        if is_prime(i):
            ans.append(i)
    return ans 

b_list = prime_list_under(stopPt)
for b in b_list :
    for a in range(-stopPt-1, stopPt, 2):
    
        n   = 0
        cont = True 
        if not  a+ b > 0 :
            cont = False 
        while cont:            
            f = lambda n :n**2 + a*n + b             
            if f(n) <2 or not is_prime(f(n) ):                
                cont = False 
                if n >= max(nth_list) and not f(n)<2:
                    nth_list.append(n)
                    ab_list.append([a,b])                    
            n += 1                         
print(ab_list[-1])   
mil2= time.time()
print("time:", (mil2 - mil1), "seconds ")  
'''
