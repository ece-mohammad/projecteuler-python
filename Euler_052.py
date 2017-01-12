from time import time as t
ss=t()

found = 0

i=100

def mul6(n):
	s=set(str(n))
	for i in xrange(2,7):
		if not set(str(n*i)) == s:
			return False
	return True

while not found:
#	print 'trying %s'%i
	if mul6(i):
		found=i
		break
	i+=1
#	print '*'*50

print found

print t()-ss
