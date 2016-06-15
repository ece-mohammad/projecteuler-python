'''What is the sum of the digits of the number 2***1000?'''
from time import *
s=time()

print sum([int(i) for i in str(2**1000)])

print time() - s
