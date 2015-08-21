## SOLVED But very slow!
#
# Project Euler Problem 35
# ========================
# The number, 197, is called a circular prime
# because all rotations of the digits: 197, 971, and
# 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5,
# 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one
# million?
#



# ===functions===

def list2int(l):
    '''
    Takes a list of seperate digits
    and returns the integer that is the
    sequence of the digits
    '''
    s=0
    for i in l:
        s+=int(i)
    return s



def isPrime(n):
    '''
    Tests for primality trivial division
    '''
    #primes are not negative or zero
    if n<=0: return False

    #1 is not prime
    elif n==1: return False
    
    #2 is prime
    elif n==2: return True

    else:
        #if 2 is a factor, n is
        #even and non prime
        if n%2==0: return False

        #otherwise, n will have
        #only odd factors...
        else:
            for d in range(3,n,+2):
                if n%d==0: return False

        #...or be an odd prime
        return True


def sieveOfEratosthenesBig(n):
    '''
    Generates a list of primes upto
    but not including the value of n
    using the famous and instinctive
    Sieve of Eratosthenes method.
    For a large limit this function
    is faster. It zeroes the non-primes
    rather than remove.
    '''
    #generate a list to be sieved, list from
    #zero so that the index matches the value
    #which makes life simpler
    l=range(n)

    #manually zero out one, l[0] is already zero 
    l[1]=0

    #remove each 'prime times table'
    #from the list
    for entry in range(2,len(l)):
            
        # check that the square is still in range
        if entry**2 < n:
            
            #start removing multiples from the square
            #of the prime since all smaller multiples
            #have already been sieved
            for mult in range(entry**2,n,entry):
                
                #Eratosthenes' sieve is over defined,
                #previous iteration may have removed
                #value already so check the entry is
                #not already zeroed
                #(makes miniscule time saving)
                if l[mult]!=0:

                    #zero the non-prime
                    l[mult]=0
                    
    return l

# ===Code===


# time running of code
from time import clock

st=clock()
print 'Listing all primes under 1E6'
primes=sieveOfEratosthenesBig(1000000)

# test for circular prime
def isCircularPrime(n):
    s=str(n)
    if len(s)==1:return True
    else:
        for p in range(1,len(s)):
            u=s[:p]
            v=s[p:]
            #if not isPrime(int(v+u)):
            if int(v+u) in primes:
                return True
    return False


print 'Searching for and counting circular primes'
count=0
for n in primes:
    if n!=0:
        if isCircularPrime(n):
            print n
            count+=1

fn=clock()

print 'Total number found is ',count

print 'Time to execute '+`fn-st`+'ms'

