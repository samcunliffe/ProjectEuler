'''
A set of basic functions for finding or
testing prime numbers.
'''

def isPrime(n):
    '''
    Basic prime test by searching for divisors
    '''
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def sieveOfEratosthenesSmall(n):
    '''
    Generates a list of primes upto n
    using the Sieve of Eratosthenes.
    The function returns a list only of
    primes, for example
    [2,3,5,7] and works well for small
    but slowly for large values of n.
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

def eratosthenes(n):
    '''
    Generate a list of primes upto n using the Sieve of Eratosthenes.
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


def EulerSieve(n):
    '''
    Do not use, not implemented correctly.
    '''
    # Create a candidate list within which non-primes will
    # marked as None, noting that only candidates below
    # sqrt(n) need be checked. 
    l = range(n+1)
    fin = int(n**0.5)
 
    # Loop over the candidates, marking out each multiple.
    # If the current candidate is already checked off then
    # continue to the next iteration.
    for i in xrange(2, fin+1):
        if not l[i]:
            continue
 
        l[2*i::i] = [None] * (n//i - 1)
 
    # Filter out non-primes and return the list.
    return [i for i in l[2:] if i]

# sieve of Eratosthenes
def sieve(n):
  primes = range(2,n)
  x = 0
  while primes[x] < n**0.5:
    # remove all multiples of the current prime from primes
    primes = [y for y in primes if y==primes[x] or y%primes[x]]
    x = x+1
  return primes


