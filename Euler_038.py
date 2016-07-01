#-------------------- modules import
from time import time as t

#----- start time
ss=t()

#-------------------- functions

#--- check txt if 1-9 pandigital
def is_pan(txt):
	txt=str(txt)
	if len(txt)>9 or len(txt)<9: return False
	else:
		pan=set('123456789')
		return pan==set(txt)


#--- concatenate multiplications
def com(num):
	c=''
	for i in xrange(1,10):
		c+=str(num*i)
		if len(c)>=9: break
	return c


#--------------- main
def main():
	maxi=0;n=0
	for num in xrange(9000,10000):
		a=com(num)
		if is_pan(a) and int(a)>maxi: maxi,n=int(a),num
	print maxi,n

#932'718'654

main()

print '\n',t()-ss


#-------------------------------
'''
alt solution from mbh038  
on projecteuler forum

import time
import itertools

def panmult(n):
    start_time = time.time()
    prodmax=-1    
    basenums=[]
    for digits in range(1,4):
        for i in itertools.permutations('1234678',digits):
            basenums.append('9'+''.join(i))
    
    for i in basenums:
        prod=''
        for multiplier in range(1,10):
            newprod=prod+str(multiplier*int(i))
            if len(newprod)!=len(set(newprod)) or '0' in newprod:
                break
            prod=newprod
            if int(prod)>prodmax and len(prod)==9:
                imax,prodmax,multmax=i,int(prod),multiplier
            
    print imax,range(1,multmax+1),prodmax
        
    print("--- %s s ---" % (time.time() - start_time))
'''
