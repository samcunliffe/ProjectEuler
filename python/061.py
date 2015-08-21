## SOLVED

# Project Euler Problem 61
# ========================
#	Triangle, square, pentagonal, hexagonal, heptagonal, and
#	octagonal numbers are all figurate (polygonal) numbers and are
#	generated by the following formulae:

#	Triangle 	 	P3,n=n(n+1)/2  	1, 3,  6, 10, 15, ...
#	Square 	  	P4,n=n2 	  		1, 4,  9, 16, 25, ...
#	Pentagonal 	P5,n=n(3n-1)/2 	1, 5, 12, 22, 35, ...
#	Hexagonal  	P6,n=n(2n-1) 	  1, 6, 15, 28, 45, ...
#	Heptagonal 	P7,n=n(5n-3)/2 	1, 7, 18, 34, 55, ...
#	Octagonal  	P8,n=n(3n-2) 	  1, 8, 21, 40, 65, ...

#	The ordered set of three 4-digit numbers: 8128, 2882, 8281, has
#	three interesting properties.

# The set is cyclic, in that the last two digits of each number
#	is the first two digits of the next number (including the last
#	number with the first).

#	Each polygonal type: triangle (P3,127=8128), square (P4,91=8281),
#	and pentagonal (P5,44=2882), is represented by a different number
#	in the set.

#	This is the only set of 4-digit numbers with this property.

#	Find the sum of the only ordered set of six cyclic 4-digit
#	numbers for which each polygonal type: triangle, square,
#	pentagonal, hexagonal, heptagonal, and octagonal, is represented
#	by a different number in the set.



from time import clock

def triangle(n):
  return n*(n+1)/2

def square(n):
  return n*n

def pentagonal(n):
  return n*(3*n -1)/2

def hexagonal(n):
  return n*(2*n -1)

def heptagonal(n):
  return n*(5*n -3)/2

def octagonal(n):
  return n*(3*n -2)

def f(n):
  return (
            (3,triangle(n)),
            (4,square(n)),
            (5,pentagonal(n)),
            (6,hexagonal(n)),
            (7,heptagonal(n)),
            (8,octagonal(n))
          )

def problem61():

  data=[] #list of figurate numbers with type

  # get all 4 digit figurate numbers
  for n in range(19,141): #limits obtained analytically
    for order, number in f(n):
      if 1000<=number<=9999 :
        data.append( (order,str(number)) ) 
                            #numbers as str for easy comparison

  # perform search for cyclic set

  for t1,fn1 in data:

    for t2,fn2 in data:
      if t1 != t2:
        if fn1[2:]==fn2[:2]:

          for t3,fn3 in data:
            if t3 not in [t1,t2]:
              if fn2[2:]==fn3[:2]:

                for t4,fn4 in data:
                  if t4 not in [t1,t2,t3]:
                    if fn3[2:]==fn4[:2]:

                      for t5,fn5 in data:
                        if t5 not in [t1,t2,t3,t4]:
                          if fn4[2:]==fn5[:2]:

                            for t6,fn6 in data:
                              if t6 not in [t1,t2,t3,t4,t5]:
                                if fn5[2:]==fn6[:2]:

                                  if fn6[2:]==fn1[:2]:
      
                                    # this is the set
                                    s=[fn1,fn2,fn3,fn4,fn5,fn6]
                                    # break all loops, return answer
                                    return sum(map(int,s))


st=clock()                                
print problem61()
fn=clock()
print 'Time to run: '+str(fn-st)+ ' sec'
