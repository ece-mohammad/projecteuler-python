'''
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''
from time import *
s=time()

total = 0

d = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'one-hundred',1000:'one-thousand'}

for i in xrange(1,101):
#------		 1:20
	while (i > 1 and i < 21):
		total += len(d[i])
		break
#------		21:29
	while (i > 20 and i < 30):
		total = total + len(d[20]) + len(d[i-20])
		break
#------

print total

print time() - s
