# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91*99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(s):
  if s==s[::-1]:  return True
  else:           return False

biggest=0
for a in range(100,1000):
  for b in range(100,1000):
    if isPalindrome( str(a*b) ) and a*b>biggest:
      biggest=a*b

print biggest
