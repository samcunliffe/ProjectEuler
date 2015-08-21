from fractions import Fraction

def primeFactors(n):
    factor=2
    N=n
    l=[]
    while 1:
        if N%factor==0:
            N/=factor
            l.append(factor)
        if N%factor!=0:
            factor+=1
        if N==1:
            break
    return l

def distinctPrimeFactors(n):
    return set(primeFactors(n))
             
def phi(n):
    '''
    Calculates the Euler totent function
    '''
    phi=n
    for p in distinctPrimeFactors(n):
        phi*=(1-Fraction(1,p))
    return int(phi)


# Sequence length
# ===============
# The Farey sequence of order n contains all of the
# members of the Farey sequences of lower orders. In
# particular Fn contains all of the members of Fn−1,
# and also contains an additional fraction for each
# number that is less than n and coprime to n. Thus
# F6 consists of F5 together with the fractions 1⁄6
# and 5/6. The middle term of a Farey sequence Fn is
# always 1/2, for n > 1.
# 
# From this, we can relate the lengths of Fn and
# Fn−1 using Euler's totient function phi(n) :
# 
#    |F_n| = |F_{n-1}| + \varphi(n).
#  
# Using the fact that |F1| = 2, we can derive an
# expression for the length of Fn :
# 
#     |F_n| = 1 + \sum_{m=1}^n \varphi(m). 

n=1000000
Fn=1
for m in range(1,n+1):
    Fn+=phi(m)

print Fn-2
