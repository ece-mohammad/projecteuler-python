from time import time
s=time()
#numbers spiral diagonal sum
#the NE diagonal is the square of odd numbers (2n+1)**2
#the difference between the diagonals = even numbers (2n)
#starting from the center and move out, the number of elements on the diagonal = spiral size/2 +1
#excluding 1.
#
'''
columns:
       1  2  3   
---------------- rows:
21          25 |3
    7     9    |2
       1       |1
    5     3    |
17          13 |


21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
'''
spiral_size = 1001
'''
def diagonal_sum(n):
	elem1 = ((2*n)+1)**2
	elem2 = elem1 - (2*n)
	elem3 = elem2 - (2*n)
	elem4 = elem3 - (2*n)
	
	return sum([elem1,elem2,elem3,elem4])
'''	

'''
def diagonal_sum(n):
	return (16*(n**2) + 4*n + 4)
'''

'''
ttl = 0
for size in xrange(1,spiral_size/2+1):
	ttl+= diagonal_sum(size)
'''

spiral_size = 5
print (sum(map(lambda n:(16*(n**2) + 4*n + 4),xrange(1,spiral_size/2+1))))+1

#print ttl+1
print time()-s
