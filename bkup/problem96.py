class sudoku:
    def __init__(self,l):
        self.rows=l
        self.possibilities=[[set(range(1,10))]*9]*9

    def __repr__(self):
        # string for printing
        s='\n'

        # loop over rows
        for m in range(9):

            # loop over columns
            for n in range(9):
                
                s+=' '
                s+=self.rows[m][n]

                # new row
                if n==8:
                    s+='\n'

                # split into 3x3 boxes
                if n in [2,5]:
                    s+=' |'
                if (m,n) in [(2,8),(5,8)]:
                    s+=' ---------------------\n'
        return s+'\n'

    def getrow(self,n):
        return self.rows[n]
    
    def getcolumn(self,m):
        mthcol=[]
        for row in self.rows:
            mthcol.append(row[m])
        return mthcol

    def getcell(self,m,n):
        return self.rows[n][m]

    def solved(self):
        print self.possibilities
        #for m in range(9):
        #    for n in range(9):

def importGrids(filename):
    # open file for reading
    f=file(filename,"r")

    # prepare lists for data
    currentGrid=[]
    data=[]

    # import data
    for line in f:
        
        if line[0:7]=="Grid 01":
            # ignore the first label
            continue
        
        elif line[0:4]=="Grid":
            # save the previous grid
            data.append(sudoku(currentGrid))

            # clear ready for new grid
            currentGrid=[]
            
        else:
            # add each line to the grid
            currentGrid.append(map(str,list(line[0:9])))

    return data

grids=importGrids("problem96data.txt")
print grids[0]
print sudoku.solved(grids[0])
