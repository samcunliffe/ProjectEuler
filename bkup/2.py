#!/usr/bin/python

# Find the sum of all the even-valued terms in the Fibonacci
# sequence which do not exceed four million.

def fib(n): 
  return fib(n-1)+fib(n-2)

print sum([fib(x) for x in range(4*(10**6)) if fib(x)<4*(10**6)])
