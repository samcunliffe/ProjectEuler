# Project Euler Problem 68

def unique(l):
    '''Returns a list of unique entries in the list
        if the use of set() is not possible'''
    for item in l:
        if l.count(item)>1:
            for c in range(l.count(item)-1):
                l.remove(item)
    return l

def partitions3(n):
    '''Finds all groups of 3 integers that sum to n'''
    s=[]
    for i in range(1,n-1):
        for j in range(1,n-1):
            k=n-i-j
            if k>0:
                s.append( sorted([i,j,k]) )
    return unique(sorted(s))

for branchTotal in range(9,13):
    p=partitions3(branchTotal)
    for s in p:
        s=set(s)
