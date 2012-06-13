## SOLVED

# How many numbers below fifty million can be expressed as the 
# sum of a prime square, prime cube, and prime fourth power?

#  http://projecteuler.net/problem=87


from time import clock
from samsPrimeTools import sieveOfEratosthenes

# start timer
st=clock()

# sieve for primes up to sqrt(50m)
primes=sieveOfEratosthenes(7072)

# remove zeroes
for z in range(primes.count(0)):
  primes.remove(0)

# set object will not contain
# duplicated entries
S=set()

# limit is fourth root of 50m
# this won't BE 85 since the
# zeroes have been removed
for f in primes[:85]:
  if f<85:

    # limit is cube root of 50m
    for c in primes[:369]:
      if c<369:

        for s in primes:

          t = s**2 + c**3 + f**4
          if t< 50*(10**6) : S.add(t)

# report
print len(S)

# stop timer
fn=clock()
print 'Time to run: '+str(fn-st)+' sec'
