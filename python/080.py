# Project Euler Problem 80
# ========================
# It is well known that if the square root of a
# natural number is not an integer, then it is
# irrational. The decimal expansion of such square
# roots is infinite without any repeating pattern at
# all.
# 
# The square root of two is 1.41421356237309504880..
# and the digital sum of the first one hundred
# decimal digits is 475.
# 
# For the first one hundred natural numbers, find
# the total of the digital sums of the first one
# hundred decimal digits for all the irrational
# square roots.

from samsPrimeTools import sieveOfEratosthenes
from decimal import *

getcontext().prec = 100

primes=sieveOfEratosthenes(100)

t=0
for p in primes:
    if p!=0:
        s=str(Decimal(p).sqrt())
        s=s[2:]

        for d in s:
            t+=int(d)

print t
