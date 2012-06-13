#  Project Euler Problem 103
#  =========================
#  Let S(A) represent the sum of elements in set A of size n. We
#  shall call it a special sum set if for any two non-empty disjoint
#  subsets, B and C, the following properties are true:

#    (i)   S(B) != S(C); that is, sums of subsets cannot be equal.
#    (ii)  If B contains more elements than C then S(B) > S(C).

#  If S(A) is minimised for a given n, we shall call it an optimum
#  special sum set. The first five optimum special sum sets are
#  given below.

#  n = 1: {1}
#  n = 2: {1, 2}
#  n = 3: {2, 3, 4}
#  n = 4: {3, 5, 6, 7}
#  n = 5: {6, 9, 11, 12, 13}

#  It seems that for a given optimum set, 
#             A = {a1, a2, ... , an},
#  the next optimum set is of the form 
#         B = {b, a1+b, a2+b, ... ,an+b}, 
#  where b is the "middle" element on the previous row.

#  By applying this "rule" we would expect the optimum set for n = 6
#  to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However,
#  this is not the optimum set, as we have merely applied an
#  algorithm to provide a near optimum set. The optimum set for 
#  n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and
#  corresponding set string: 111819202225.

#  Given that A is an optimum special sum set for n = 7, find its
#  set string.

#  NOTE: This problem is related to problems 105 and 106.

# ===============================================================

# make notation same as in the problem
def S(A):               return sum(A)
def n(A):               return len(A)
def middleElement(A):   return A[-len(A)/2]
def setString(A):       return ''.join([str(a) for a in A])

# the algotrithm to find provide the next near optimum set
def nextNearOptimum(A):
  b=middleElement(A)
  B=[b]
  for a in A:
    B.append(a+b)
  return B

# print out the sets up to n=6
A=[1]
for i in range(6):
  print 'n='+str(i+1)+'    A='+str(A)
  A=nextNearOptimum(A)

# the correct optimum special set for n=6
A = [11, 18, 19, 20, 22, 25]
print '\nn=6    A='+str(A)

# the near optimum set for n=7
A=nextNearOptimum(A)
print '\nn=7    A='+str(A)



# make all two-subset possibilities from A
possibilities=[]

for firstElement in range(len(A)):
  for lastElement in range(firstElement+1,len(A)):

    # B is the subset of A
    B=A[firstElement:lastElement]

    # copy the whole list A onto C
    C=[]
    C.extend(A)

    # remove elements in B
    for b in B:
      C.remove(b)

    print B
    print C
    print ''
    possibilities.append((B,C))
