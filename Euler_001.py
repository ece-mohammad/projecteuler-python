''' 

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''

"""
The sum of numbers divisible by 3 below 1000 is:
3+6+9+12+.......+999

dividing all terms by 3:
3*(1+2+3+4+....+333)

the term (1+2+3+4+....+333) is an arithmetic series, where the last element is 1000//3

the sum of all elements up to 333 is given by:
sum_n = n * (a_0 + a_n) / 2

where:
	a_0 is the first element (in this case it'll always be 1)
	a_n is the last element ((1000-1)//3)
	n is the numbber of elements, since the prgression constant is 1, then n = (1000-1)//3

So the term (1+2+3+4+....+333) = 333 * (1 + 333)/2 = 55611

multiplying that with 3, gives us the sum of all numbers below 1000 that are divisible by 3
which is: 166833
"""
from time import time
ss = time()

def sum_multiples(start, end, num):
    return num*(end//num)*((end//num) + start)/2

print(sum_multiples(1, 999, 3) + sum_multiples(1, 999, 5) - sum_multiples(1, 999, 15))
print(time() - ss)

#res = 0
#for i in xrange(3,1000,2):
#	if i%3 ==0 or i%5 == 0:
#		res = res + i
#can be summarized using the list comperhension:
#print sum([i for i in xrange(1000) if (i%3==0) or (i%5 == 0)])

