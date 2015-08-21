# It is possible to show that the square root of two can be expressed as an
# infinite continued fraction.
#
# sqrt2 = 1+1/(2+1/(2+1/(2+...)))=1.414213...
#
# By expanding this for the first four iterations, we get:
# 
# 1 + 1/2 = 3/2 =1.5
# 1 + 1/(2 + 1/2) = 7/5 =1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 =1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) =41/29=1.41379...
# 
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth
# expansion, 1393/985, is the first example where the number of digits in the
# numerator exceeds the number of digits in the denominator.
# 
# In the first one-thousand expansions, how many fractions contain a numerator 
# with more digits than denominator?  

from fractions import Fraction
from time import clock
st=clock()

def continued(n):
    '''
    Returns the nth expansion of the continued fraction for sqrt 2
    '''
    return 1+Fraction(1,eval(
        ('2+Fraction(1,'*n)+'2'+(n*')')
        ))

def digits(x):
    return len(str(x))

# arrays to store numerator and
# denominator values
n=[1]*1001
d=[1]*1001

# total
t=0

# perform sequential calculations
# and check for digits(n)>digits(d)
for i in range(1,1000):
    n[i]=n[i-1]+(2*d[i-1])
    d[i]=n[i-1]+d[i-1]
    
    if digits(n[i])>digits(d[i]):
        t+=1

print t
fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
