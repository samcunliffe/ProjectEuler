## SOLVED
#
# Project Euler Problem 63
# ========================
# The 5-digit number, 16807=7**5, is also a fifth
# power. Similarly, the 9-digit number,
# 134217728=8**9, is a ninth power.
#
# How many n-digit positive integers exist which are
# also an nth power?

from time import clock
st=clock()

t=0
# upper limit set by 9**1000 which has 944 digits
for power in range(1,1000):
    for base in [1,2,3,4,5,6,7,8,9]:
        if power==len(str(base**power)):
            t+=1

print t
fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
