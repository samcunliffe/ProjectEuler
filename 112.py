## SOLVED
#
# Project Euler Problem 112
# =========================
# Working from left-to-right if no digit is exceeded
# by the digit to its left it is called an
# increasing number; for example, 134468.
#
# Similarly if no digit is exceeded by the digit to
# its right it is called a decreasing number; for
# example, 66420.
#
# We shall call a positive integer that is neither
# increasing nor decreasing a "bouncy" number; for
# example, 155349.
#
# Clearly there cannot be any bouncy numbers below
# one-hundred, but just over half of the numbers
# below one-thousand (525) are bouncy. In fact, the
# least number for which the proportion of bouncy
# numbers first reaches 50% is 538.
#
# Surprisingly, bouncy numbers become more and more
# common and by the time we reach 21780 the
# proportion of bouncy numbers is equal to 90%.
#
# Find the least number for which the proportion of
# bouncy numbers is exactly 99%.

def isBouncy(n):
    s=str(n)
    asc=False
    des=False
    for i in range(1,len(s)):
        if s[i]<s[i-1]:des=True
        elif s[i]>s[i-1]:asc=True

        if asc==True and des==True:
            return True
    return False

from time import clock
st=clock()

print 'Listing'
nums=range(21781)

print 'Mapping'
bncy=map(isBouncy,nums)
n=nums[-1]

bouncyNumbers=bncy.count(True)

print 'Searching Onward'
while 1:

    # calculate percentage of
    # bouncy numbers
    prop=(bouncyNumbers*100)/n

    # break clause
    if prop>=99:
        print n
        break

    # increment stuff if
    # density is not high
    # enough yet
    n+=1
    if isBouncy(n):
        bouncyNumbers+=1

fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
