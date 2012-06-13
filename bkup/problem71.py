## SOLVED
#
# Project Euler Problem 71
# ========================
# Consider the fraction, n/d, where n and d are
# positive integers. If n<d and HCF(n,d)=1, it is
# called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for
# d <= 8 in ascending order of size, we get:
#
#                                         ***
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7,
# 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7,
# 7/8
#
# It can be seen that 2/5 is the fraction
# immediately to the left of 3/7.
#
# By listing the set of reduced proper fractions for
# d <= 1,000,000 in ascending order of size, find
# the numerator of the fraction immediately to the
# left of 3/7.



from fractions import *
from time import clock     

## Farey neighbour
#http://en.wikipedia.org/wiki/Farey_sequence

# the first term that appears between a/b and c/d is
#     a+c / b+d
# so for a/b=2/5  c/d=3/7

st=clock()

c=3
d=7

# starting numbers
a=2
b=5
AoverB=Fraction(2,5)
print 'Searching'
while 1:#AoverB.denominator<1000000:
    
    AoverB=Fraction(a+c,b+d)
    if AoverB.denominator>=1000000:
        break
    else:
        a=AoverB.numerator
        b=AoverB.denominator
    
print a

fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
