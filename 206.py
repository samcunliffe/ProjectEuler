## SOLVED by brute force which takes way too long
#
# Project Euler Problem 206
# =========================
# Find the unique positive integer whose square has
# the form 1_2_3_4_5_6_7_8_9_0,
# where each "_" is a single digit.

from math import sqrt
print 'Finding start'
n=int(sqrt(1020304050607080900))

print 'Searching through squares'
while 1:
    square=str(n**2)
    if len(square)==19:
        if square[0]=='1':
            if square[2]=='2':
                if square[4]=='3':
                    if square[6]=='4':
                        if square[8]=='5':
                            if square[10]=='6':
                                if square[12]=='7':
                                    if square[14]=='8':
                                        if square[16]=='9':
                                            if square[18]=='0':
                                                print n
                                                break
    n+=1
