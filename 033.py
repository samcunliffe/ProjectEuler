## SOLVED
#
# Project Euler Problem 33
# ========================
#
# The fraction 49/98 is a curious fraction, as an
# inexperienced mathematician in attempting to
# simplify it may incorrectly believe that 49/98 =
# 4/8, which is correct, is obtained by cancelling
# the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to
# be trivial examples.
# 
# There are exactly four non-trivial examples of
# this type of fraction, less than one in value, and
# containing two digits in the numerator and
# denominator.
# 
# If the product of these four fractions is given in
# its lowest common terms, find the value of the
# denominator.



from time import clock
from fractions import Fraction

st=clock()

count=0
prod=1    

while count < 4:
    
    for n in range(10,100):
        for d in range(n+1,100):

            # exclude trivials
            if n%10!=0 and d%10!=0 :
                
                N=str(n)
                D=str(d)

                if ( N[0]==D[0] or N[1]==D[0] \
                     or N[0]==D[1] or N[1]==D[1]):
                    v=Fraction(n,d)

                    if N[0]==D[0]:
                        w=Fraction(N[1]+'/'+D[1])
                        if v==w:
                            count+=1
                            prod*=w

                    if N[1]==D[0]:
                        w=Fraction(N[0]+'/'+D[1])
                        if v==w:
                            count+=1
                            prod*=w

                    if N[0]==D[1]:
                        w=Fraction(N[1]+'/'+D[0])
                        if v==w:
                            count+=1
                            prod*=w

                    if N[1]==D[1]:
                        w=Fraction(N[0]+'/'+D[0])
                        if v==w:
                            count+=1
                            prod*=w

                
print prod
fn=clock()
print('Time to run: %.2f seconds' % (fn-st))
