from random import randint

class Sudoku:
    LENGTH = 9
    EMPTY = 0

    def __init__(self):
        self.generateBoard()
    
    def emptyArray(self):
        return [self.EMPTY for i in range(self.LENGTH)]

    def emptyMatrix(self):
        return [self.emptyArray() for i in range(self.LENGTH)]
    
    def generateBoard(self):
        self.rows = self.emptyMatrix()

    def getRows(self):
        return self.rows
    
    def getColumns(self):
        columns = self.emptyMatrix()
        for i in range(self.LENGTH):
            for j in range(self.LENGTH):
                columns[i][j] = self.getRows()[j][i]
        return columns
    
    def getBlocks(self):
        blocks = self.emptyMatrix()
        for i in range(self.LENGTH):
            for j in range(self.LENGTH):
                blocks[i][j] = self.getRows()[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]
        return blocks
    
    def getEmptyCells(self):
        arr = []
        for i in range(self.LENGTH):
            for j in range(self.LENGTH):
                arr.append([i, j]) if self.getRows()[i][j] == self.EMPTY else ''
        return arr
    
    def isInRow(self, num, row):
        return num in self.getRows()[row]

    def isInColumn(self, num, column):
        return num in self.getColumns()[column]

    def isInBlock(self, num, block):
        return num in self.getBlocks()[block]
    
    def isPlaceble(self, num, row, col):
        return not (self.isInRow(num,row) or self.isInColumn(num,col) or self.isInBlock(num,row // 3 * 3 + col // 3))

    def setNumber(self, num, row, col):
        self.getRows()[row][col] = num if self.isPlaceble(num, row, col) else self.EMPTY

    def placeRandomNumber(self, row, col):
        nums = [num for num in range(1, 10)]
        num = nums.pop(randint(0, len(nums) - 1))
        while not self.isPlaceble(num, row, col) and len(nums) > 0:
            num = nums.pop(randint(0, len(nums) - 1))
        self.setNumber(num, row, col)
    
    def randomize(self):
        while len(self.getEmptyCells()) > 2:
            self.generateBoard()
            self.randomizeEmptyCells()
    
    def randomizeEmptyCells(self):
        emptyCells = self.getEmptyCells()
        while len(emptyCells) > 0:
            self.placeRandomNumber(*emptyCells.pop())

    def printHDivider(self):
        print('+ - - - + - - - + - - - +')
    
    def printRow(self, numRow):
        row = '| '
        for i in range(self.LENGTH):
            row += f'{self.getRows()[numRow][i]} ' + ('| ' if (i % 3 == 2) else '')
        print(row)
    
    def printBoard(self):
        self.printHDivider()
        for i in range(self.LENGTH):
            self.printRow(i)
            self.printHDivider() if i % 3 == 2 else ''

sudoku = Sudoku()
sudoku.randomize()
print(sudoku.getEmptyCells())
sudoku.printBoard()