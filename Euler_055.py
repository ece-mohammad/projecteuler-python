'''
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?
'''

from time import time as t
ss=t()

def rev_num(num):
	return int(str(num)[::-1])

def is_pal(txt):
	return str(txt)==str(txt)[::-1]

def main():
	limit=10000
	nums=[1]+[0]*(limit-1) #array of 0s to save found nums
	found=set()
	n= 0 #start number
	
	while n< limit-1:
		n+=1
		rev_n=rev_num(n)
		#print
		#print 'new number',n
		if nums[n]: continue	#if number is calc before, skip it
		
		itr= 0	#number of iterations
		ttl= n	#to save the sum process
		lych= 1	#assume n is lych
		
		while itr<= 50:
			
			itr+=1
			
			ttl += rev_num(ttl) #reverse and add
			
			if is_pal(ttl):	#check if result is palindromic
				
				itr+=50		#break he iter loop
				nums[n]=0
				nums[rev_n]=0	#change in nums to i, also cange its reverse number
				lych= 0		#n isn't lych
		
		if lych:
			found.add(n)
			#for numbers ending with 10 (multiples of 10), reversing them
			#will result in smaller numbers
			#if not str(n).endswith('0'):
			#if not str(n)[-1]=='0':
			#	found.add(rev_n)
			
			#x= len(str(n))-1
			#if rev_n/(10**x)>1:
			if n%10:
				#print n, rev_n,10**x, rev_n/10**x
				found.add(rev_n)
				nums[rev_n]=1
			#found.add(rev_n)
			
			nums[n]=1
			#nums[rev_num(n)]=1
			#print n#,rev_n
		
	return found

a=main()
#print 'found:',sorted(list(a))
print len(a)
print t()-ss
