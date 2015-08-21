## SOLVED
#
# Project Euler Problem 55
# ========================
#
# If we take 47, reverse and add, 47 + 74 = 121,
# which is palindromic.
#
# Not all numbers produce palindromes so quickly.
# For example,
# 
#     349 + 943 = 1292,
#     1292 + 2921 = 4213
#     4213 + 3124 = 7337
#
# That is, 349 took three iterations to arrive at
# a palindrome.
#
# Although no one has proved it yet, it is thought
# that some numbers, like 196, never produce a
# palindrome. A number that never forms a palindrome
# through the reverse and add process is called a
# Lychrel number. Due to the theoretical nature of
# these numbers, and for the purpose of this
# problem, we shall assume that a number is Lychrel
# until proven otherwise. In addition you are given
# that for every number below ten-thousand, it will
# either (i) become a palindrome in less than fifty
# iterations, or, (ii) no one, with all the
# computing power that exists, has managed so far to
# map it to a palindrome. In fact, 10677 is the
# first number to be shown to require over fifty
# iterations before producing a palindrome:
# 4668731596684224866951378664 (53 iterations,
# 28-digits).
# 
# Surprisingly, there are palindromic numbers that
# are themselves Lychrel numbers; the first example
# is 4994.
#
# How many Lychrel numbers are there below
# ten-thousand?
#
# NOTE: Wording was modified slightly on 24 April
# 2007 to emphasise the theoretical nature of
# Lychrel numbers.

def reverse(n):
    return int( str(n)[::-1] )

def isPalindrome(s):
    '''Tests string for palindrome'''
    a= s[:len(s)/2]
    
    if len(s)%2==0: #string is even length
        b= s[len(s)/2:]
        b=b[::-1]
        if a==b:
            return True
    else: #string is odd length
        b= s[(len(s)/2)+1:]
        b=b[::-1]
        if a==b:
            return True
    return False

def isLychrel(n):
    c=0
    a=n
    while c<50:
        b = a+  reverse(a)
        if isPalindrome(str(b)):
            # used isPalindrome(`b`) which gave some
            # problems as long ints have a trailing L
            # when converted to a string this way
            # however str(b) will always give the pure
            # number as a string
            return False
        else:
            a=b
            c+=1
    return True

from time import clock
st=clock()

#isLychrel(89)
print 'Performing Search'
t=0

for n in range(10001):
    if isLychrel(n):
        t+=1

fn=clock()

print t
print('Time to run: %.2f seconds' % (fn-st))


# A really nice concisely coded version
# by ilan

def reverse(n): return int( str(n)[::-1] )
 
def isLychrel(n):
    for i in range(50):
        n += reverse(n)
        if n==reverse(n): return 0
    return 1
 
print sum( isLychrel(n) for n in range(10000) )
