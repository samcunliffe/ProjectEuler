def f(x):
	return (x*x)+x

def nBoxes(x,y):
    return f(x)*f(y)/4

x=20
y=20
best=25502500
bestX,bestY=100,100

for x in range(100):
    for y in range(100):
        nB=nBoxes(x,y)
        if abs(2000000-nB)<abs(2000000-best):
            best=nB
            bestX=x
            bestY=y


print bestX*bestY
