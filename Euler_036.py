from time import time as t

ss=t()

limit = 10**6

res=[]

'''
def dec2bin(num):
	b=''
	while num > 0:
		b=b+str(num%2)
		num/=2
	return b
'''

'''
def ispal(x):
	x=str(x); a=len(x)
	if a==1: return True
	elif a%2:
		print x[-((a/2)+2)::-1],x[a/2+1:]
		return x[-((a/2)+2)::-1]==x[a/2+1:]
	else:
		print x[-((a/2)+1)::-1],x[a/2:]
		return x[-((a/2)+1)::-1]==x[a/2:]
'''

def dec2bin(num):
	return bin(num)[2:]

def ispal(str):
	ind = len(str)/2
	return str[0:ind]==str[-1:-(ind+1):-1]

#check for odd numbers
for num in xrange(1,limit,2):
	if ispal(str(num)) and ispal(dec2bin(num)): res.append(num)

print res
print len(res)
print sum(res)


print t()-ss
