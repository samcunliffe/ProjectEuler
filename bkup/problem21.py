## SOLVED
#
# Project Euler Problem 21
# ========================
# Let d(n) be defined as the sum of proper divisors of
# n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b
# are an amicable pair and each of a and b are called
# amicable numbers.
# 
# For example, the proper divisors of 220 are
# 		1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# 
# therefore d(220) = 284.
# 
# The proper divisors of 284 are
# 		1, 2, 4, 71 and 142;
# 
# so d(284) = 220.
# 
# 
# Evaluate the sum of all the amicable numbers under 10000.
#


def d(n):
    t=0
    for i in range(1,n): #this works but could be made more
                         #efficient by only going up to sqrt(n)
        if n%i==0:
            t+=i
    return t

#print d(220)
#print d(284)


# not actually used
def areAmicable(x,y):
    if (d(x)==y) and (d(y)==x):
        return True
    else: return False

#print areAmicable(220,284)



total=0
for a in range(1,10000):
        b = d(a)
        if (a!=b) and (a==d(b)):
                total += a
print total
