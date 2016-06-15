from time import*
s=time()

def fib():
	a,b = 0,1
	while True:
		yield b
		a,b = b,a+b

count = 0
for i in fib():
	count+=1
	if len(str(i)) < 1000:
		continue
	else:
		break
print count,'\n'
print i,'\n'
print time()-s

'''
aying that a number contains 1000 digits is the same as saying that it's greater than 10**999.
The nth Fibonacci number is [phi**n / sqrt(5)], where the brackets denote "nearest integer". 
So we need:
phi**n/sqrt(5) > 10**999 n * log(phi) - log(5)/2 > 999 * log(10)
n * log(phi) > 999 * log(10) + log(5)/2 
n > (999 * log(10) + log(5) / 2) / log(phi)
A handheld calculator shows the right hand side to be 4781.8593,
so 4782 is the first integer n with the desired property.
Why bother with a computer on this one?
'''
