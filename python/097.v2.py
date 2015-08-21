## SOLVED
#
# Project Euler Problem 97
# ========================
# The first known prime found to exceed one million
# digits was discovered in 1999, and is a Mersenne
# prime of the form 2^(6972593)-1; it contains 
# exactly 2,098,960 digits. Subsequently other 
# Mersenne primes, of the form 2^p-1, have been 
# found which contain more digits.
# 
# However, in 2004 there was found a massive
# non-Mersenne prime which contains 2,357,207
# digits: 28433x2^(7830457)+1.
# 
# Find the last ten digits of this prime number.

def reverse(s):
    return s[::-1]

from time import clock
st=clock()

# using 'Successive Squaring' method
# http://www.exploringbinary.com/how-to-find-the-last-digits-of-a-positive-power-of-two/

targetPower=7830457
multiplier=28433

binaryString=bin(targetPower)
binaryString=binaryString[2:] #deletes preceeding '0b'
binaryString=reverse(binaryString)

print 'Splitting target into sum of powers of two'
two=1
powersOfTwo=[]
for bit in binaryString:
    if bit=='1':
        powersOfTwo.append(two)
    elif bit=='0':
        powersOfTwo.append(0)
    two*=2

m=100000000000
listOfTwoTwoMod=[2]

print 'Listing powers of two raised to powers of two mod', m

for i in range(1,len(powersOfTwo)+1):
    item=(listOfTwoTwoMod[i-1]**2)%m
    listOfTwoTwoMod.append(item)

print 'Combining required powers'
t=1
for i in range(len(powersOfTwo)):
    if powersOfTwo[i]!=0:
        t*=listOfTwoTwoMod[i]
        t=t%m

t=((multiplier*t)+1)%(m/10)
print t

fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
