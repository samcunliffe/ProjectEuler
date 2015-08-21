## SOLVED
#
# Project Euler Problem 26
# ========================
# A unit fraction contains 1 in the numerator. The
# decimal representation of the unit fractions with
# denominators 2 to 10 are given:
# 
#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1
# 
# Where 0.1(6) means 0.166666..., and has a 1-digit
# recurring cycle. It can be seen that 1/7 has a
# 6-digit recurring cycle.
# 
# Find the value of d < 1000 for which 1/d contains
# the longest recurring cycle in its decimal
# fraction part.
#


# get the super useful decimal module
from decimal import *

# set number of dp to keep and search upto
upBound = 1000
getcontext().prec = (2*upBound)+1

# checks the unit fraction for cycles
def checkForRepetition(n):
    s=str(n)
    s=s[2:] #deletes the preceding "0."
    mx=int(len(s)/2)
    for c in range(2,mx):
        if s[0:c]==s[c:2*c]: return s[0:c]
    return ''

# start stopwatch
from time import clock
st=clock()

# current longest cycle
C=1

# longest cycle generating denom
D=7

# perform search
print 'Searching'
for d in range(7,1000):
    frac=Decimal(1)/Decimal(d)
    ch = checkForRepetition(frac)

    if len(ch)>C:
        C=len(ch)
        D=d
        #print '   1/'+`D`+' gives cycle of len '+`C`


# stop stopwatch              
fn=clock()

print D
print('Time to run: %.2f seconds' % (fn-st))

