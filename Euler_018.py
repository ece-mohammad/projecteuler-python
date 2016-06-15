'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom.

Find the maximum total from top to bottom of the triangle below

00 	              75
01 	             95 64
02 	            17 47 82
03 	           18 35 87 10
04 	          20 04 82 47 65
05 	         19 01 23 75 03 34
06 	        88 02 77 73 07 63 67
07 	       99 65 04 28 06 16 70 92
08 	      41 41 26 56 83 40 80 70 33
09 	     41 48 72 33 47 32 37 16 94 29
10 	    53 71 44 65 25 43 91 52 97 51 14
11 	   70 11 33 28 77 73 17 78 39 68 17 57
12 	  91 71 52 38 17 14 91 43 58 50 27 29 48
13 	 63 66 04 68 89 53 67 30 73 16 69 87 40 31
14	04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

from time import *
s=time()
y='''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''.split('\n')


for i in y:
	ind = y.index(i)
	y[ind] = i.split()
	for j in xrange(len(y[ind])):
		y[ind][j] = int(y[ind][j])

solved = False
l = 13 #line number : start at the second to the last line     >>> y[l]
i = 0 #number index in the line >>> y[l][i]

trace = [[]]

while not solved:
# list of additions in the lines
	trace.append([])

# number of elements in line = line number
	for i in xrange(l+1):
# add the largest of the two numbers in the next line
		if y[l+1][i+1]>y[l+1][i]:
	
			trace[14-l].append((y[l][i]+y[l+1][i+1],y[l][i],y[l+1][i+1]))
			y[l][i]+=y[l+1][i+1]
			
		else:
			
			trace[14-l].append((y[l][i]+y[l+1][i],y[l][i],y[l+1][i]))
			y[l][i]+=y[l+1][i]

#condition to break the while loop
	if l == 0:
		solved = True
	l -= 1

for i in trace:
	print i

print y[0]
print
print time() - s
