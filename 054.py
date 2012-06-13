## SOLVED   --boring
#
# Project Euler Problem 54
# =========================
# In the card game poker, a hand consists of five
# cards and are ranked, from lowest to highest, in
# the following way:
#
#     * High Card: Highest value card.
#     * One Pair: Two cards of the same value.
#     * Two Pairs: Two different pairs.
#     * Three of a Kind: Three cards of the same
#       value.
#     * Straight: All cards are consecutive values.
#     * Flush: All cards of the same suit.
#     * Full House: Three of a kind and a pair.
#     * Four of a Kind: Four cards of the same
#       value.
#     * Straight Flush: All cards are consecutive
#       values of same suit.
#     * Royal Flush: Ten, Jack, Queen, King, Ace, in
#       same suit.
#
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King,
# Ace.
#
# If two players have the same ranked hands then the
# rank made up of the highest value wins; for
# example, a pair of eights beats a pair of fives
# (see example 1 below). But if two ranks tie, for
# example, both players have a pair of queens, then
# highest cards in each hand are compared (see
# example 4 below); if the highest cards tie then
# the next highest cards are compared, and so on.
#
# The file, poker.txt, contains one-thousand random
# hands dealt to two players. Each line of the file
# contains ten cards (separated by a single space):
# the first five are Player 1's cards and the last
# five are Player 2's cards. You can assume that all
# hands are valid (no invalid characters or repeated
# cards), each player's hand is in no specific
# order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?


def valueOf(card):
    if   card[0]=='A': return 14
    elif card[0]=='K': return 13
    elif card[0]=='Q': return 12
    elif card[0]=='J': return 11
    elif card[0]=='T': return 10
    else:              return int(card[0])

def suitOf(card):
    return card[1]

def highestCardIn(hand):
    highest=0
    for card in hand:
        if valueOf(card) > highest:
            highest=valueOf(card)
    return highest

# which player: a==player 1 or b==player 2
# has the highest card out of the two hands
def highCard(a,b):
    if   highestCardIn(a) > highestCardIn(b): return 1
    elif highestCardIn(a) < highestCardIn(b): return 2
    else:       return 0 # draw


def pairIn(hand):
    '''
    Returns the value of the
    highest pair in the hand.
    If the hand contains no
    pairs, or a three/four of
    a kind, zero is returned.
    '''
    vals=map(valueOf,hand)
    for i in range(14,0,-1):
        if vals.count(i)==2:
            return i
    return 0

def threeOfAKindIn(hand):
    '''
    Returns the value of any
    three of a kind in the
    hand.
    If the hand contains
    pairs, or a four of a 
    kind, zero is returned.
    '''
    vals=map(valueOf,hand)
    for i in range(14,0,-1):
        if vals.count(i)==3:
            return i
    return 0

def fourOfAKindIn(hand):
    '''
    Returns the value of any
    four of a kind in the
    hand.
    If the hand contains
    pairs, or a three of a 
    kind, zero is returned.
    '''
    vals=map(valueOf,hand)
    for i in range(14,0,-1):
        if vals.count(i)==4:
            return i
    return 0

# which has the highest value pair of cards
def onePair(a,b):
    if pairIn(a) > pairIn(b):
        return 1
    elif pairIn(a) < pairIn(b):
        return 2
    else:
        return 0
    
def twoPairIn(hand):
    '''
    Returns the value of the
    highest pair in the hand.
    Ensuring that there are
    two pairs.
    If the hand contains 0 or 1
    pair, or a three/four of
    a kind, zero is returned.
    '''
    vals=map(valueOf,hand)
    for i in range(14,0,-1):
        if vals.count(i)==2:
            for j in range(i-1,0,-1):
                if vals.count(j)==2:
                    return [i,j]
    return [0,0]

def twoPair(a,b):
    if twoPairIn(a) > twoPairIn(b):
        return 1
    elif twoPairIn(a) < twoPairIn(b):
        return 2
    else:
        return 0

