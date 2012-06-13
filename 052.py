# Project Euler Problem 52 #
# ========================
# It can be seen that the number, 125874, and its
# double, 251748, contain exactly the same digits,
# but in a different order.
#
# Find the smallest positive integer, x, such
# that 2x, 3x, 4x, 5x, and 6x, contain the same
# digits.
#

def getDigits(n):
    '''Returns a set of all the digits in n'''
    s=set()
    for digit in str(n):
        s.add(int(digit))
    return s

# start timing
from time import clock
st=clock()


# search
n=1
keepGoing=True

while keepGoing==True:
    n+=1
    if getDigits(n)==getDigits(2*n):
        if getDigits(n)==getDigits(3*n):
            if getDigits(n)==getDigits(4*n):
                if getDigits(n)==getDigits(5*n):
                    if getDigits(n)==getDigits(6*n):
                        print n
                        keepGoing=False
                        # want the first one found

# stop timing
fn=clock()

print 'Time to run '+`(fn-st)`[:4]+'s'
