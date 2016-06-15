'''
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from time import *
s=time()

#------------pythagorean natural triplet of sum 1000 -----------------
# for a,b,c:
# a or b is odd, c is always odd
# a or b is divisible by 4
# a or b is divisible by 3
# a or b or c is divisible by 5
# largest common divisor for a*b*c is 60
# euclid's formula:
# a = ((n**2) - (m**2))
# b = (2*m*n)
# c = ((m**2) + (n**2))

#######################################################################

t = []
for m in xrange(1,50):
	for n in xrange(m,51):
		a = ((max(m,n)**2) - (min(m,n)**2));b = (2*m*n);c = ((m**2) + (n**2))
		if a**2 + b**2 == c**2 and a+b+c==1000:
			t.append([(m,n),(a,b,c)])
			break
print t
print a*b*c

print time() - s
