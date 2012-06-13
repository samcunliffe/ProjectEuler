# Project Euler Problem 5
# =======================
# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
# What is the smallest number that is evenly divisible by all of the numbers 
# from 1 to 20?

from math import floor
Number = 2520
n = 1

while (n<=20):
  RemainderOfDivision = Number-(n*(floor(Number/n)))
  if (RemainderOfDivision != 0):
    Number = Number+20
    n = 1
  n+=1
print Number
