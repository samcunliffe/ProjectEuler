class twovector:
    def __init__(self,xcomp,ycomp):
        self.x=xcomp
        self.y=ycomp
        
    def __repr__(self):
        return repr((self.x,self.y))  
    
    def __add__(self, other):
        data = []
        for j in range(len(self.data)):
            data.append(self.data[j] + other.data[j])
        return Vector(data)

    def mag(self):
        from math import sqrt
        return sqrt((x**2)+(y**2))
        
    
