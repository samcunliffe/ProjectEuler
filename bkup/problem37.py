## SOLVED but works mega-slowly
#
# Project Euler Problem 37
# ========================
# The number 3797 has an interesting property. Being
# prime itself, it is possible to continuously
# remove digits from left to right, and remain prime
# at each stage: 3797, 797, 97, and 7. Similarly we
# can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are
# both truncatable from left to right and right to
# left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be
# truncatable primes.
#


def sieveOfEratosthenes(n):
    l=range(n)
    l[1]=0
    for entry in range(2,len(l)):
        if entry**2 < n:
            for mult in range(entry**2,n,entry):
                if l[mult]!=0:
                    l[mult]=0
    return l

def isEven(n):
    if n%2==0:return True
    else: return False

t=0
count=0

l=[]

from time import clock
st=clock()

print 'Sieving'
primes      =sieveOfEratosthenes(1000000)

# don't need to search thru
# primes bigger than candidate
fewerPrimes =sieveOfEratosthenes(100000)

#remove single digit primes from list
primes=primes[8:]


print 'Searching'
for p in primes:

    s=str(p)

    # check that st/fn digits are prime
    # to save time
    if (int(s[-1]) in [3,7]) and (int(s[0]) in [2,3,5,7]):

        # loop over all possible truncations
        for c in range(2,len(s)):
            if (int(s[-c:]) in fewerPrimes) and (int(s[:c]) in fewerPrimes):
                l.append(0)
            else:
                # not truncatable
                l.append(1)
                exit

        if sum(l)==0:
                t+=p
                print p
                count+=1
        l=[] 

fn=clock()
print ''       
print count
print t
print 'Time to run ',(fn-st)
            
