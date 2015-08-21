# Project Euler Problem 66
# ========================
# Consider quadratic Diophantine equations of the form:

# x**2 - Dy**2 = 1

# For example, when D=13, the minimal solution in x is 
# 649**2 - 13*180**2 = 1

# It can be assumed that there are no solutions in positive
# integers when D is square.

# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we
# obtain the following:

#  3**2 - 2*2**2 = 1
#  2**2 - 3*1**2 = 1
#  9**2 - 5*4**2 = 1
#  5**2 - 6*2**2 = 1
#  8**2 - 7*3**2 = 1

# Hence, by considering minimal solutions in x for D<=7, the
# largest x is obtained when D=5.

# Find the value of D<=1000 in minimal solutions of x for which
# the largest value of x is obtained.

# ============



from math import sqrt



# the equation solved for y
def y(x,D):
  return sqrt(float(x**2 - 1)/D)



# Get all possible D values 
# up to and including n
def getDvalues(n):
  vals=range(1,n+1)

  # remove all square numbers
  for a in range(1,int(sqrt(n)+1)):
    vals.remove(a*a)

  return vals



# Return the minimal x 
# solution for a given D
def minimalDiophantine(D):
  x=2
  while 1:
    if y(x,D)==int(y(x,D)):
      return [x,y]
    else:
      x+=1




biggestX=9
for D in getDvalues(1000):
  x=minimalDiophantine(D)[0]
  if x>biggestX:
    biggestX=x
    bestD=D
    print D

print biggestX
