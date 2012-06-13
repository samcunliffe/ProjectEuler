## SOLVED
#
# Project Euler Problem 46
# ========================
# 
# It was proposed by Christian Goldbach that every
# odd composite number can be written as the sum of
# a prime and twice a square.
# 
#                9 =  7 + 2 x 1**2
#               15 =  7 + 2 x 2**2
#               21 =  3 + 2 x 3**2
#               25 =  7 + 2 x 3**2
#               27 = 19 + 2 x 2**2
#               33 = 31 + 2 x 1**2
# 
# It turns out that the conjecture was false.
# 
# What is the smallest odd composite that cannot be
# written as the sum of a prime and twice a square?

from math import sqrt
from samsPrimeTools import sieveOfEratosthenes
from time import clock

st=clock()

def primeAndTwiceSq(n):
    for sumPart in sieveOfEratosthenes(n):
        twiceSquare = n- sumPart
        if twiceSquare%2==0:
            if sqrt(twiceSquare/2)==int(sqrt(twiceSquare/2)):
                return [sumPart,2,twiceSquare/2]
    return[n,-1,-1]



print 'Sieving'
primes=sieveOfEratosthenes(10000)

print 'Finding odd composites'
oddComposites=[]
for i in range(2,len(primes)):
    if i%2 != 0:
        if primes[i]==0:
            oddComposites.append(i)

print 'Searching'
for oc in oddComposites:
    if primeAndTwiceSq(oc)[1]==-1:
        print oc
        exit


fn=clock()
print('Time to run %0.3f seconds' % (fn-st))

