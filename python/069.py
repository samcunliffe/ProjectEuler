# Project Euler Problem 69
# ========================
# Euler's Totient function, f(n) [sometimes called 
# the phi function], is used to determine the 
# number of numbers less than n which are 
# relatively prime to n. 
#
# For example, as 1, 2, 4, 5, 7, and 8, are all 
# less than nine and relatively prime to nine, 
# f(9)=6.
#
# n 	Relatively Prime 	f(n) 	n/f(n)
# --------------------------------------------
# 2 	1 			1	2
# 3 	1,2 			2	1.5
# 4 	1,3 			2 	2
# 5 	1,2,3,4     		4 	1.25
# 6 	1,5 			2 	3
# 7 	1,2,3,4,5,6 		6	1.1666...
# 8 	1,3,5,7 		4	2
# 9 	1,2,4,5,7,8 		6 	1.5
# 10 	1,3,7,9 		4 	2.5
#
# It can be seen that n=6 produces a maximum n/f(n)
# for n = 10.
#
# Find the value of n <= 1,000,000 for which n/f(n)
# is a maximum.

from fractions import *
from time import clock
from samsPrimeTools import sieveOfEratosthenes
st=clock()

## Smart method using the Euler totent formula
#http://en.wikipedia.org/wiki/Euler%27s_totient_function

# sieve for primes
print 'Sieving'
primes=sieveOfEratosthenes(10000)

# want a product of small primes
n=1
largest=3
bestN=6
print 'Searching'
for i in range(len(primes)):

    if primes[i]!=0:
        n*=primes[i]
        if n>1000000:
            break
        phi=n
        for prime in primes[:i+1]:
            if prime!=0:
                phi*=(1 - Fraction(1,prime))
        if Fraction(n,phi)>largest:
            largest=Fraction(n,phi)
            bestN=n
            
print bestN


fn=clock()
print('Time to run %0.3f seconds' % (fn-st))

## Brute force code, which takes ages!
st=clock()
def f(n):
    f=0
    for m in range(1,n):
        if gcd(n,m) == 1:
            f+=1
    return f

largest=3.0
for n in range(2,1000001):
    if Fraction(n,f(n)) > largest:
        largest=Fraction(n,f(n))
        N=n

print N

fn=clock()
print('Time to run (brute force) %0.3f seconds' % (fn-st))

