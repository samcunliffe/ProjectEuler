# Project Euler Problem 1
# =======================
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# the loopy way
t=0
for n in range(1000):
    if n%3==0 or n%5==0 :
        t+=n
print t

# one liner
print sum([x for x in range(1000) if x%3==0 or x%5==0])

# another one liner using sets
print sum(set(range(0,1000,3))|set(range(0,1000,5)))

# the pipe "|" denotes the union of sets
# equivalent to:
#    set(***).union(set(***))
