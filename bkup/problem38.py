## SOLVED
#
# Project Euler Problem 38
# ========================
# Take the number 192 and multiply it by each of 1,
# 2, and 3:
# 
#     192 x 1 = 192
#     192 x 2 = 384
#     192 x 3 = 576
# 
# By concatenating each product we get the 1 to 9
# pandigital, 192384576. We will call 192384576 the
# concatenated product of 192 and (1,2,3)
# 
# The same can be achieved by starting with 9 and
# multiplying by 1, 2, 3, 4, and 5, giving the
# pandigital, 918273645, which is the concatenated
# product of 9 and (1,2,3,4,5).
# 
# What is the largest 1 to 9 pandigital 9-digit
# number that can be formed as the concatenated
# product of an integer with (1,2, ... , n)
# where n > 1?


from itertools import permutations

print 'Finding all 1 to 9 pandigitals'

l=permutations(range(1,10))
pandigitals=[]
for p in l:
    s=''
    for i in p:
        s+=str(i)
    pandigitals.append(s)

print 'Searching for largest by criteria'
largest=192384576

print ' [1,2]'
for x in range(1000,10000):
    s=''
    for y in [1,2]:
        s+=str(x*y)

    if len(s)==9:
        if int(s)>largest:
            if s in pandigitals:
                largest=int(s)

print
for x in range(10,1000):
    s=''
    for y in [1,2,3]:
        s+=str(x*y)
        
    if len(s)==9:
        if int(s)>largest:
            if s in pandigitals:
                largest=int(s)


for x in range(10,100):
    s=''
    for y in [1,2,3,4]:
        s+=str(x*y)
        
    if len(s)==9:
        if int(s)>largest:
            if s in pandigitals:
                largest=int(s)


for x in range(1,20):
    s=''
    for y in [1,2,3,4,5]:
        s+=str(x*y)
        
    if len(s)==9:
        if int(s)>largest:
            if s in pandigitals:
                largest=int(s)
                


for x in range(1,20):
    s=''
    for y in [1,2,3,4,5,6]:
        s+=str(x*y)
        
    if len(s)==9:
        if int(s)>largest:
            if s in pandigitals:
                largest=int(s)


for x in range(1,10):
    s=''
    for y in [1,2,3,4,5,6,7]:
        s+=str(x*y)
        
    if len(s)==9:
        if int(s)>largest:
            if s in pandigitals:
                largest=int(s)

print largest

###
# A fast isPandigital function
###

def isPandigital(n):
    digits=set(str(n))
    if digits==set('123456789'):
        return True
    else
        return False
