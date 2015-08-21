from fractions import Fraction

def primeFactors(n):
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

def distinctPrimeFactors(n):
    return set(primeFactors(n))
             
def phi(n):
    '''
    Calculates the Euler totent function
    '''
    phi=n
    for p in distinctPrimeFactors(n):
        phi*=(1-Fraction(1,p))
    return int(phi)

#for n in range(1,10000000):
  

end=10000000
runningMin=Fraction(end,1)

#print 'Big search'
for n in range(1,end):
    if n%100000==0:print n
    
    if sorted(str(n))==sorted(str(phi(n))):
        if Fraction(n,phi(n)) < runningMin:
            runningMin=Fraction(n,phi(n))
            N=n
print N


