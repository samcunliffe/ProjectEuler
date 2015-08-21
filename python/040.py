## SOLVED
#
# Project Euler Problem 40
# ========================
# An irrational decimal fraction is created by
# concatenating the positive integers:
# 
#    0.123456789101112131415161718192021...
# 
# It can be seen that the 12th digit of the
# fractional part is 1.
# 
# If dn represents the nth digit of the fractional
# part, find the value of the following expression.
# 
#   d1 x d10 x d100 x d1e3 x d1e4 x d1e5 x d1e6
#
#
s=''
i=0
while len(s)<1000001:
    s+=str(i)
    i+=1

product=int(s[1])\
         *int(s[10])\
         *int(s[100])\
         *int(s[1000])\
         *int(s[10000])\
         *int(s[100000])\
         *int(s[1000000])

print product
