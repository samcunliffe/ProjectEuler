## SOLVED
#
# Imagine a rectangular grid measuring a units
# across and b units down.
# 
# There are a+1 vertical lines and b+1 horizontal
# lines. Each rectangle formed on this grid is made
# up of two vertical lines and two horizontal lines.
# 
# As there are C(a+1,2)=a(a+1)/2 ways of picking two
# vertical lines and, similarly, b(b+1)/2, ways of
# picking two horizontal lines.
# 
# Hence, there are a(a+1)b(b+1)/4 rectangles on an a
# by b rectangular grid.

# http://en.wikipedia.org/wiki/Binomial_coefficient#Multiplicative_formula


# start timer
from time import clock
st=clock()

# define function
def twoOmega(x):
	return (x*x)+x

def nBoxes(x,y):
    return twoOmega(x)*twoOmega(y)/4

# start points
x,y=20,20

# best values for search
best=25502500
X,Y=100,100

# perform search
print 'Searching'
for x in range(100):
    for y in range(100):
        nB=nBoxes(x,y)
        if abs(2000000-nB)<abs(2000000-best):
            best=nB
            X=x
            Y=y
print X*Y

# stop timer
fn=clock()
print('Time to run %0.3f seconds' % (fn-st))


