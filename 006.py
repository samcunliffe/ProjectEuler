# The sum of the squares of the first ten natural numbers is, 
#       1^(2) + 2^(2) + ... + 10^(2) = 385
#
# The square of the sum of the first ten natural numbers is,
#       (1 + 2 + ... + 10)^(2) = 55^(2) = 3025
#
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

SumOfSquares = 0
Sum          = 0
for n in range(1,101):
  SumOfSquares += (n**2)
  Sum += n
SquareOfSum = Sum**2
print SquareOfSum - SumOfSquares


print (sum(range(101))**2)-sum([a**2 for a in range(101)])
