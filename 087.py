#  Project Euler Problem 87
#  ========================

#  The smallest number expressible as the sum of a prime square,
#  prime cube, and prime fourth power is 28. In fact, there are
#  exactly four numbers below fifty that can be expressed in such a
#  way:

#  28 = 2**2 + 2**3 + 2**4
#  33 = 3**2 + 2**3 + 2**4
#  49 = 5**2 + 2**3 + 2**4
#  47 = 2**2 + 3**3 + 2**4

#  How many numbers below fifty million can be expressed as the sum
#  of a prime square, prime cube, and prime fourth power?

#  ==============================================================

from samsPrimeTools import sieveOfEratosthenes

#upper limit is the square root of fifty million
upper= int(5e7**(0.5))+1

print 'Sieving primes'
primes=sieveOfEratosthenes(upper)

print 'Removing zeros'
for z in range(primes.count(0)):
  primes.remove(0)

print primes
print 'Searching'

s=set()
for a in primes:
  for b in primes:
    for c in primes:
      t=(a**2) + (b**3) + (c**4)
      if t<50:s.add(t)

print len(s)
print s
