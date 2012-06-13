# Project Euler Problem 81
# ========================
# In the 5 by 5 matrix below, the minimal path sum
# from the top left to the bottom right, by only
# moving to the right and down, is indicated by *s
#
#    131*	673	234	103	 18
#    201*	 96*	342*	965	150
#    630	803	746*	422*	111
#    537	699	497	121*	956
#    805	732	524	 37*	331*
#	
# Find the minimal path sum, in matrix.txt (right
# click and 'Save Link/Target As...'), a 31K text
# file containing a 80 by 80 matrix, from the top
# left to the bottom right by only moving right and
# down.


## do the same thing as problems 18 & 67: replace
## each diagonal with a minimal sum

from time import clock
st=clock()

def smallest(x,y):
    if(x<=y):   return x
    else:       return y

data=open('problem81data.txt','r')

M=[] #will store matrix

#reads matrix into M which becomes a list of sublists
for line in data:
    M.append( map( int, line.split(',') ) )


dimension=79
for a in range(158,-1,-1):
    for b in range(a,-1,-1):
        c=a-b
        #print b
        #print c
        if b==c and b==dimension:
            continue
        elif b==dimension:
            M[b][c]+=M[b][c+1]
        elif c==dimension:
            M[b][c]+=M[b+1][c]
        elif b<dimension and c<dimension:
            M[b][c]+=smallest(M[b+1][c],M[b][c+1])
        else:
            continue

print M[0][0]

fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
