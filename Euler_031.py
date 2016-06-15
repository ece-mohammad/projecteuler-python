from time import time
s=time()

count =0

for a in xrange(200,-1,-200):
	for b in xrange(a,-1,-100):
		for c in xrange(b,-1,-50):
			for d in xrange(c,-1,-20):
				for e in xrange(d,-1,-10):
					for f in xrange(e,-1,-5):
						for g in xrange(f,-1,-2):
							count+=1

print count
print time()-s

'''
coinvalues = [1, 2, 5, 10, 20, 50, 100, 200]

def count(total, largest):
    if largest > total: return 0
    if largest == 1 or largest == total: return 1
    c = 0
    remaining = total - largest
    for coin in coinvalues:
        if coin > largest: return c
        c += count(remaining, coin)
    return c
    
print sum(count(200, coin) for coin in coinvalues)
'''
'''

total = 200
combinations = [1] + [0]*total
monies = [1,2,5,10,20,50,100,200]

for x in monies:
	for i in xrange(x,201):
		combinations[i] += combinations[i-x]
		
print combinations[total]
'''
