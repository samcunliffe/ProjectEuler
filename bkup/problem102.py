## SOLVED
#
# Project Euler Problem 102
# =========================
# Three distinct points are plotted at random on a
# Cartesian plane, for which
#                -1000 <= x, y <= 1000,
# such that a triangle is formed.
# 
# Consider the following two triangles:
# 
#      A(-340,495), B(-153,-910), C(835,-947)
#      X(-175,41),  Y(-421,-714), Z(574,-645)
# 
# It can be verified that triangle ABC contains the
# origin, whereas triangle XYZ does not.
# 
# Using triangles.txt (right click and 'Save
# Link/Target As...'), a 27K text file containing
# the co-ordinates of one thousand "random"
# triangles, find the number of triangles for which
# the interior contains the origin.
#
# NOTE: The first two examples in the file represent
# the triangles in the example given above.

from time import clock
st=clock()

print 'Reading in data'
f=file('problem102data.txt','r')
data=[]
for line in f:
    data.append(eval(line))



def crossProd((xa,ya),(xb,yb),(xc,yc)):
    '''
    Calculates the vector cross
    product between two vectors
    which are taken to be in the
    cartesian plane.
       AB x AC
    '''
    #         ABx     ACy   -   ABy     ACx
    return ((xb-xa)*(yc-ya))-((yb-ya)*(xc-xa))


# origin coordinates
origin=(0,0)

# counter for number of times triangle covers origin
insideCount=0

print 'Counting with vector products method'

for trianglePoints in data:

    vertex1=(trianglePoints[0:2])
    vertex2=(trianglePoints[2:4])
    vertex3=(trianglePoints[4:6])


    # work out which direction is inside
    # the triangle by performing vector
    # product (1->2) X (1->3)
    if crossProd(vertex1,vertex2,vertex3)>0:
        direction12x13=+1
    elif crossProd(vertex1,vertex2,vertex3)<0:
        direction12x13=-1
    else:
        print 'Error, (1->2) X (1->3) =0 at ',trianglePoints
        break
    

    # same but for (3->1) X (3->2)
    if crossProd(vertex3,vertex1,vertex2)>0:
        direction31x32=+1
    elif crossProd(vertex3,vertex1,vertex2)<0:
        direction31x32=-1
    else:
        print 'Error, (3->1) X (3->2) =0 at ',trianglePoints
        break


    # ...for (2->3) X (2->1)
    if crossProd(vertex2,vertex3,vertex1)>0:
        direction23x21=+1
    elif crossProd(vertex2,vertex3,vertex1)<0:
        direction23x21=-1
    else:
        print 'Error, (2->3) X (2->1) =0 at ',trianglePoints
        break

    
    # now want the vector product of each
    # side vector with the origin vector to
    # be in the same direction
    if (crossProd(vertex1,vertex2,origin)*direction12x13) >0:
        if (crossProd(vertex3,vertex1,origin)*direction31x32) >0:
            if (crossProd(vertex2,vertex3,origin)*direction23x21) >0:
                insideCount+=1





print insideCount

fn=clock()
print('Time to run %0.3f seconds' % (fn-st))




















