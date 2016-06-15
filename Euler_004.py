'''
Find the largest palindrome made from the product of two 3-digit numbers.

'''

from time import *
s=time()
def ispal(str):
	ind = len(str)/2
	if str[0:ind]==str[-1:-(ind+1):-1]:
		return True
	else:
		return False

res = list()
for x in xrange(900,1000):
	for y in xrange(x,1000):
		if ispal(str(x*y)):
			res.append(x*y)

print max(res)
print time()-s

#print max([x*y for x in range(900,1000) for y in range(900,1000) if str(x*y) == str(x*y)[::-1]])

'''
def get_numbers():
    for a in range (800, 1000):
        for b in range(a, 1000):
            yield a * b

def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(max(x for x in get_numbers() if is_palindrome(x)))
'''
'''
def ispal(str):
	ind = len(str)/2
	if str[0:ind]==str[-1:-(ind+1):-1]:
		return True
	else:
		return False

res = 0
for x in xrange(900,1000):
	for y in xrange(x,1000):
		if ispal(str(x*y)):
			if x*y > res: res = x*y

print res
'''
