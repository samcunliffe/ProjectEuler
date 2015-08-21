## SOLVED
#
# Project Euler Problem 27
# ========================
# Euler published the remarkable quadratic formula:
# 
#       n**2 + n + 41
#
# It turns out that the formula will produce 40
# primes for the consecutive values n = 0 to 39.
# However, when n = 40,
#
#       40**2 + 40 + 41 = 40(40 + 1) + 41
#
# is divisible by 41, and certainly when n = 41,
#
#       41**2 + 41 + 41
#
# is clearly divisible by 41.
# 
# Using computers, the incredible formula
#
#       n**2 - 79n+ 1601
#
# was discovered, which produces 80 primes
# for the consecutive values n = 0 to 79. The
# product of the coefficients, -79 and 1601, is
# -126479.
# 
# Considering quadratics of the form:
# 
#       n**2 + an + b,
#
#       where |a| < 1000 and |b| < 1000
# 
# Find the product of the coefficients, a and b, for
# the quadratic expression that produces the maximum
# number of primes for consecutive values of n,
# starting with n = 0.
#



def isPrime(n):
    '''
    Tests for primality by dividing
    by sucessive factors until the
    number itself is reached
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


def sieveOfEratosthenes(n):
    '''
    Generates a list of primes upto
    but not including the value of n
    using the famous and instinctive
    Sieve of Eratosthenes method
    '''
    #generate a list to be sieved
    l=range(2,n)

    #remove each 'prime times table'
    #from the list
    for entry in l:
        if entry**2 < n:
            #start at the square since all smaller
            #multiples have already been sieved
            for mult in range(entry**2,n,entry):
                if mult in l:
                    l.remove(mult)
    return l

#
# if the prime-generating quadratic is of the form
#           n**2 + an + b == f(n)
#
# then b must be prime so that f(0) is prime
#

print 'Generating all primes under 10 000'
primes=sieveOfEratosthenes(10000)

#
# also, f(1)=1+a+b must be a prime (call it p)
#           a=p-(1+b)
#

A=0
B=0     #will hold the running optimum set of values
C=40


print 'Starting search loop'
for b in primes:
    if b<1000:
        for a in [(p-(1+b)) for p in primes]:
            if abs(a)<1000:
                def f(n):
                    return (n**2) + (a*n) + b
                
                i=0
                while isPrime(f(i)):
                    #c+=1
                    i+=1

                if (i+1)>C:  # i+1 accounts for the zero
                    C=(i+1)
                    A=a
                    B=b

print 'Highest number of primes achieved is ',C
print ' with coefficients a=',A
print '               and b=',B
print 'So ab=',(A*B)

