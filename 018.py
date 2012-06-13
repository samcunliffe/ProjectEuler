## SOLVED
#
# Project Euler Problem 18
# ========================
# By starting at the top of the triangle below and
# moving to adjacent numbers on the row below, the
# maximum total from top to bottom is 23.
# 
#                   3
#                  7 4
#                 2 4 6
#                8 5 9 3
# 
# That is, 3 + 7 + 4 + 9 = 23.
# 
# Find the maximum total from top to bottom of the
# triangle below:
# 
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is
# possible to solve this problem by trying every route.
# However, Problem 67, is the same challenge with a
# triangle containing one-hundred rows; it cannot be
# solved by brute force, and requires a clever method! ;o)
#

def biggest(x,y):
    if(x>=y):   return x
    else:       return y
    
#data=open('problem18data.txt','r')
data=open('problem67data.txt','r')

T=[] #will store triangle

#reads triangle into T which becomes a list of sublists
for line in data:
    T.append( map( int, line.split() ) )

#reduces triangle from second-to-last row upwards
for row in range(len(T)-2,-1,-1):
    for entry in range(len(T[row])):
        T[row][entry]+=biggest( T[row+1][entry] , T[row+1][entry+1])

#answer
print T[0][0]


# Using the small example from above...
#
#                    3               (0,0)
#                  7   4           (1,0) (1,1)
#                2   4   6       (2,0) (2,1) (2,2)
#              8   5   9   3   (3,0) (3,1) (3,2) (3,3)
#
# and considering entries on the penultumate row
# (row #2 if we start counting from #0)
# First take the case of the 2 (indexes row=2, entry=0).
# We don't know that 2 isn't included in the final sum but
# any sum containing this 2 will go on to contain the 8 in
# the row below. So 2 can be replaced by 10.
# Then consider the 4 which is at location (2,1) if we ended
# up here, then we'd add the 9 from below so this can be
# replaced by 13. Continuing in this vein results in...
#
#                    3
#                  7   4
#               10  13  15
#              8   5   9   3
#
# Now move up a row to the (1,0) entry 7+13 > 7+10 so it can
# also be replaced...
#
#                    3
#                 20  19
#               10  13  15
#              8   5   9   3
#
# Finally, the largest of the two entries in row 1 is 20 so
# 20+3=23 is the solution.
