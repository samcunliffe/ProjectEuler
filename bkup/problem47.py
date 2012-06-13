## SOLVED
## Really slow! 342 sec!
#
# Project Euler Problem 47
# ========================
# The first two consecutive numbers to have two
# distinct prime factors are:
#  
#     14 = 2 x 7
#     15 = 3 x 5
# 
# The first three consecutive numbers to have three
# distinct prime factors are:
# 
#     644 = 2**2 x  7 x 23
#     645 = 3    x  5 x 43
#     646 = 2    x 17 x 19.
# 
# Find the first four consecutive integers to have
# four distinct primes factors. What is the first of
# these numbers?

def getPrimeFactors(n):
    factor=2
    N=n
    l=[]
    while 1:
        if N%factor==0:
            N/=factor
            l.append(factor)
        if N%factor!=0:
            factor+=1
        if N==1:
            break
    return l
           
def areDistinctLists(A,B):
    for a in A:
        for b in B:
            if a==b:
                if A.count(a)==B.count(b):
                    return False
    return True


from time import clock
st=clock()

print 'Searching'
number=(2*3*5*7)

while 1:
    first=getPrimeFactors(number)
    if len(set(first))==4:
        second=getPrimeFactors(number+1)
        if len(set(second))==4:
            if areDistinctLists(first,second):
                third=getPrimeFactors(number+2)
                if len(set(third))==4:
                    if areDistinctLists(first,third)   \
                       and areDistinctLists(second,third):
                        fourth=getPrimeFactors(number+3)
                        if len(set(fourth))==4:
                            if areDistinctLists(first,fourth)        \
                               and areDistinctLists(second,fourth)   \
                               and areDistinctLists(third,fourth):
                                break
                        else:
                            number+=4
                else:
                    number+=3
        else:
            number+=2
    else:
        number+=1
    
print number
fn=clock()
print('Time to run %0.3f seconds' % (fn-st))



