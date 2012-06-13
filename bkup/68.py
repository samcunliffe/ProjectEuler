## SOLVED! But I actually did it by hand 
## using guesswork and logic first

# http://projecteuler.net/index.php?section=problems&id=68

from itertools import permutations
from time import clock

st=clock()

lrgConcat=0

for p in permutations([10,9,8,7,6,5,4,3,2,1]):

  total=p[0]+p[1]+p[2]

  # ensure all sides sum to the total
  if p[3]+p[2]+p[4]==total:
    if p[5]+p[4]+p[6]==total:
      if p[7]+p[6]+p[8]==total:
        if p[9]+p[8]+p[1]==total:

          # ensure the solution is not a rotation
          if p[9]<p[7] and p[9]<p[5] and p[9]<p[3] and p[9]<p[0]:

            # solution found!
            concat= str(p[9]) + str(p[8]) + str(p[1]) +\
                    str(p[0]) + str(p[1]) + str(p[2]) +\
                    str(p[3]) + str(p[2]) + str(p[4]) +\
                    str(p[5]) + str(p[4]) + str(p[6]) +\
                    str(p[7]) + str(p[6]) + str(p[8])

            if len(concat)==16 and int(concat)>lrgConcat:
              lrgConcat=int(concat)

fn=clock()
print lrgConcat
print 'Time to run: '+str(fn-st)+'sec'
