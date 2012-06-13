def pprint(M):
  for row in M:
    print row
  print ''
  return 0

# http://projecteuler.net/index.php?section=problems&id=81

# start timer
from time import clock
st=clock()

# open text file
textfile=open('matrix.txt','r')

# will store matrix
M=[]


# the example	
M=[ [131,	673,	234,	103,	18 ],
    [201,	96,	  342,	965,	150],
    [630,	803,	746,	422,	111],
    [537,	699,	497,	121,	956],
    [805,	732,	524,	37,	  331]  ]

## read file into matrix
## (a list of sublists)
#for line in textfile:
#  M.append( map( int, line.split(',') ) )

# the smallest if two ints
def sml(x,y):
  if(x<=y): return x
  else:     return y

# size of matrix
dim=len(M[0])-1

# perform minimal backwards sum
for a in range(dim*2,-1,-1):
    for b in range(a,-1,-1):
        c=a-b
        
        #
        if b==c and b==dim:
            continue

        # at the edge
        elif b==dim:
            M[b][c]+=M[b][c+1]
            pprint(M)

        # at the edge
        elif c==dim:
            M[b][c]+=M[b+1][c]
            pprint(M)

        elif b<dim and c<dim:
            M[b][c]+=sml(M[b+1][c],M[b][c+1])
            pprint(M)
        else:
            continue

# result in first entry
print M[0][0]

# stop stopwatch
fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
