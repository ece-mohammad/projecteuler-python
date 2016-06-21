'''

mathematical fallacy: division
ab/bc = a/c

n/d
where n: ac, d:bc
and ac/bc = a/b

'''

from time import time as t
s=t()

sol = []

for a in xrange(1,10):
	for b in xrange(a,10):
		for c in xrange(b,10):
			n1 = a+10*c ; n2 = 10*a+c
			d1 = b+10*c ; d2 = 10*b+c
			if a<b:
				if n1*b == d1*a: sol.append((n1,d1,a,b))
				elif n2*b == d1*a: sol.append((n2,d1,a,b))
				elif n1*b == d2*a: sol.append((n1,d2,a,b))
				elif n2*b == d2*a: sol.append((n2,d2,a,b))
			else: continue

print sol

t1,t2 = 1,1
for a,b,c,d in sol:
	t1*=a; t2*=b

print float(t1)/t2

print t()-s


