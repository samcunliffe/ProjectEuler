## SOLVED
#
# Project Euler Problem 41
# ========================
# We shall say that an n-digit number is pandigital
# if it makes use of all the digits 1 to n exactly
# once. For example, 2143 is a 4-digit pandigital
# and is also prime.
#
# What is the largest n-digit pandigital prime that
# exists?
#

def isPrime(n):
    # range starts with 2 and only needs
    # to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

from time import clock
from itertools import permutations

st=clock()


print 'Searching for Pandigitals'
pandigitals=[]

for n in range(2,10):
    for perm in permutations(range(1,n)):

        s=''
        for digit in perm:
            s+=str(digit)
            
        pandigital=int(s)
        
        pandigitals.append(pandigital)

        
print 'Searching Pandigitals for Primes'
primePandigitals=[]

for pandigital in pandigitals:
    if isPrime(pandigital):
        primePandigitals.append(pandigital)

print max(primePandigitals)

fn=clock()
print('Time to run %0.3f seconds' % (fn-st))

