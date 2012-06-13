## SOLVED
#
# Project Euler Problem 32
# ========================
# We shall say that an n-digit number is pandigital
# if it makes use of all the digits 1 to n exactly
# once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital.
# 
# The product 7254 is unusual, as the identity,
#     39 x 186 = 7254,
# containing multiplicand, multiplier, and product
# is 1 through 9 pandigital.
# 
# Find the sum of all products whose
# multiplicand/multiplier/product identity can be
# written as a 1 through 9 pandigital. HINT: Some
# products can be obtained in more than one way so
# be sure to only include it once in your sum.
#

def isPandigital(s):
    '''
    Checks if a string contains
    all digits up to its lenghth
    '''

    u=''.join(sorted(s))
    v=''
    for i in range(1,len(s)+1):
        v+=str(i)
    if u==v: return True
    else:    return False



# start timer
from time import clock
st=clock()

# search
pandigitals=set()

for a in range(1,10000):
    for b in range(1,10000):
        c=a*b
        if len(`a`+`b`+`c`)==9:
            if isPandigital(`a`+`b`+`c`):
                pandigitals.add(c)
            
print sum(pandigitals)

# stop timer
fn=clock
print('Time to run %0.3f s' % fn-st)
