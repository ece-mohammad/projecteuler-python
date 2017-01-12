from time import time
from itertools import permutations as p
ss=time()

'''
01- High Card: Highest value card.
02- One Pair: Two cards of the same value.
03- Two Pairs: Two different pairs.
04- Three of a Kind: Three cards of the same value.
05- Straight: All cards are consecutive values.
06- Flush: All cards of the same suit.
07- Full House: Three of a kind and a pair.
08- Four of a Kind: Four cards of the same value.
09- Straight Flush: All cards are consecutive values of same suit.
10- Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
'''

#max no. of cards of same value = 4

card_suits={'H':33,'D':22,'C':11,'S':44}

card_ranks={'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,\
'J':10,'Q':11,'K':12,'A':13}

hand_ranks={'royal flush':1000,'straight flush': 900,'four of a kind': 800\
,'full house':700,'flush':600,'straight':500,'three of a kind':400,\
'two pairs':300,'one pair':200,'high card':100 }

def hand_format(hand):
	vals=[]
	suits=[]
	for card in hand:
		vals.append(card_ranks[card[0]])
		suits.append(card_suits[card[-1]])
	return vals,suits

line = '5D 8C 9S JS AC 2C 5C 7D 8S QH'
line=line.split(' ')
p1=line[:5]
p2=line[5:]
p1=hand_format(p1)
p2=hand_format(p2)
#print p1
#print p2

def royal_flush(vals,suits):
	return (vals==[9,10,11,12,13] and len(set(suits))==1),suits[0]

#print 'royal flush',royal_flush([9,10,11,12,13],[11,11,11,11,11])

def straight_flush(vals,suits):
	straights=[]
	nums=range(11,1,-1)
	ind=0
	while ind<6:
		straights.append(nums[ind:ind+5])
		ind+=1
	return (vals in straights and len(set(suits))==1),max(vals)

#print 'straigt flush',straight_flush([1,2,3,4,5],[11,11,11,11,11])

def four_kind(vals,suits):
	one=0
	for i in vals:
		if vals.count(i)==1: one=1
		elif vals.count(i)==4: return (True,i,one)
	return False,0

#print 'four of a kind',four_kind([1,2,2,2,2],[11,11,11,11,11])

def full_house(vals,suits):
	three=0
	two=0
	for i in vals:
		if vals.count(i)==2: two=i
		elif vals.count(i)==3: three=i
	return bool(three and two),three,two

#print 'full house',full_house([1,2,2,2,1],[11,11,11,11,11])

def flush(vals,suits):
	return len(set(suits))==1

#print 'flush',flush([1,6,4,5,1],[11,11,11,11,11])

def straight(vals,suits):
	straights=[]
	nums=range(11,1,-1)
	ind=0
	while ind<6:
		straights.append(nums[ind:ind+5])
		ind+=1
	return (vals in straights),max(vals)
#	return straight_flush(vals,[11,11,11,11,11])

#print 'straight',straight([1,2,3,4,5],[11,12,13,11,11])

def three_kind(vals,suits):
	other=[]
	three=False
	for i in vals:
		if vals.count(i)<3: other.append(i)
		elif vals.count(i)==3: three=i
	return bool(three),three,other

#print 'three of a kind',three_kind([1,2,2,1,1],[11,11,11])

def two_pairs(vals,suits):
	
	first=0
	second=0
	other=0
	
	for i in vals:
		if i==first: continue
		elif vals.count(i)==1:
			other=i
		elif vals.count(i)==2:
			if not bool(first):
				first=i
			else:
				second=i
		tmp=max(first,second)
		second=min(first,second)
		first=tmp
	return bool(first and second),first,second,other

#print 'two pairs',two_pairs([1,1,2,9,2],[11])

def one_pair(vals,suits):
	other=[]
	tmp=0
	pair=False
	for i in vals:
		if vals.count(i)==2:
			pair=i
		elif vals.count!=2:
			other.append(i)
	return bool(pair),pair,other

#print 'one pair',one_pair([1,1,3,4,6],[])

def high_card(vals,suits):
	
	return max(vals)

#print high_card(p1[0],p1[1])

def hand_score(vals,suits):
	
	if royal_flush(vals,suits)[0]: return hand_ranks['royal flush']
	
	elif straight_flush(vals,suits)[0]: return hand_ranks['straight flush']
	
	elif four_kind(vals,suits)[0]: return hand_ranks['four of a kind']

	elif full_house(vals,suits)[0]: return hand_ranks['full house']

	elif flush(vals,suits): return hand_ranks['flush']

	elif straight(vals,suits)[0]: return hand_ranks['straight']

	elif three_kind(vals,suits)[0]: return hand_ranks['three of a kind']

	elif two_pairs(vals,suits)[0]: return hand_ranks['two pairs']

	elif one_pair(vals,suits)[0]: return hand_ranks['one pair']

	else: return hand_ranks['high card']

def main():
	
	player1_wins=0
	player2_wins=0
	
	game=open('p054_poker.txt','r')
	
	for line in game:
		line=line.strip('\n').split()
		p1_cards,p2_cards=hand_format(line[:5]),hand_format(line[5:])
		#print player1_hand
		p1_vals,p1_suits=p1_cards
		p1_vals.sort(reverse=True)
		
		p2_vals,p2_suits=p2_cards
		p2_vals.sort(reverse=True)
		#print p1_vals
		p1_score= hand_score(p1_vals,p1_suits)
		p2_score= hand_score(p2_vals,p2_suits)
		
		if p1_score>p2_score:
			player1_wins+=1
		
		elif p1_score<p2_score:
			player2_wins+=1
		
		elif p1_score==p2_score and p1_score == 100:
			
			def hc_tie(p1,p2):
				
				p1_wins=0
				p2_wins=0
				
				p1_hc=high_card(p1,[11])
				p2_hc=high_card(p2,[11])
				
				if p1_hc>p2_hc: p1_wins +=1
				
				elif p1_hc<p2_hc: p2_wins +=1
				
				elif p1_hc==p2_hc: player_hc_tie(p1[:-1],p2[:-1])
				
				return p1_wins,p2_wins
			
			wins= hc_tie(p1_vals,p2_vals)
			
			player1_wins+= wins[0]
			player2_wins+= wins[1]
		
		elif p1_score==p2_score and p1_score==200:
			
			def pair_tie(p1,p2):
				p1_wins=0
				p2_wins=0
				
				p1_pair=one_pair(p1,[11])
				p2_pair=one_pair(p2,[11])
				
				p1_pv=p1_pair[1]
				p2_pv=p2_pair[1]
				
				p1_other=p1_pair[2]
				p2_other=p2_pair[2]
				
				if p1_pv>p2_pv: p1_wins+=1
				
				elif p1_pv<p2_pv: p2_wins+=1
				
				elif p1_pv==p2_pv:
					
					tie=hc_tie(p1_other,p2_other)
					p1_wins+= tie[0]
					p2_wins+= tie[1]
				
				return p1_wins,p2_wins
			
			wins= pair_tie(p1_vals,p2_vals)
			
			player1_wins+= wins[0]
			player2_wins+= wins[1]
		#if p1_score==10:
		#	p1_hc=high_card(p1_vals,p1_suits)
		
		

	return 'player one wins: %s, player 2 wins: %s, out of %s plays'\
	%(player1_wins,player2_wins,player1_wins+player2_wins)

print main()

print time()-ss


'''
hands = [line.split() for line in open("p054_poker.txt")]
def euler54():
    """
    Medley of Kutta, eske and Paul Crowley's code.
    KW. Diederich added a few corrections for 'real world' poker
    (but unrequired in the problem, it seems):
        - Straight (3,1,2) and Flush (3,1,3) have to be ranked :
                - above three of a kind (3,1,1)
                - below full house (3,2)
        - Ace,2,3,4,5 is also straight according to the rules.
    """
    values = {c: v for v, c in enumerate('23456789TJQKA', start=2)}
    def rank(hand):
        """
        Reduce the hand to a compact form that can be directly compared to another.
        The score (or ranking) of a hand is essentially the count of same cards, in
        descending order - for example three of a kind scores (3,1,1), a double pair
        scores (2,2,1). Full House will score (3,2).
        We attribute (3,1,3) to a Flush, and (3,1,2) to a Straight.
        The next ranking value are the cards values themselves.
        """
        cards, colors = zip(*hand)
        cards = [values[c] for c in cards]
        score, cards = zip(*sorted([(cards.count(c), c) for c in set(cards)], reverse=True))

        # Handle some special cases (flush, straight...)
        if len(cards) == 5:
            flush = (len(set(colors)) == 1)
            if cards == (14,5,4,3,2):  # this is the 'Ace' type of straight
                straight = 1; cards = (5,4,3,2,1)
            else:
                straight = (cards[0]-cards[4] == 4)
            score = (((1,), (3,1,3)), ((3,1,2), (5,)))[straight][flush]
        return (score, cards)

    player1, player2 = slice(0, 5), slice(5, 10)
    return sum((rank(hand[player1]) > rank(hand[player2])) for hand in hands)
print euler54()
'''
