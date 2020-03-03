class Board:

    w, h = 8, 8

    def printBoard(self, bPx, bPy, pPx, pPy):
    
        matrix = [['*' for x in range(w)] for y in range(h)] 

        matrix[bPx][bPy] = 'B'
        matrix[pPx][pPy] = 'P'

        for x in range(w):
            print(matrix[x])
