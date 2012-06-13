from fractions import Fraction




def R(d):

  if d==1:return Fraction(0,1)

  resilientcount=0
  for n in range(1,d):
    if Fraction(n,d).denominator == d:
      resilientcount+=1

  return Fraction(resilientcount,(d-1))



# brute force!
d=1
while 1:
  d+=1
  if R(d)<Fraction(4,10):
    print d
    break

#d=1
#while 1:
#  d+=1
#  if R(d)<Fraction(15499,94744):
#    print d
#    break

# prime d will have a resilience =1 since nothing divides
# so large multiples of primes will have small resilience
d=24576
for i in range(20) :
  d*=3
  print d
  print R(d)
  if R(d)<Fraction(15499,94744):
    print d
    break
#R(49152) = 16384/49151


