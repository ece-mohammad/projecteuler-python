'''
Find the sum of the digits in the number 100! (factorial 100)
'''
from time import *
s=time()

def factor(n):
	res = n
	if (n == 0) or (n == 1):
		return 1
	while n > 1:
		n -= 1
		res = res*n
	return res
	
print sum( [int(i) for i in str(factor(100))])

print time() - s
