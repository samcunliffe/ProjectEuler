## SOLVED
#
# Project Euler Problem 36
# ========================
# The decimal number, 585 = 1001001001 (binary), is
# palindromic in both bases.
# 
# Find the sum of all numbers, less than one
# million, which are palindromic in base 10 and base
# 2.
# 
# (Please note that the palindromic number, in
# either base, may not include leading zeros.)
# 



from math import log

def asBinary(n):
    # can just use bin(n) which returns 0b<number in binary>
    # so the bit to test for palindrome is bin(n)[2:]
    # (chops off first two characters)
    
    '''Converts integer n to a string
    representation of binary'''
    l=[2**i for i in range(int(log(n,2)),-1,-1)]
    s=''
    for k in l:
        if n-k >=0:
            s+='1'
            n-=k
        elif n-k <0:
            s+='0'
        
    return s

def asDecimal(s):
    '''Converts string representation
    of binary to a decimal integer'''
    return int(s,2)

def isPalindrome(s):
    '''Tests string for palindrome'''
    a= s[:len(s)/2]
    
    if len(s)%2==0: #string is even length
        b= s[len(s)/2:]
        b=b[::-1]
        if a==b:
            return True
    if len(s)%2!=0: #string is odd length
        b= s[(len(s)/2)+1:]
        b=b[::-1]
        if a==b:
            return True
    return False

#start timing
from time import clock
st=clock()

#search code
t=0
for n in range(1,1000000):
    if isPalindrome(str(n)) and isPalindrome(bin(n)[2:]):
                                                #######
        print n
        t+=n

#stop timing
fn=clock()

# report
print '\nSum of decimal/binary palindromes is ',t
print 'Time to run '+`fn-st`+'s'


    
