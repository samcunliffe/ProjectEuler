from math import sqrt
 
odd_period = 0
L = 10000
 
for N in range(23,24):#2, L+1):
  r = limit = int(sqrt(N))
  print 'r=',r
  print 'limit=',limit
  if limit*limit == N: 
    continue
    print 'inside if, continuing'
  k, period = 1, 0
  print 'k=',k
  print 'period=',period
  i=0
  while k !=1 or period == 0:
    i+=1
    print '\nWhile loopcount ',i
    k = (N - r * r) / k
    print 'k=',k
    r = ((limit + r) / k) * k - r
    print 'r=',r
    period += 1
    print 'period=',period
  if period % 2 == 1: odd_period += 1
 
#print "Answer to PE64 =", odd_period
