import sys
class NodeObject():
    def __init__(self,L=None,R=None,U=None,D=None,C=None,I="default"):
        self.L=L
        self.R=R
        self.D=D
        self.U=U
        self.C=C
        self.I=I
    def __str__(self):
        return str(self.I)

class ColumnNode( NodeObject ):
    def __init__(self,N="defaultName",S=-1):
        super().__init__()
        self.N=N
        self.S=S
    def __str__(self):
        return str(self.N)


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


def createColumnHeaders(Matrix):
    """ from 2d array create column headers for the link list structure

    :param Matrix: 2d python array of 1's and 0's
    
    :return: the root element of the linked list structure
    :rtype: ColumnNode
    """

    def makeColumnNodes(n):
        if n == 0:
            return ColumnNode(N=n,S=0)
        a = ColumnNode(N=n,S=0) 
        a.L = makeColumnNodes( n-1 )
        return a

    columnCount = len(Matrix[0])-1
    root = ColumnNode(N="root")
    a = makeColumnNodes(columnCount)
    
    nxt = a
    while nxt.L:
        nxt.L.R = nxt
        nxt = nxt.L
    #append root
    root.L = a
    root.R = nxt 
    return root

def connectRowsFromRowList(rowArray):
    """connects rows based on rowArray

    :param rowArray: Array of zeros and NodeObjects 
    
    :return: None
    """
    First = None
    prev = None
    for i in rowArray:
        if i != 0:
            #sets Right value of current element
            i.R = prev
            prev = i
            #set left Node
            if i.R != None:
                i.R.L = i
            if First == None:
                First =i
    First.R = prev
    prev.L = First


def createRows(rootNode,Matrix):
    """Loops over matrix adding nodes for each one"

    :param rootNode: ColumnNode 
    :param Matrix: 2d python array of 1's and 0's
    
    :return: None
    """

    for row in Matrix:
        #generate the nessacary Node objects
        #storing them in an array lets us generate them and keep track of their column number
        rowArray = [0 for i in row]
        for i in range(len(row)):
            if row[i] == 1:
                rowArray[i] = NodeObject(I=i)
        #link them up horizontally

        connectRowsFromRowList(rowArray)
        #link them to column headers
        
        #Testing
        for i in rowArray:
            if i != 0:
                print(i.R,i,i.L)
        break
        
        


def ConvertMatrixToList(Matrix):
    """Converts a 2d python array into a structure of linked lists based on Donal E. Knuths paper "Dancing Links"

    :param Matrix: 2d python array of 1's and 0's
    
    :return: the root element of the linked list structure
    :rtype: ColumnNode
    """
    rootHeader = createColumnHeaders(Matrix)
    
    
    


if __name__ == "__main__":
    #Used for testing
    A = testFillFromLecture()
    node = NodeObject(L=22)
    col = ColumnNode(N="bob")
