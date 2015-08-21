def isPrime(n):
    import math
    n = abs(n)
    i = 2
    while (i <= math.sqrt(n)):
        if (n % i == 0):
            return False
        i += 1
    return True

def isCircPrime(n)
   if (isPrime(n)==False):
      return False
   else:
      bck=int(str(n)[::-1])
      if (isPrime(bck)==True):
         return True
      else:
         return False

for i in range(1,1000000,2)
