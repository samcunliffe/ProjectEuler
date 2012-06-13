# Project Euler Problem 16
# ========================
# 2^(15) = 32768 and the sum of its digits is 
#   3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 
#    2^(1000)?


def digitSum(n):   #sum the digits in a number
   t=0
   for j in range(0,len(str(n))):
      t+=(n%10)
      n/=10
   return t

import math
f=math.pow(2,1000)
print digitSum(int(f))
