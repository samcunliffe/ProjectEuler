## SOLVED but takes ages!
## isPrime and (p in primes) are slow for large n
#
# Problem Euler Problem 50
# ========================
# The prime 41, can be written as the sum of six
# consecutive primes:
#
#         41 = 2 + 3 + 5 + 7 + 11 + 13
# 
# This is the longest sum of consecutive primes that
# adds to a prime below one-hundred.
# 
# The longest sum of consecutive primes below
# one-thousand that adds to a prime, contains 21
# terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as
# the sum of the most consecutive primes?

from samsPrimeTools import sieveOfEratosthenes
from samsPrimeTools import isPrime
from time import clock

st=clock()

print 'Sieving'
primes=sieveOfEratosthenes(1000000)

print 'Searching'

longest=21
prime=953

for startPoint in range(len(primes)):
    i=startPoint
    t=0
    count=0
    while t<1000000 and i<len(primes):
        t+=primes[i]
        i+=1
        if primes[i]!=0:
            count+=1
        if (count>longest):
            if (t in primes):
                longest=count
                prime=t
                print count
                print t
                print ''

print prime

fn=clock()
print('Time to run %0.3f seconds' % (fn-st))

