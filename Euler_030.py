from time import time
s=time()
def sod(num):
	return sum(int(x)**5 for x in str(num)) == num

limit = 200000
num=2
found = []

while 1:
	if sod(num): found.append(num)
	num+=1
	if num == limit: break

print found
print sum(found)
print time()-s
