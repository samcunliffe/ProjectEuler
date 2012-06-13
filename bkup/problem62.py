## SOLVED
#
# Project Euler Problem 62
# ========================
# The cube, 41063625 (345**3), can be permuted to
# produce two other cubes: 56623104 (384**3) and
# 66430125 (405**3). In fact, 41063625 is the
# smallest cube which has exactly three permutations
# of its digits which are also cube.
# 
# Find the smallest cube for which exactly five
# permutations of its digits are cube.



# strategy:
#
# iterate over the cubes of the natural
# numbers whilst taking a sorted list
# of the digits of the cubes
#
# when we have found 5 identical sorted
# lists then find the natural number
# that was used to generate the smallest 

def cubed(n):
    return n**3

def listDigits(n):
    l=[]
    for digit in str(n):
        l.append(digit)
    return sorted(l)

from time import clock
st=clock()

print 'Searching'
n=0 # the index of the list will match the cube root
hashys=[]
while 1:
    hashys.append(listDigits(cubed(n)) )
    if hashys.count(listDigits(cubed(n)))==5:
        print 'Found'
        break
    n+=1

# when above loop breaks, n will be the largest
# cube whose digits are in the permutation group
# so need to find the first occurence of the
# 'listDigits' of n3 then cube the index number(=n)

print (  hashys.index((listDigits(cubed(n))))   )**3


fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
