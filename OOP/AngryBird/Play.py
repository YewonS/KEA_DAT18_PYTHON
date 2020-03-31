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

    def makeMove(self, userInput):

        if userInput == 'd':
            self.bP[0] += 1
        elif userInput == 'r':
            self.bP[1] += 1
        elif userInput == 'l':
            self.bP[1] -= 1
        elif userInput == 'u':
            self.bP[0] -= 1

        print(f'Current bird position: ({self.bP[0]}, {self.bP[1]})')
        print(f'Current pig position: ({self.pP[0]}, {self.pP[1]})')
        return self.bP
    
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
print("Type in 'u' for up, 'r' for right, 'l' for left, 'd' for down. Type 'f' when you finished.")

finishGame = 'f'
userInput = ''
while(userInput != finishGame):
    userInput = input("Make your move: ").lower()
    playObject.makeMove(userInput)

playObject.calculateResult()
