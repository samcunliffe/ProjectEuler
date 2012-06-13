# Project Euler Problem 49
# ========================
#
# The arithmetic sequence, 1487, 4817, 8147, in
# which each of the terms increases by 3330, is
# unusual in two ways: (i) each of the three terms
# are prime, and, (ii) each of the 4-digit numbers
# are permutations of one another.
#
# There are no arithmetic sequences made up of three
# 1-, 2-, or 3-digit primes, exhibiting this
# property, but there is one other 4-digit
# increasing sequence.
#
# What 12-digit number do you form by concatenating
# the three terms in this sequence?

from samsPrimeTools import sieveOfEratosthenes

def isPerm(x,y):
    '''Tests that x is a digit permutation of y'''
    from itertools import permutations
    x=str(x)
    y=str(y)
    for p in permutations(x):
        if len(p)==4:            
            z=p[0]+p[1]+p[2]+p[3]
            if y==z:
                return True
    return False

def uniquify(seq):
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]

from time import clock
st=clock()

print 'Sieving'
primes=sieveOfEratosthenes(10000)

print 'Selecing only 4 digit primes'
fourDigitPrimes=primes[1000:10000]

print 'Removing zero entries'
fourDigitPrimes=uniquify(fourDigitPrimes)
fourDigitPrimes.remove(0)
     
print 'Searching for arithmetic sequences'
for a in fourDigitPrimes:
    for b in fourDigitPrimes:
        if a!=b:
            for c in fourDigitPrimes:
                if c!=a and c!=b:
                    
                    if (b-a)==(c-b):
                        if isPerm(a,b):
                            if isPerm(b,c):
                                if isPerm(a,c):
                                    print str(a)+str(b)+str(c)
                                    if str(a)+str(b)+str(c) != '148748178147':
                                        exit
 

fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
