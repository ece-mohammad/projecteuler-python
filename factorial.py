#from time import*
#s = time()

def factor(n):
	res = n
	if (n == 0) or (n == 1):
		return 1
	while n > 1:
		n -= 1
		res = res*n
	return res

#print time()-s
