## SOLVED
#
# Project Euler Problem 89
# ========================
# 
# The rules for writing Roman numerals allow for
# many ways of writing each number (see FAQ: Roman
# Numerals). However, there is always a "best" way
# of writing a particular number.
# 
# For example, the following represent all of the
# legitimate ways of writing the number sixteen:
#
# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI
# 
# The last example being considered the most
# efficient, as it uses the least number of
# numerals.
# 
# The 11K text file, roman.txt (right click and
# 'Save Link/Target As...'), contains one thousand
# numbers written in valid, but not necessarily
# minimal, Roman numerals; that is, they are
# arranged in descending units and obey the
# subtractive pair rule (see FAQ for the definitive
# rules for this problem).
# 
# Find the number of characters saved by writing
# each of these in their minimal form.
#
# Note: You can assume that all the Roman numerals
# in the file contain no more than four consecutive
# identical units.


# roman2int
def value(rn):
    '''Returns the value of the Roman numeral, rn'''

    # will hold the sum
    s=0

    while (len(rn)!=0):

        # take most significant numeral
        numeral=rn[0]

        # check to see if there
        # is a next numeral
        if (len(rn)==1):
            nextNumeral='0' # dummy
        else:
            nextNumeral=rn[1]

            
        if numeral=='M':
            s+=1000   # add value of 'M'
            rn=rn[1:] # discard 'M' from numeral string
            
        if numeral=='C':
            if nextNumeral=='M':
                s+=900    # add value of 'CM'
                rn=rn[2:] # discard 'CM' from numeral string
                
            elif nextNumeral=='D':
                s+=400
                rn=rn[2:]
                
            else:
                s+=100
                rn=rn[1:]

        if numeral=='D':
            s+=500
            rn=rn[1:]

        if numeral=='X':
            if nextNumeral=='C':
                s+=90
                rn=rn[2:]
                
            elif nextNumeral=='L':
                s+=40
                rn=rn[2:]
                
            else:
                s+=10
                rn=rn[1:]
                
        if numeral=='L':
            s+=50
            rn=rn[1:]

        if numeral=='I':
            if nextNumeral=='X':
                s+=9
                rn=rn[2:]
                
            elif nextNumeral=='V':
                s+=4
                rn=rn[2:]
                
            else:
                s+=1
                rn=rn[1:]

        if numeral=='V':
            s+=5
            rn=rn[1:]
                
    return s

## int2roman
def minimal(n):
    '''Returns the minimal form Roman numeral of the value n'''

    rn=''

    while n>=1000:
        rn+='M'
        n-=1000

    if (n-900)>=0:
        rn+='CM'
        n-=900

    if (n-500)>=0:
        rn+='D'
        n-=500

    if (n-400)>=0:
        rn+='CD'
        n-=400

    while n>=100:
        rn+='C'
        n-=100

    if (n-90)>=0:
        rn+='XC'
        n-=90

    if (n-50)>=0:
        rn+='L'
        n-=50

    if (n-40)>=0:
        rn+='XL'
        n-=40

    while n>=10:
        rn+='X'
        n=n-10

    if (n-9)>=0:
        rn+='IX'
        n-=9
            
    if (n-5)>=0:
        rn+='V'
        n=n-5

    if (n-4)>=0:
        rn+='IV'
        n=n-4
        
    while n>0:
        rn+='I'
        n=n-1

    return rn

from time import clock

# start timer
st=clock()

# import the file
data=open('problem89data.txt','r')

# will hold the total savings
s=0

for line in data:

    # get the text file numeral
    # remove the '\n' at the end
    if (line[-1]=='\n'):
        romanNumeral=line[:-1]
    else:
        romanNumeral=line

    # find the minimal form of the text file numeral
    minimalRomanNumeral=minimal(value(romanNumeral))

    # total up the character saving
    s+=len(romanNumeral)-len(minimalRomanNumeral)

#report
print s

# stop timer
fn=clock()
print('\nTime to run %0.3f seconds' % (fn-st))
