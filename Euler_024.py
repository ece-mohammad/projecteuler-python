'''
find the nth permutation of a text
'''
from time import *
from factorial import factor as f
s = time()

def nth_perm(n,txt):
	txt = txt.split(' ')
	ans = ''
	
	while len(txt) >2:
		l = len(txt)-1
		#print 'l',l
		#print 'n',n
		ind = n/f(l)
		#print 'ind',ind
		n = n%f(l)
		#print 'n',n
		if n == 0:
			ind -= 1
		ans+= txt.pop(ind)
		#print ans
	if n == 0: ans+=txt.pop(txt.index(max(txt)))
	else: ans+=txt.pop(txt.index(min(txt)))
	ans+= txt.pop()
	return ans

print nth_perm(1000000,'0 1 2 3 4 5 6 7 8 9')

print time()-s
