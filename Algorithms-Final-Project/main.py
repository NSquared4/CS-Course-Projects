# Nussinov.py

class NussinovMatrix ():
  """
  Once the NussinovMatrix() is called with an input of an rnaString (list of Strings), it will create and solve the Nussinov matrix and print the solutions. For specific output details, check the README.
  """
  def __init__(self, rnaString):
    self.dimension = len(rnaString)
    self.matrix = [] #nxn empty matrix
    self.solution = []
    self.rnaString = rnaString
    self.pointers = []
    self.createMatrix()
    self.initializeZeros()
    self.fillMatrix()
    self.traceBack()
    self.printSolution()
  
  """
    Create a matrix of size n x n and initialize it to 'x'
    Ex. 5x5 [[x,x,x,x,x], 
             [x,x,x,x,x],
             [x,x,x,x,x],
             [x,x,x,x,x],
             [x,x,x,x,x]]
  """
  def createMatrix(self):
    if (self.dimension <= 1):
      print("RNA sequence not long enough. Must be >= 2")
    self.matrix=[[0] * self.dimension for i in range(self.dimension)]
  
  """
    Initialize the two diagonals of 0 in self.matrix
    Ex. 5x5 [[0, , , , ],
             [0,0, , , ],
             [ ,0,0, , ],
             [ , ,0,0, ],
             [ , , ,0,0]]

  """
  def initializeZeros(self):
    """
    Initialize the 1st diagonals of 0
    Ex. 5x5 [[0, , , , ],
             [ ,0, , , ],
             [ , ,0, , ],
             [ , , ,0, ],
             [ , , , ,0]]
    """
    for i in range(self.dimension):
      for j in range(self.dimension):
        if(i == j):
          self.matrix[i][j] = 0
    
    """
    Initializes the 2nd diagonal of 0 
    Ex. 5x5 [[ , , , , ],
             [0, , , , ],
             [ ,0, , , ],
             [ , ,0, , ],
             [ , , ,0, ]]
    """
    for i in range(1, self.dimension):
        for j in range(self.dimension-1):
          if(j == i-1):
            self.matrix[i][j] = 0; 

  """
  Given two specific indices i and j, the function will check the scoring of the two characters as pairs in the rnaString at the given indices.
  """
  def checkPairScore(self, i, j):
    # Our scoring: 
    # "A" and "U" = 1
    # "G" and "C" = 1
    value1 = self.rnaString[i]
    value2 = self.rnaString[j]
    if (value1 == "A" and value2 == "U"):
      return 1
    elif (value1 == "U" and value2 == "A"):
      return 1
    elif (value1 == "G" and value2 == "C"):
      return 1
    elif (value1 == "C" and value2 == "G"):
      return 1
    else:
      return 0

  """
  Given a pairscore (From checkPairScore likely) of the pairs i and j, this function calculates the max score of substring i and j using our reccurence relation. Note: All of the subproblems must be solved prior to calling this function.
  """
  def checkGridScore(self, i, j, pairScore):
    #Checks for the max value scoring for our grid
    # S(i+1,j-1) + w(i,j)
    includingPairij = self.matrix[i+1][j-1] + pairScore
    # for i <= k < j: S(i,k) + S(k+1,j)
    max_score = includingPairij
    for k in range(i, j):
      tempScore = self.matrix[i][k] + self.matrix[k+1][j]
      if max_score < tempScore:
        max_score = tempScore
    return max_score
    
  """
  Fills the upper half of the matrix diagonal by diagonal using checkPairScore() and checkGridScore().
  """
  def fillMatrix(self):
		#Fill in the rest of the printMatrix
    for diagonalCount in range(1, self.dimension):
      for i in range(self.dimension - diagonalCount):
        # Scoring (A,U) = 1, (G,C) = 1, otherwise 0
        # Current grid i = i, j = i+diagonalCount
        # self.matrix[i][i+diagonalCount] = 1 
        pairScore = self.checkPairScore(i, (i+diagonalCount))
        gridScore = self.checkGridScore(i,(i + diagonalCount), pairScore)
        self.matrix[i][i+diagonalCount] = gridScore
 
  """
  Prints the matrix. We use 0s for the lower half for printing purposes but these should be empty.
  """
  def printMatrix(self):
    for i in range(self.dimension):
      print(self.matrix[i])

  """
  Traceback function retains the solution (specific pairings) from the matrix. Starts from matrix[1][n] follow the pointers to the end to obtain the path that gives the max pairs. Returns the indices of the letters in the rnaString list that are paired
  """
  def traceBack(self):
    stack = []
    stack.append((0,self.dimension-1))
    while (len(stack) != 0):
      curr_location = stack.pop()
      i = curr_location[0]
      j = curr_location[1]
      valueOfGrid = self.matrix[i][j]
      if (i >= j):
        continue
      elif (valueOfGrid == self.matrix[i+1][j]):
        # push onto stack
        stack.append((i+1,j))
      elif (valueOfGrid == self.matrix[i][j-1]):
        # push onto stack
        stack.append((i,j-1))
      elif (valueOfGrid == (self.matrix[i+1][j-1]+1)):
        #push and record
        stack.append((i+1,j-1))
        self.solution.append((i,j))
      else:
        for k in range(i+1,j-1):
          if (valueOfGrid == (self.matrix[i][k] + self.matrix[k+1][j])):
            stack.append((k+1,j))
            stack.append((i,k))
            break
  
  """
  Prints the pairing we found from traceback. The solution includes the original RNA string and the bracket notation representing pairings.
  """
  def printSolution(self):
    arr = ["*"] * self.dimension
    for i in self.solution:
      arr[i[0]] = "("
      arr[i[1]] = ")"
    self.printMatrix()
    print("".join(self.rnaString))
    print("".join(arr))
  

def main():
  # test
  file = open("sequence.txt","r")
  string = file.readlines()
  file.close()
  for i in range(len(string)):
    NussinovMatrix(string[i].strip("\n").split(" "))

  #The tests we used.
  #a.printMatrix()
  #print(a.solution)
  #a.printSolution()
  #b = NussinovMatrix(["G","C","A","C","G","A","C","G"])
  #b.printMatrix()
  #print(b.solution)
  #b.printSolution()
  #c = NussinovMatrix(["G","G","G","A","A","A","U","C", "C"])
  #c.printMatrix()
  #print(c.solution)
  #c.printSolution()
  #clear idea for output: matrix & indices

main()