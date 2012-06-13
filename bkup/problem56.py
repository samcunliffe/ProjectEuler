## SOLVED brute force with ~2sec
#
# Project Euler Problem 56
# ========================
#
# A googol (10**100) is a massive number: one 
# followed by one-hundred zeros; 100**100 is almost
# unimaginably large: one followed by two-hundred
# zeros. Despite their size, the sum of the digits
# in each number is only 1.
#
# Considering natural numbers of the form, a**b, 
# where a, b < 100, what is the maximum digital
# sum?

from time import clock
st=clock()

def digitSum(n):
    '''Simple digit sum function for small numbers'''
    t=0
    for s in str(n):
        t+=int(s)
    return t

print 'Brute force search'
D=0
for a in range(100):
    for b in range(100):
        d=digitSum(a**b)
        if d > D:
            D=d
print D

fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
