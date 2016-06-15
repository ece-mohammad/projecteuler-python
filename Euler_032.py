#9 pan-digital numbers
#pan = '123456789'
'''
a*b=c
based on 10*1 * 10**4 = 10**5
{9 * 999  = 8991	> 8-digits
 9 * 9999 = 89991	> 10-digits } >>> 1
 
and 10**2 * 10**3 = 10**5
{99 * 99  = 9801	> 8-digits
 99 * 999 = 98901	> 10-digits } >>> 2

from 1 and 2:
we can get 'c' when: 'b' is within [999 : 9999] and 'a' [2:9]
and also when 'b' is within [99:999] and 'a' [10:99]

combining the limits on both a and b:

2<a<100
100<b<10000

'''

from time import time as t

s=t()

def ispan(y):
	x='123456789'
	z=''.join(sorted([i for i in y]))
	return z==x

'''
#ispan test

import random as r
x=range(1,10)
f=[i for i in x]
print f
r.shuffle(f)
print f
f=''.join([str(i) for i in f])
print f
print ispan(f)
'''
q=0
x = lambda n: str(n)
prod=set()							#set to avoid duplicates.
for a in xrange(100,10000):
	for b in xrange(2,100):
		#q+=1						#number of iterations.
		c=x(a)+x(b)+x(a*b)
		if len(c)<9: continue
		#elif '0' in c: continue	#adding this line or-combining it with the prvious if-stat. increases the runtime, weird.
		elif len(c)>9: break		#major speed up.
		else:
			if ispan(c): prod.add(a*b)#;print a,b,c
			#if len(set(c))==len(c) and '0' not in c: prod.append(a*b)
#print prod
#print q
print sum(prod)
print t()-s