def threeOfAKind(a,b):
    if threeOfAKindIn(a) > threeOfAKindIn(b):
        return 1
    elif threeOfAKindIn(a) < threeOfAKindIn(b):
        return 2
    else:
        return 0

def straightIn(hand):### does not take ACE=1 and 14 into account
    vals=map(valueOf,hand)
    vals.sort()
    shouldBe=range(min(vals),min(vals)+5)
    if vals==shouldBe:
        return max(vals)
    else:
        return 0
##    for card in vals:
##        if card!=shouldBe:
##            return 0
##        shouldBe+=1
##    return max(vals)
    

def straight(a,b):
    if straightIn(a) > straightIn(b):
        return 1
    elif straightIn(a) < straightIn(b):
        return 2
    else:
        return 0

def flushIn(hand):
    suits=map(suitOf,hand)
    if suits==['S']*5 or suits==['D']*5\
       or suits==['C']*5 or suits==['H']*5:
        return max(map(valueOf,hand))
    return 0

def flush(a,b):
    if flushIn(a) > flushIn(b):
        return 1
    elif flushIn(a) < flushIn(b):
        return 2
    else:
        return 0

def fullHouseIn(hand):
    if threeOfAKindIn(hand) != 0 and pairIn(hand) != 0:
        return [threeOfAKindIn(hand),pairIn(hand)]
    else:
        return [0,0]

def fullHouse(a,b):
    if fullHouseIn(a) > fullHouseIn(b):
        return 1
    elif fullHouseIn(a) < fullHouseIn(b):
        return 2
    else:
        return 0

def fourOfAKind(a,b):
    if fourOfAKindIn(a) > fourOfAKindIn(b):
        return 1
    elif fourOfAKindIn(a) < fourOfAKindIn(b):
        return 2
    else:
        return 0

def straightFlushIn(hand):
    if straightIn(hand)!=0 and flushIn(hand)!=0:
        if straightIn(hand)!=flushIn(hand):
            print 'St Flush vals dont match'
        return straightIn(hand)
    else:
        return 0

def straightFlush(a,b):
    if straightFlushIn(a) > straightFlushIn(b):
        return 1
    elif straightFlushIn(a) < straightFlushIn(b):
        return 2
    else:
        return 0

## Doesn't need implementing!
## This is just a winning straight flush
    
##def royalFlush(a,b):
##    print 'Under development'
##    return a


def poker(a,b):
    if   straightFlush(a,b)==1: return 1
    elif straightFlush(a,b)==2: return 2
    else:
        if   fourOfAKind(a,b)==1: return 1
        elif fourOfAKind(a,b)==2: return 2
        else:
            if   fullHouse(a,b)==1: return 1
            elif fullHouse(a,b)==2: return 2
            else:
                if   flush(a,b)==1: return 1
                elif flush(a,b)==2: return 2
                else:
                    if   straight(a,b)==1: return 1
                    elif straight(a,b)==2: return 2
                    else:
                        if   threeOfAKind(a,b)==1: return 1
                        elif threeOfAKind(a,b)==2: return 2
                        else:
                            if   twoPair(a,b)==1: return 1
                            elif twoPair(a,b)==2: return 2
                            else:
                                if   onePair(a,b)==1: return 1
                                elif onePair(a,b)==2: return 2
                                else:
                                    if   highCard(a,b)==1: return 1
                                    elif highCard(a,b)==2: return 2
                                    else:
                                        print 'No winner recorded'
                                        print a,b
                                        return 0


game=open('problem54data.txt')

t=0
for line in game:
    a=[line[ 0: 2],line[ 3: 5],line[ 6: 8],line[ 9:11],line[12:14]]
    b=[line[15:17],line[18:20],line[21:23],line[24:26],line[27:29]]

    if poker(a,b)==1:
        t+=1
print t 
