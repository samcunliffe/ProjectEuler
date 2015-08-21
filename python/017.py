## SOLVED
#
# Project Euler Problem 17
# ========================
# If the numbers 1 to 5 are written out in words: one,
# two, three, four, five, then there are
#
#      3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand)
# inclusive were written out in words, how many letters
# would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342
# (three hundred and forty-two) contains 23 letters
# and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in
# compliance with British usage.
#

one2Nine    = [0,3,3,5,4,4,3,5,5,4]
            # including a 0 value placeholder for 'zero'

ten2Nineteen = [3,6,6,8,8,7,7,9,8,8]

tys         = [6,6,6,5,5,7,6,5]

hundred     =  7
aand        =  3
oneThousand = 11

twenty2Nintynine = []
for i in tys:
    for j in one2Nine:
        twenty2Nintynine.append(i+j)

one2Nintynine = one2Nine+ten2Nineteen+twenty2Nintynine


hundreds=[(k+7) for k in one2Nine[1:]]

oneHundred2NineHundredAndNintynine=[]
for m in hundreds:
    for n in one2Nintynine:
        if n==0: # i.e. the zero placeholder
            oneHundred2NineHundredAndNintynine.append(m)
        else:
            oneHundred2NineHundredAndNintynine.append(m+aand+n)

one2OneThousand=one2Nintynine\
                 +oneHundred2NineHundredAndNintynine\
                 +[oneThousand]

print sum(one2OneThousand)    

