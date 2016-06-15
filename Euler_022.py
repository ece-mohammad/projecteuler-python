#over 5'000 names
#1 : sort the names
#2 :  alphabetical value for each name
#3 : multiply this value by its position in the list to obtain a name score.
#d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
#What is the total of all the name scores in the file?
# ans: 871 198 282
#------------------------------------

from time import *
from re import *

s=time()
d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
#def alpha_value(txt):

names = []
txt = open('p022_names.txt')
#read the text file, search for all alphaneumeric chars (\w)(+)
# till a non-alphaneumeric char is reached, return as a list
for name in findall(r'\w+',txt.read()):
	names.append(name.lower())

names.sort()

#score depending on the name letters
def name_score(name):
	name = name.lower()
	score = 0
	for letter in name:
		score += d[letter]
	return score

#score depending on the position in the list
def position_score(name):
	final_score = name_score(name)*(names.index(name)+1)
	return final_score


summ = 0
for name in names:
	summ += position_score(name)


print summ
print
print time()-s

'''

# First load the file and sort it.

x = eval( '[' + open( 'p022_names.txt' ).readlines()[ 0 ] + ']' )
x.sort()

# Then calculate what is needed.

print reduce( lambda x, y: x + y, [ reduce( lambda x, y: x + y, [ ( j + 1 ) * ( ord( i ) - 64 ) for i in x[ j ] ] ) for j in xrange( len( x ) ) ] )	
'''
'''
import string
from time import *

start = time()
valuehash = dict(zip([x for x in string.letters[26:]],range(1,27)))
names = [x[1:-1] for x in string.split(open('p022_names.txt','r').read()[:-1],',')]
names.sort()
namescores = [sum([valuehash[x] for x in names[i]])*(i+1) for i in range(len(names))]
print "Sum = %d" % sum(namescores)
print "Time taken = %f" % (time()-start)
'''
