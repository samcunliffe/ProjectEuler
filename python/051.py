# Project Euler Problem 51
# ========================
# By replacing the 1st digit of *3, it turns out
# that six of the nine possible values: 13, 23, 43,
# 53, 73, and 83, are all prime.
# 
# By replacing the 3rd and 4th digits of 56**3 with
# the same digit, this 5-digit number is the first
# example having seven primes among the ten
# generated numbers, yielding the family: 56003,
# 56113, 56333, 56443, 56663, 56773, and 56993.
# Consequently 56003, being the first member of this
# family, is the smallest prime with this property.
# 
# Find the smallest prime which, by replacing part
# of the number (not necessarily adjacent digits)
# with the same digit, is part of an eight prime
# value family.

from samsPrimeTools import isPrime,sieveOfEratosthenes
from time import clock
from string import replace

st=clock()

def isEightFamily(prime, repDig):
    p=str(prime)
    rd=str(repDig)
    c=0
    for digit in '0123456789':
        n=int( replace(p,rd,digit) )
        if isPrime(n) and n>10000:
            c+=1
            if c==8:
                return True
    return False

        
print 'Sieving'
primes=sieveOfEratosthenes(1000000)

print 'Searching'
threeRepDigits=[]
for prime in primes:

        s=str(prime)
        for d in '012':
            if (s.count(d)==3):
                if isEightFamily(prime,d):
                    print prime

fn=clock()
print('Time to run %0.3f seconds' % (fn-st))

