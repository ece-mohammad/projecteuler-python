from time import time
from itertools import permutations as p
ss=time()

def prime_sieve(limit):
	sieve=['a']*limit

	sieve[0]=sieve[1]=False

	for num in xrange(2,limit):
		
		if sieve[num]=='a':
			sieve[num]=True
			
			for mult in xrange(2*num,limit,num):
				sieve[mult]=False

	return sieve

limit=int(1e6)
prime=prime_sieve(limit)
#primes= [n for n in prime_sieve(limit) if n]
#print len(primes)

def gen_pat(ones,zeros,length):
	#return a list of all possible sub patterns
	#with 1s as sub numbers and 0s as fixed num
	#takes 3 ints, Ones, Zeros, number length
	#make sure ones+zeros==lenght
	#zeros are the digits that will be replaced by the same number
	#while ones are the fixed digits
	a=[1]*ones+[0]*zeros
	comb= [i for i in p(a,length)]
	return comb
#c=gen_pat(2,3,5)
#print len(c)
#print c


def fill_zeros(pat,zero):
	res=pat[:]
	a=len(pat)
	for ind in xrange(a):
		if not pat[ind]:
			res[ind]=zero
	return res

#print fill_zeros([1,0,0,1,0],4)

def fill_ones(pat,ones):
	a=len(pat)
	res=pat[:]
	ind_o=0
	#print 'given ones',ones,'given pat',pat
	if pat.count(1)!=len(ones):
		print 'ValueError: ones lenght is invalid!'
		return None
	for ind in xrange(a):
		if pat[ind]:
			res[ind]=ones[ind_o]
			ind_o+=1
	return res

#print fill_ones([1,0,0,1],[6,9])
#print fill_ones([1,0,1,1],[6,9])
#print fill_ones([1,0,0,0],[6,9])

def calc_num(lst):
	#takes a list of numbers and calc the decimal
	#value of the number depending on the index of each
	#digit
	lst=lst[::-1]
	a=len(lst)
	res=0
	for ind in xrange(a):
		res+= lst[ind]*(10**ind)
	return res
#print calc_num([1,2,3,0,9,6,9])

def main():
	#generate patterns with 3 zeros 2 ones and
	#patterns with 2 zeros and 3 ones for a
	#5 digit number
	#test case 1:
	# 2 digit numbers, seq len of 6 >> passed
	##test case 2:
	#5 digit numbers, seq len of 7
	#passed
	target=8
	nzeros=1
	digits=6
	suffix=[1,3,7,9]
	##write=0
	los=[]
	while nzeros<digits-1:
		nones=digits-nzeros
		print 'ones:',nones,'zeros:',nzeros
		#set number of zeros
		
		#generate the respective patterns
		#as a list of tuples
		patterns=gen_pat(nones,nzeros,digits)
		
		#remove redundancies
		#patterns=sorted(list(set(patterns)))
		patterns=set(patterns)
		#patterns=list(patterns)
		#print patterns
		#print len(patterns)
		
		#print 'generated patterns',patterns
		#print 'starting iteration over patterns...'
		
		#iterate over the patterns
		for pat in patterns:
			pat=list(pat)
			
			#print 'current pattern',pat
			
			pat_woz=pat[:]	#type:list
			#iterate over all possible ones
			#print 'iterating over fixed digits..'
			
			#if pat==[0,1,0,1,1,1]: print 'current pat: [0,1,0,1,1,1]'
			
			#for one in sorted(list(set(p(range(1,10),nones)))):
			for one in set(p(range(1,10)*2,nones)):
				#0 is excluded for 2 digit numbers
				seq=[]
				#make a list for the found primes
				loo=list(one)	#type: list
				#print loo
				##if loo==[2,3,1,3]:
					##write=1
				##else:
					##write=0
				
				##if write: print 'fixed digits are',loo
				
				#list of ones
				#fill the pattern with ones
				pat=fill_ones(pat_woz,loo)
				
				##if write: print 'filled with ones',pat,'pat2',pat_woz
				
				#break if pat ends with non suffix digits
				if pat[-1] in [2,4,5,6,8]:
					##if write: print 'pat ends with non prime digits, skipping..'
					continue
				
				pat_wz=pat[:]	#type:list
				
				#iterate over the zeros
				#print 'iterating over zeros...'
				for zero in xrange(10):
					
					##if write: print 'current zero',zero
					
					pat=fill_zeros(pat_wz,zero)	#type:list
					
					##if write: print 'filled with zeros',pat
					
					#break if pat ends in non suffix digits
					if pat[-1] not in suffix:
						#print 'pat ends with non prime digits, skipping..'
						continue
					
					#calculate the number
					num=calc_num(pat)	#type:list
					
					if num<10**(digits-1): continue
					
					##if write: print 'calculated number is',num
					
					#add to seq list if it's a prime
					if prime[num]:
						seq.append(num)
						
						##if write: print 'current seq:',seq
						
				#print 'seq=',seq
				#if seq length == target, stop and return the
				#smallest number, sequence and sequence length
				#print '%-'*40
				if len(seq)==target:
					los.append(seq)
		nzeros+=1
	return los

a=main()
print time()-ss
print min(a)
#for one in p(range(10),3):
#	print list(one)
print time()-ss

