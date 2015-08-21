## SOLVED
#
# Project Euler Problem 34
# ========================
# 145 is a curious number, as
#
#    1! + 4! +  5!
#  =  1 + 24 + 120
#  = 145.
# 
# Find the sum of all numbers which are equal to the
# sum of the factorial of their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are
# not included.
#

from math import factorial

def sumOfFactorialOfDigits(n):
    s=str(n)
    t=0
    for digit in range(0,len(s)):
        t+=factorial( int(s[digit]) )
    return t

t=0
for i in range(10,9999999):
    if sumOfFactorialOfDigits(i)==i:
        print i
        t+=i

print t

#
# using 9 999 999 as the upper limit as 9!=362 880
#      7*9!=2 540 160
#
