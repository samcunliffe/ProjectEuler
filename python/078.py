## SOLVED but takes ages

# Project Euler Problem 78
# ========================
#	Let p(n) represent the number of different ways in which n coins
#	can be separated into piles. For example, five coins can
#	separated into piles in exactly seven different ways, so p(5)=7.

#    OOOOO
#    OOOO   O
#    OOO   OO
#    OOO   O   O
#    OO   OO   O
#    OO   O   O   O
#    O   O   O   O   O

# Find the least value of n for which p(n) is divisible by one
# million.

# =======================

# This is the integer partition function but I don't just want to
# calculate one term (as in problems 31 & 76), I want the whole 
# sequence.

# Can use Euler's recurrence relation (equation 11 @
# http://mathworld.wolfram.com/PartitionFunctionP.html)

# p(n) = p(n-1) + p(n-2) - p(n-5)- p(n-7) + p(n-12) + p(n-15)...

# Which is a finite sum since p(0)=1 and p(x<0)=0.
# The sequence of subtracted numbers are the generalized
# pentagonal numbers: 1, 2, 5, 7, 12, 15, 22, 26

# start timer
from time import clock
st=clock()

# initialise
n=0
p=[1]
seq=[0,1]
genPent=[0,1]

# while p(n) not divisible by 1million
while (p[n]%1000000) != 0:

  n+=1

  # if n is larger than the number 
  # of precalculated generalized 
  # pentagonal numbers, then need
  # to calculate more
  while n >= len(genPent):

    # add term to the generator sequence
    if seq[-1] < 0:
      seq.append( ((-1)*seq[-1])+1 )
    else:
      seq.append( (-1)*seq[-1] )

    # add term to the generalized pentagonal sequence
    x=seq[-1]    
    genPent.append( ((3*x*x)-x)/2 )


  # now calculate the partition function
  # for n as a sum over the terms in
  # Euler's recurrence relation
  s=0
  for k in range(1,n+1):

    sign=(-1)**(int((k-1)/2))

    if (n-genPent[k]) >= 0 :
      s+=sign*p[n-genPent[k]]
 
  p.append(s)
 
#print p

fn=clock()

print n
print p[n]
print p[n]%1000000
print ''

print 'Time to run = '+str(fn-st)+' sec'

#
