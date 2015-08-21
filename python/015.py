## SOLVED
#
# Project Euler Problem 15
# ========================
# Starting in the top left corner of a 2x2 grid,
# there are 6 routes (without backtracking) to the
# bottom right corner.
#
# How many routes are there through a 20x20 grid?

n=20 # grid size
import math
ans= math.factorial(2*n)/(math.factorial(n)*math.factorial(n))
print ans

# This is a Statistical mechanics problem.
# The statistical weight (number of states)
# is the quotient of the total number of arrangements
# divided through by the number of indistinct
# arrangements (to get rid of the overcount).
#
# Analogously, the word "STATISTICS" has 10! anagrams.
# But the word has three "S"s, three "T"s and
# two "I"s; so we have to divide through by 3!x3!x2! to
# account for the overcount.
#
# Namely:   10! / ( 3!x3!x2! )
#
# Routes accross a grid are just arrangements of the
# directions "R" (for "move right") and "D" (for
# "move down"). So for 2x2 grids we have 6 combinations
# because there are 6 distinct anagrams of the word:
#
#           RRDD
#
# The formula is:       (2x2)! / (2!x2!) = 6
#
# which is clearly:       2n!  /  (n!n!)
#
#




