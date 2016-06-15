'''
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
upper limit: 20161
expected ans: 4'179'871
'''
from time import *
s=time()

limit = 20163

#sum of divisors
def is_abdundant(num):
	sod = 1
	for div in xrange(2,int((num**0.5)+1)):
		if num%div: continue
		else:
			if div*div == num:
				sod+= div
			else:
				sod+=(div + num/div)
	return sod>num

#returns true if (number - (any)abd = abd), iterates over abd set
def is_abd_sum(num):
	return any((num-a in abd) for a in abd)

abd = set()
son = 0
#adds abdundants then check if the number is abd free
for num in xrange(1,limit):
	if is_abdundant(num): abd.add(num)
	if not is_abd_sum(num): son += num


print son
print time()-s

'''
#my opt code
limit = 20163

#sum of divisors
def is_abdundant(num):
	sod = 1
	for div in xrange(2,int((num**0.5)+1)):
		if num%div: continue
		else:
			if div*div == num:
				sod+= div
			else:
				sod+=(div + num/div)
	return sod>num

#returns true if (number - (any)abd = abd), iterates over abd set
def is_abd_sum(num):
	return any((num-a in abd) for a in abd)

abd = set()
son = 0
#adds abdundants then check if the number is abd free
for num in xrange(1,limit):
	if is_abdundant(num): abd.add(num)
	if not is_abd_sum(num): son += num


print son


'''

'''
def is_abundant(n):
    if n == 1 or n == 0:
        return False
    
    s = 0
    d = 1
    while d * d < n:
        if n % d == 0:
            s = s + d + (n / d)
            if s - n > n:
                return True
        d += 1

    if d * d == n:
        s += d

    return s - n > n
    
print is_abundant(20160)
'''

'''

import math

bound = 28123

def get_divisors(n):
    div = set({1})
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            div.add(i)
            div.add(int(n / i))
    return div

abund_nums = set()

for i in range(1, bound + 1):
    if sum(get_divisors(i)) > i:
        abund_nums.add(i)

abund_sums = set()

for num1 in abund_nums:
    abund_sums.add(2 * num1)
    for num2 in (abund_nums - {num1}):
        abund_sums.add(num1 + num2)

non_abund_sums = set(range(1, bound + 1)) - abund_sums
print(sum(non_abund_sums))
'''
#the other way around (sum of all numbers - sum of sums of abdundants)
'''
#finding abundant numbers and making a lsit of them
abundant = []
for a in range(12, 28203): #28203
	facs1 = [x for x in range(1, int(a**0.5+1)) if a%x == 0]
	facs2 = [a/x for x in facs1 if x > 1]
	facs = set(facs1 + facs2)
	if sum(facs) > a:
		abundant.append(a)

		
#combine pairs of abundant numbers
#if the sum is under the limit, add it to a list
#sum that list to find all nums under limit that CAN be written as the sum of two abundant nums
sumsofar = []
for a in abundant:
	for b in abundant:
		summer = a + b
		if summer <= 28123:
			sumsofar.append(summer)
sets = set(sumsofar)
summable = sum(sets)


#sum of all numbers under limit
sumtotal = (28123)*(2+(28122))/2
#sum of all numbers that can't be written as the sum of two abundant nums
nonsum = sumtotal - summable 


print nonsum
'''
#neat sum of divisors
'''
def proper_divisor_sums(limit):
    result = [0] * limit
    for n in range(1, limit):
        for k in range(2*n, limit, n):
            result[k] += n
    return result

def non_abundant_sums():
    abundant_numbers = set()
    for n, s in enumerate(proper_divisor_sums(28123)):
        if s > n:
            abundant_numbers.add(n)
        for a in abundant_numbers:
            if n - a in abundant_numbers:
                break
        else:
            yield n

print(sum(non_abundant_sums()))
'''
'''
from math import sqrt, ceil

def sumOfDivisors( n ) :
	root = int( ceil( sqrt( n ) ) )
	total = 1
	for i in xrange( 2, root ) :
		if n % i == 0 :
			total += i + n // i
	if n != 1 and n == root * root:
		total += root
	return total


def isSumOfTwoAbundants( n ) :
	return any( (n-a in abundants) for a in abundants )

abundants = set()
total = 0

for n in xrange( 1, 28124 ) :
	if sumOfDivisors( n ) > n :
		abundants.add( n )
	if not isSumOfTwoAbundants( n ) :
		total += n
		
print total
'''
'''
My solution is quite similiar, but is about twice as fast at the expense of being slightly longer. 
Calculating the set of abundants in advance is a waste because it makes 
"any(i-a in abundants for a in abundants)" check the entire set of abundants.
If you create the set of abundants as you go, that check becomes much quicker for smaller numbers.
'''
'''
blackonyx's

from itertools import takewhile

class HasSum(Exception): pass

def sumOfDividers(candidate):
    sqrt = candidate**0.5
    list = ((n, candidate/n) for n in xrange(2, int(sqrt) + 1)
            if not candidate%n)
    list = [item for tuple in list for item in tuple]
    list.append(1)
    return sum(set(list))

def abundants(limit):
    collection, logical = [], (limit + 1) * [False]
    for n in range(1, limit + 2):
        if sumOfDividers(n) > n:
            logical[n] = True
            collection.append(n)
    return collection, logical

def main():
    limit, result = 28123, 0
    collection, logical = abundants(limit)
    for number in range(1, limit + 1):
        try:
            for first in takewhile(lambda x: x <= number/2, collection):
                if logical[number - first]: raise HasSum
        except HasSum: pass
        else: result += number
    return result

if __name__ == '__main__':
    print main()

'''
