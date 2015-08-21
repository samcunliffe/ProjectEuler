#SOLVED    but v.slow Time to run 173.997 seconds
#
# Project Euler Problem 60
# ========================
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
# and concatenating them in any order the result will always be prime. For 
# example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four 
# primes, 792, represents the lowest sum for a set of four primes with this 
# property.
#
# Find the lowest sum for a set of five primes for which any two primes 
# concatenate to produce another prime.
#

#start timer
from time import clock
st=clock()

# add prime module
from sys import path; path.append("modules")

from samsPrimeTools import isPrime, sieveOfEratosthenes

def pairConcPrime(x,y):
    s=str(x)
    t=str(y)
    if isPrime( int(s+t) ) and isPrime( int(t+s) ):
        return True#y
    else:
        return False#0

print 'Sieving'
primes=sieveOfEratosthenes(10000)
for p in primes:
    if p==0:
        primes.remove(0)


b=False
print 'Searching'
def search():
    for a in primes:
        for b in primes:
            if pairConcPrime(a,b):
                for c in primes:
                    if pairConcPrime(a,c) and pairConcPrime(b,c):
                        for d in primes:
                            if pairConcPrime(a,d) \
                               and pairConcPrime(b,d) \
                               and pairConcPrime(c,d):

                                for e in primes:
                                    if pairConcPrime(a,e) \
                                       and pairConcPrime(b,e) \
                                       and pairConcPrime(c,e) \
                                       and pairConcPrime(e,d):

                                        print [a,b,c,d,e]
                                        print sum([a,b,c,d,e])
                                        return
search()

#stop timer
fn=clock()
print('Time to run %0.3f seconds' % (fn-st))


