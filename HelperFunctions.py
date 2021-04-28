class NodeObject():
    def __init__(self,L=None,R=None,U=None,D=None,C=None):
        self.L=L
        self.R=R
        self.D=D
        self.U=U

class ColumnObject( NodeObject ):
    def __init__(self,L=None,R=None,U=None,D=None,C=None,N="defaultName",S=-1):
        super().__init__(L,R,U,D,C)
        self.N=N
        self.S=S
class testClass():
    def __init__(self,*args,**kwargs):
        print(args)
        print(kwargs)
def pprint(matrix):
    #print column count
    sys.stdout.write(f"  ")
    for i in range(0,len(matrix[0])):
        sys.stdout.write(f" {i} ")
    sys.stdout.write("\n")
    for i in range(0,len(matrix[0])+1):
        sys.stdout.write(f" - ")
    sys.stdout.write("\n")

    #print rows
    rows = list(range(0,len(matrix)))
    rowcount = 0
    for row in matrix:
        sys.stdout.write(f"{rows[rowcount]}|")
        for col in row:
            sys.stdout.write(f" {col} ")
        sys.stdout.write("\n")
        rowcount += 1
def testfillFromPaper():
    return [
        [0,0,1,0,1,1,0],
        [1,0,0,1,0,0,1],
        [0,1,1,0,0,1,0],
        [1,0,0,1,0,0,0],
        [0,1,0,0,0,0,1],
        [0,0,0,1,1,0,1]
    ]
def testFillFromLecture():
    return [
        [1,0,0,1,0,0,1],
        [1,0,0,1,0,0,0],
        [0,0,0,1,1,0,1],
        [0,0,1,0,1,1,0],
        [0,1,1,0,0,1,1],
        [0,1,0,0,0,0,1]
    ]

def ConvertMatrixToList():
    pass


if __name__ == "__main__":
    #Used for testing
    x = NodeObject(U=1,D=2,L=3,R=4,C=5)
    c = ColumnObject(D=2,L=3,R=4,C=5,N=6,S=7)
    #print(x.U)
    #print(c.U)
    x = testClass(1,2,3,4)