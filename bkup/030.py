## SOLVED
#
# Project Euler Problem 30
# ========================
# Surprisingly there are only three numbers that can
# be written as the sum of fourth powers of their
# digits:
# 
#     1634 = 1**4 + 6**4 + 3**4 + 4**4
#     8208 = 8**4 + 2**4 + 0**4 + 8**4
#     9474 = 9**4 + 4**4 + 7**4 + 4**4
# 
# As 1 = 14 is not a sum it is not included.
# 
# The sum of these numbers is
#     1634 + 8208 + 9474 = 19316.
# 
# Find the sum of all the numbers that can be
# written as the sum of fifth powers of their
# digits.





# for the power 5, the highest value for a digit is
#     9**5 = 59049
# so for 7 digit numbers, the maximum sum would be
#     7*59049 = 413343
# and this is much less than 9999999 so a limit of 1E6
#

def getDigit(n,i):
    '''Returns the ith digit in n'''
    s=str(n)
    return int(s[i])

def digitPowerSum(n,p):
    '''Sums the pth power of each digit in n'''
    return sum((getDigit(n,i)**p for i in range(len(str(n)))))

#start timing code
from time import clock
st=clock()

#search
t=0
for n in range(2,1000000):
    if n==digitPowerSum(n,5):
        print n
        t+=n

#stop timing
fn=clock()

#report
print '\nThe sum of these is ',t
print 'Time to run '+`fn-st`+'s'
