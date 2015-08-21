## SOLVED
#
# Project Euler Problem 23
# ========================
# 
# A perfect number is a number for which the sum of
# its proper divisors is exactly equal to the
# number. For example, the sum of the proper
# divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.
# 
# A number n is called deficient if the sum of its
# proper divisors is less than n and it is called
# abundant if this sum exceeds n.
# 
# As 12 is the smallest abundant number,
#	 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum
# of two abundant numbers is 24. By mathematical
# analysis, it can be shown that all integers greater
# than 28123 can be written as the sum of two
# abundant numbers. However, this upper limit cannot
# be reduced any further by analysis even though it
# is known that the greatest number that cannot be
# expressed as the sum of two abundant numbers is less
# than this limit.
# 
# Find the sum of all the positive integers which cannot
# be written as the sum of two abundant numbers.



# divisor sum
def d(n):
    t=1
    import math
    for i in range(2,n):
        if n%i==0:
            t+=i
    return t
    
abundants=set() #a set is a better data type
                #for this, since it does not
                #duplicate entries and
                #maintains their order.
                #**see notes at very end**

lim=28124



# create big list of abundant numbers
print 'Listing abundant numbers'

for a in range(1,lim):
    if d(a)>a: abundants.add(a)



# search the natural numbers for non sums
print 'Searching for numbers not sums of abundants'
s=0

for b in range(1,lim):
    if not any((b-c in abundants) for c in abundants):
        s+=b

print s


# really concise python solution from the PE forum
# by norvig from USA Python 2.4 with 2.5's "any":
# 
# 
##abundants = set(i for i in range(1,28124) if d(i) > i)
##
##def abundantsum(i):
##return any(i-a in abundants for a in abundants)
##
##print sum(i for i in range(1,28124) if not abundantsum(i))
#
#


# From the Python documentation
#
##A set object is an unordered collection of
##distinct hashable objects. Common uses include
##membership testing, removing duplicates from a
##sequence, and computing mathematical operations
##such as intersection, union, difference, and
##symmetric difference. (For other containers see
##the built in dict, list, and tuple classes, and
##the collections module.)
##
##New in version 2.4.
##
##Like other collections, sets support x in set,
##len(set), and for x in set. Being an unordered
##collection, sets do not record element position or
##order of insertion. Accordingly, sets do not
##support indexing, slicing, or other sequence-like
##behavior.
##
##There are currently two built-in set types, set
##and frozenset. The set type is mutable - the
##contents can be changed using methods like add()
##and remove(). Since it is mutable, it has no hash
##value and cannot be used as either a dictionary
##key or as an element of another set. The frozenset
##type is immutable and hashable - its contents
##cannot be altered after it is created; it can
##therefore be used as a dictionary key or as an
##element of another set.
##
##As of Python 2.7, non-empty sets (not frozensets)
##can be created by placing a comma-separated list
##of elements within braces, for example: {'jack',
##'sjoerd'}, in addition to the set constructor.
