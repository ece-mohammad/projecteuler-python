'''
function that generates fibbo sequence up to -but not including- a certain number
'''
'''
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
from time import *
s=time()

def fib(end):
	a,b = 0,1
	res = list()
	while b < end:
		res.append(b)
		a,b = b,a+b
	return res

end = int(raw_input('Enter the fibbo end: '))
print fib(end)
'''
sums = sum(i for i in fib(end) if (i%2==0))
print sums
'''
print time() - s
