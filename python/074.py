## SOLVED
#
# Project Euler Problem 74
# ========================
# The number 145 is well known for the property that
# the sum of the factorial of its digits is equal to
# 145:
# 
# 1! + 4! + 5! = 1 + 24 + 120 = 145
# 
# Perhaps less well known is 169, in that it
# produces the longest chain of numbers that link
# back to 169; it turns out that there are only
# three such loops that exist:
# 
# 169 ; 363601 ; 1454 ; 169
# 871 ; 45361 ; 871
# 872 ; 45362 ; 872
# 
# It is not difficult to prove that EVERY starting
# number will eventually get stuck in a loop. For
# example,
# 
# 69 ; 363600 ; 1454 ; 169 ; 363601 (... 1454)
# 78 ; 45360 ; 871 ; 45361 (... 871)
# 540 ; 145 (... 145)
# 
# Starting with 69 produces a chain of five
# non-repeating terms, but the longest non-repeating
# chain with a starting number below one million is
# sixty terms.
# 
# How many chains, with a starting number below one
# million, contain exactly sixty non-repeating
# terms?


# start timer
from time import clock
st=clock()

# calculate the factorials of all
# the digits 0-9 (only do this once)
from math import factorial
f=map(factorial,range(10))


# define the digit factorial sum function
# n.b. uses the list of factorials above
def digitsFactorial(n):
    return sum(f[int(d)] for d in str(n))


# the limit of the search
mil=1000000

# will store the chain lengths
# for each number 0 to 1million
counts=[]


print 'Searching'

for i in range(mil):

    n=i
    count=0
    chain=[]
    
    while n not in chain:

        # might have already counted the
        # chain length for this n
        if n < len(counts):
            count+=counts[n]
            break
        
        # otherwise add n to the chain
        # and find the next term, increase
        # the count
        else:
            chain.append(n)
            n=digitsFactorial(n)
            count+=1
        
    # add the non repeating chain
    # length to the list of counts    
    counts.append(count)

print counts.count(60)

# stop timer
fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
