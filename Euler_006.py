'''Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''
from time import *
s=time()

print (sum([x for x in range(0,101)])**2) - (sum([(i**2) for i in range(0,101)]))

print time() - s
