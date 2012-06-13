
from math import sqrt,floor

# find continued fraction of sqrt(N)
def cf_sqrt(n):

  a0=floor(sqrt(n))
  print a0

  f1=1./(sqrt(n)-a0)
  a1=floor(f1)
  print a1

  f2=1./(sqrt(n)-a1)
  a2=floor(f2)
  print a2
cf_sqrt(13)
