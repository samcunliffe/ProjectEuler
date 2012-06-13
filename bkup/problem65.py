## SOLVED
#
# Project Euler Problem 65
# ========================
# ...What is most surprising is that the important
# mathematical constant,
#
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
#
# The first ten terms in the sequence of convergents
# for e are:
# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71,
# 1264/465, 1457/536, ...
# 
# The sum of digits in the numerator of the 10th
# convergent is 1+4+5+7=17.
#
# Find the sum of digits in the numerator of the
# 100th convergent of the continued fraction for e.

#http://en.wikipedia.org/wiki/E_(mathematical_constant)#Representations
from fractions import Fraction

def digitSum(n):
    t=0
    for digit in str(n):
        t+=int(digit)
    return t

def contFrac(l):
    l.reverse()
    prev=Fraction(0,1) # fractional form of zero
    for i in l[:-1]:
        a=i+prev
        prev=Fraction(1,a)
    return prev+l[-1]

# generates the list form of the continued fraction
print 'Finding list form'
eList=[2]
k=1
for i in range(33): #33 since (100-1)/3
    eList.append(1)
    eList.append(2*k)
    eList.append(1)

    k+=1

print 'Evaluating continued fraction from list'
eFrac=contFrac(eList)

print 'Performing digit sum'
print digitSum(eFrac.numerator)


