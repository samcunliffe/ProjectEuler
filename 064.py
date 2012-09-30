
from math import sqrt,floor
from time import clock
st=clock()


def isOdd(n):return n%2!=0



def irrationalSurds(n):
  """Returns list of numbers <n that are not squares"""
  return [i for i in range(n) if sqrt(i)!=floor(sqrt(i))]



def periodLength(s):
  """
  Iterates over continued fraction expansion of sqrt(s) until period is found,
  returns the length of the period.
  """
  
  # check input
  if sqrt(s)==floor(sqrt(s)): 
    print "Call to periodLength() with a rational number argument:",s
    return -1

  n=0; m=[0]; d=[1]; a=[floor(sqrt(s))]
  prevSets=[[m[0],d[0],a[0]]]

  while True:

    # calculate vals
    m_nplus1=(d[n]*a[n])-m[n]
    d_nplus1=(s-(m_nplus1*m_nplus1))/d[n]
    a_nplus1=floor((a[0] + m_nplus1)/d_nplus1)

    # check to see if we've seen these values before
    thisSet=[m_nplus1,d_nplus1,a_nplus1]
    if thisSet in prevSets:
      return n+1-prevSets.index(thisSet)

    # if not, push all vals back
    m.append(m_nplus1)
    d.append(d_nplus1)
    a.append(a_nplus1)
    prevSets.append(thisSet)
    n+=1




s=0
for i in irrationalSurds(10000):
  if isOdd(periodLength(i)):s+=1

print s
fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
