## SOLVED but very slow
#
# Project Euler Problem 73
# ========================
# Consider the fraction, n/d, where n and d are
# positive integers. If n<d and HCF(n,d)=1, it is
# called a reduced proper fraction.
# 
# If we list the set of reduced proper fractions for
# d <= 8 in ascending order of size, we get:
# 
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7,
# 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7,
# 7/8
#
# It can be seen that there are 3 fractions between
# 1/3 and 1/2.
#
# How many fractions lie between 1/3 and 1/2 in the
# sorted set of reduced proper fractions for
# d <= 12,000?
#
# Note: The upper limit has been changed recently.


from fractions import *
from math import floor
from time import clock     

## Farey neighbour and Next term
#http://en.wikipedia.org/wiki/Farey_sequence

# To calculate the next term in the Farey sequence
# one needs the two preceeding terms. Using the
# code from problem71.py we can calculate the term
# to the left of 1/3 so will be able to calculate
# and count next terms until I reach 1/2

st=clock()

n=12000 # new denom

c=1
d=3

# starting numbers
a=2
b=7
AoverB=Fraction(2,5)
while 1:
    
    AoverB=Fraction(a+c,b+d)
    if AoverB.denominator<=n:
        a=AoverB.numerator
        b=AoverB.denominator
    else:
        break
        
AoverB=Fraction(a-c,b-d)
a=AoverB.numerator
b=AoverB.denominator
# this is the fraction left of 1/3 so calculate
# next terms p/q
#http://en.wikipedia.org/wiki/Farey_sequence#Next_term

count=0
while 1:
    p=int(  (floor((n+b)/d)*c)-a  )
    q=int(  (floor((n+b)/d)*d)-b  )
    if Fraction(p,q)<Fraction(1,2):
        count+=1
        
        a=c
        b=d

        c=p
        d=q
    else:
        break

print count
fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
