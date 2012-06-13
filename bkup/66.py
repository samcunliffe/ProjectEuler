# x**2 - D y**2 = 1
# is Pell's Equation

def mag(a):
  if   a>=0 : return a
  elif a<0  : return -a




# the Chakravala method...
def chakravala(D):
  # find the closest square number
  # to D to start off, set b to 1
  a,b=int(D**(0.5))+1, 1
  k=a**2 -D

  print (a,b,k)

  m=1
  while 1:
  #for i in range(3):
    A,B,K=float((a*m)+D)/k, float(a+m)/k, float(m**2 -D)/k
    print m
    print (A,B,K)

    if B == int(B) :
      a,b,k=int(A),int(B),int(K)
      break #breaks this while loop
 
    m+=1
  
  return (a,b)

print chakravala(61)





print '\nSearching'

X=0
D=-1

for d in range(1,8):

  #if d in [250,500,750]:
  #  print d
  
  # find Diopantine solutions
  x,y=chakravala(d)

  # on-the-fly search for largest x
  if x>X: # biggest x so far
    X=x
    D=d

print D


