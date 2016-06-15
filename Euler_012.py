'''
What is the value of the first triangle number to have over five hundred divisors?
'''
#ans: 76576500   i =12375
#--------- generate triangular numbers -----
'''
T = (n*(n+1))/2
'''
from time import *
s = time()
#------------- no. of divisors function ----------
def divz(num):
	factors = []
	for divisor in xrange(1,num+1):
		if num%divisor == 0:
			factors.append(divisor)
	return factors

#print divz(25)
#------------- triangular number generator -------
def tri_gen():
# T = (n*(n+1))/2
	n = 0
# a : even co-prime
# b : odd co-prime
	while True:
		if n%2 == 0:
			a = n
			b = n+1
		else:
			a = n+1
			b = n
		T = ((a*b)/2)
		yield n,a,b,T
		n+= 1
#---------------
for i,j,k,l in tri_gen():
	if len(divz(j/2))*len(divz(k)) > 500:
		print divz(j/2),len(divz(j/2))
		print divz(k),len(divz(k))
		print 'Order:',i,'\t even co-prime:',j,'\t odd co-prime:',k,'\t triangular number:',l
		break
#----------------
print time() - s
