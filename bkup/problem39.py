## SOLVED but very slow
#
# Project Euler Problem 39
# ========================
# 
# If p is the perimeter of a right angle triangle
# with integral length sides, {a,b,c}, there are
# exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p <= 1000, is the number of
# solutions maximised?

from math import sqrt
from time import clock

def nSolns(p):
    slns=[]
    for a in range(p/2):
        for b in range(p/2):
            c=int(sqrt((a**2)+(b**2)))
            if a+b+c==p:
                if c-sqrt((a**2)+(b**2))==0:
                    if set([a,b,c]) not in slns:
                        slns.append(set([a,b,c]))
    return len(slns)/2

st=clock()

print 'Searching'
maximum=3
P=120
for p in range(1001):
    if nSolns(p)>maximum:
        maximum=nSolns(p)
        P=p
print P

fn=clock()
print('Time to run %0.3f s' % (fn-st))
