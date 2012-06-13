# project euler problem 124

primes=[2,3,5,7,11]



def product(seq):
  prod=1
  for item in seq:
    prod*=item
  return prod


def rad(n):
  distPrimeFactors=set()
  for p in primes:
  	if n%p ==0:
			n/=p
			distPrimeFactors.add(p)
  return product(distPrimeFactors)

for n in range(1,11):
  print n,rad(n)