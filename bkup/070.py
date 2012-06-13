## SOLVED

#  Project Euler Problem 70
#  ========================
#  Euler's Totient function, phi(n) [sometimes called the phi
#  function], is used to determine the number of positive numbers
#  less than or equal to n which are relatively prime to n. For
#  example, as 1, 2, 4, 5, 7, and 8, are all less than nine and
#  relatively prime to nine, phi(9)=6.

#  The number 1 is considered to be relatively prime to every
#  positive number, so phi(1)=1.

#  Interestingly, phi(87109)=79180, and it can be seen that 87109 is
#  a permutation of 79180.

#  Find the value of n, 1 < n < 107, for which phi(n) is a
#  permutation of n and the ratio n/phi(n) produces a minimum.



from samsPrimeTools import sieveOfEratosthenes

def ispermutation(a,b):
  if sorted(str(a))==sorted(str(b)): return True
  else: return False


print 'Sieving'
primes=sieveOfEratosthenes(4000)
for i in range(primes.count(0)):
  primes.remove(0)


print 'Finding totients'
i=0
minratio=2
for p1 in primes:
  i+=1
  for p2 in primes[i:]:
    n=p1*p2
    if n > 10**7:break
    phi=(p1-1)*(p2-1)

    if n==87109:print n,phi
    if ispermutation(n,phi) and n/float(phi)<minratio:
      minn=n
      #minphi=phi
      minratio=n/float(phi)

print minn


#  Given n=p1**e1 p2**e2...pk**ek, phi(n)=n(1-1/p1)(1-1/p2)...(1-1/pk).

#  Now for n/phi(n) to be minimised, phi(n) must be as close to n as
#  possible; that is, we want to maximise phi(n).

#  When evaluating phi(n), we note that each time we multiply by
#  (1-1/pi), it gets smaller, so we need to minimise the number of
#  distinct prime factors in n.

#  If n were prime, it would end in 1,3,7, or 9, and subtracting 1
#  only changes the last digit (to 0,2,6, or 8), so it could not be
#  a permutation.

#  Hence n=p1*p2 and we only need to search through a list of known
#  prime pairs.

#  In addition, phi(p1*p2)=p1*p2*(1-1/p1)(1-1/p2)=(p1-1)(p2-1), so we
#  can compute phi(n) more efficiently.

#  A slick implementation of all these ideas will allow you to find
#  the solution in a few seconds. We would
#  expect n to be as close to ten million as possible, so the pair
#  of prime factors would be around sqrt(1e7); remember we wish to
#  minimise (1-1/pi), so pi must be as large as possible; my minimum
#  prime was 1009.
