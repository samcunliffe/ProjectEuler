def digitSum(n):   #sum the digits in a number
   t=0
   for j in range(0,len(str(n))):
      t+=(n%10)
      n/=10
   return t

n=100
import math
f=math.factorial(n)
print digitSum(f)
