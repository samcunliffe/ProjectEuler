## SOLVED
#
# Project Euler Problem 76
# ========================
# It is possible to write five as a sum in exactly
# six different ways:
#
#    4 + 1
#    3 + 2
#    3 + 1 + 1
#    2 + 2 + 1
#    2 + 1 + 1 + 1
#    1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written
# as a sum of at least two positive integers?


# this is the integer partition function
# see problem31.py

def p(n):
    '''The integer partitions of n'''
    coins=range(1,n+1)
    count=[0]*(n+1)

    count[0]=1
    for coin in coins:
        for i in range(coin,n+1):
            count[i]+=count[i-coin]
    return count[n]

print p(100)-1 
# needs to be minus one to remove the (valid) integer partion
# 100 = 100 which is not a sum

# minus one since the trivial partition
# 100= 100+0 is included in the function
