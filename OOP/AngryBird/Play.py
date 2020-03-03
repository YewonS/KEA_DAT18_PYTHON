# import Board

class Play():

    x, y = 0, 0
    bP = []
    pP = []

    
    w, h = 8, 8

    def printBoard(self, bP, pP):
    
        matrix = [['*' for x in range(w)] for y in range(h)] 

        matrix[bPx][bPy] = 'B'
        matrix[pPx][pPy] = 'P'

        for x in range(w):
            print(matrix[x])

    def generatePosition(self):

        positionsNo = []

        for r in range(4):
            positionsNo.append(random.randint(0,7))
        
        bP = [positionsNo[0], positionsNo[1]]
        pP = [positionsNo[2], positionsNo[3]]

    def makeMove(self, bP):

        x = bP[0]
        y = bP[1]

        switcher={
            'f': y + 1,
            'r': x + 1,
            'l': x - 1,
            'b': y - 1
        }
        bp = [x, y]
        return switcher.get(bp)
    
    def calculateResult(self, bP, pP):
        if(bP == pP):
            print("You won!")
        else:
            print(f"You lost. Bird position: {bP[0]}, {bP[1]} vs Pig position: {pP[0]}, {pP[1]}.")
        
        



    print("--------Angry Bird Game--------")
    print("-------------------------------")

    generatePosition()

    printBoard(bP, pP)

    print("-------------------------------")
    print(f"Position of Bird: {bP[0]}, {bP[1]}. Position of Pig: {pP[0]}, {pP[1]}")
    print("Type in 'f' for forward, 'r' for right turn, 'l' for left turn, 'b' for backward. Type 'f' when you finished.")

    userInput = input("Make your move: ").lower()
    while(userInput != 'f'):
        makeMove(bP)
    
    calculateResult(bP, pP)

    

