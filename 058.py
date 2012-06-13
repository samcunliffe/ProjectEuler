## SOLVED  34sec
#
# Project Euler Problem 58
# ========================
# Starting with 1 and spiralling anticlockwise in 
# the following way, a square spiral with side 
# length 7 is formed.
#
#           37 36 35 34 33 32 31
#           38 17 16 15 14 13 30
#           39 18  5  4  3 12 29
#           40 19  6  1  2 11 28
#           41 20  7  8  9 10 27
#           42 21 22 23 24 25 26
#           43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares
# lie along the bottom right diagonal, but what is
# more interesting is that 8 out of the 13 numbers
# lying along both diagonals are prime; that is, a
# ratio of 8/13 ˜ 62%.
#
# If one complete new layer is wrapped around the 
# spiral above, a square spiral with side length 9 
# will be formed. If this process is continued, 
# what is the side length of the square spiral for
# which the ratio of primes along both diagonals 
# first falls below 10%?

from samsPrimeTools import isPrime
from time import clock
start=clock()

def wrapSpiralCorners(n):
    l=[1]
    odd=2
    st=0
    for i in range(n):
        l.append(l[st]+odd)
        l.append(l[st]+odd+odd)
        l.append(l[st]+odd+odd+odd)
        l.append(l[st]+odd+odd+odd+odd)
        st+=4
        odd+=2
    return l

#start off the ratio any number above 10%
ratio=100.

#start off the spiral
spiral=[1]
odd=2
st=0

#a list for isPrime vals
prime=[False]

while ratio > 10 :

    #wrap a layer onto the spiral
    spiral.append(spiral[st]+odd)
    spiral.append(spiral[st]+odd+odd)
    spiral.append(spiral[st]+odd+odd+odd)
    spiral.append(spiral[st]+odd+odd+odd+odd)

    #check the last four numbers for
    #primality
    prime+=map(isPrime,spiral[(st+1):])
    
    #recalculate the ratio
    ratio=((prime[1:].count(True))*100.)/(len(prime[1:]))

    #increment to wrap the next layer
    st+=4
    odd+=2

# le report
print spiral[-1]-spiral[-2]+1
fn=clock()
print('Time to run %0.3f seconds' % (fn-start))
