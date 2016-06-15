'''
How many such routes are there through a 20X20 grid?
'''
#In a 20x20 grid there are 137 846 528 820 possible paths.
#                          137 846 528 820
#(2**40/7)
#2**20 = 1048576
#2**40 = 1 099 511 627 776
#by using combinatronics >> 40 C 20
n = 40

from time import *
from math import factorial as fact
s = time()
print fact(n)/(fact(n/2)*fact(n -n/2))
print time() - s
