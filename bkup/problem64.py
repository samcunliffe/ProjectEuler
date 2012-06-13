def surd2cf(N,k):
  cf=[]
  x=sqrt(N)

  for i in range(k):
    a=int(x)
    cf.append(a)
    if (x-a)==0: return cf
    x=1./(x-a)
  
  return cf

from math import sqrt

oddcount=0

for N in range(2,13):
  print ''
  print 'N=',N

  # zeroth terms
  x0=sqrt(N)
  a0=int(x0)

  if a0*a0 == N:
    print ''
    #then N is a square number
    break

  #first order terms
  x1=1./(x0-a0)
  a1=int(x1)

  x=x0
  k=0
        ## keeps going forever coz there's no precision in x!=x1'
  while x != x1 or k==1:
    a=int(x)
    x=1./(x-a)
    
    print a

    k+=1


  # increment counter if period is odd
  if k%2 != 0:
    oddcount+=1
  print oddcount

print '\n\n\n'
print oddcount


    
