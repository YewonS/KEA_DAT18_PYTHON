from random import randint

class Play():


    def __init__(self):
        x, y = 0, 0
        bP = []
        pP = []

    def generatePosition(self):

        positionsNo = []

        for r in range(4):
            positionsNo.append(randint(0,7))
        
        self.bP = [positionsNo[0], positionsNo[1]]
        self.pP = [positionsNo[2], positionsNo[3]]

    def printBoard(self):
    
        self.generatePosition()

        w, h = 8, 8

        matrix = [['*' for x in range(w)] for y in range(h)] 

        matrix[self.bP[0]][self.bP[1]] = 'B'
        matrix[self.pP[0]][self.pP[1]] = 'P'

        for x in range(w):
            print(matrix[x])

    def makeMove(self):

        x = self.bP[0]
        y = self.bP[1]

        switcher = {
            'u': y + 1,
            'r': x + 1,
            'l': x - 1,
            'd': y - 1
        }
        self.bp = [x, y]
        return switcher.get(self.bp)
    
    def calculateResult(self):
        if(self.bP == self.pP):
            print("You won!")
        else:
            print(f"You lost. Bird position: {self.bP[0]}, {self.bP[1]} vs Pig position: {self.pP[0]}, {self.pP[1]}.")


playObject = Play()

print("--------Angry Bird Game--------")
print("-------------------------------")

playObject.printBoard()

print("-------------------------------")
# print(f"Position of Bird: {bP[0]}, {bP[1]}. Position of Pig: {pP[0]}, {pP[1]}")
print("Type in 'u' for up, 'r' for right, 'l' for left, 'd' for down. Type 'f' when you finished.")

userInput = input("Make your move: ").lower()
while(userInput != 'f'):
    playObject.makeMove()

playObject.calculateResult()

    

