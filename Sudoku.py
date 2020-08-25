from random import randint

class Sudoku:
    def __init__(self):
        self.generateBoard()
    
    def emptyArray(self):
        return [0 for i in range(9)]

    def emptyMatrix(self):
        return [self.emptyArray() for i in range(9)]
    
    def generateBoard(self):
        self.rows = self.emptyMatrix()

    def getRows(self):
        return self.rows
    
    def getColumns(self):
        columns = self.emptyMatrix()
        for i in range(9):
            for j in range(9):
                columns[i][j] = self.rows[j][i]
        return columns
    
    def getBlocks(self):
        blocks = self.emptyMatrix()
        for i in range(9):
            for j in range(9):
                blocks[i][j] = self.rows[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]
        return blocks
    
    def isInRow(self, num, row):
        return num in self.getRows()[row]

    def isInColumn(self, num, column):
        return num in self.getColumns()[column]

    def isInBlock(self, num, block):
        return num in self.getBlocks()[block]
    
    def isPlaceble(self, num, row, col):
        return not (self.isInRow(num,row) or self.isInColumn(num,col) or self.isInBlock(num,row // 3 * 3 + col // 3))

    def placeRandomNumber(self, row, col):
        nums = [num for num in range(1, 10)]
        num = nums.pop(randint(0, len(nums) - 1))
        while not self.isPlaceble(num, row, col) and len(nums) > 0:
            num = nums.pop(randint(0, len(nums) - 1))
        self.rows[row][col] = num if self.isPlaceble(num, row, col) else ' '
    
    def randomize(self):
        for i in range(9):
            for j in range(9):
                self.placeRandomNumber(i, j)

    def printHDivider(self):
        print('+ - - - + - - - + - - - +')
    
    def printRow(self, numRow):
        row = '| '
        for i in range(len(self.rows[numRow])):
            row += f'{self.rows[numRow][i]} ' + ('| ' if (i % 3 == 2) else '')
        print(row)
    
    def printBoard(self):
        self.printHDivider()
        for i in range(len(self.rows)):
            self.printRow(i)
            self.printHDivider() if i % 3 == 2 else ''

sudoku = Sudoku()
sudoku.randomize()
sudoku.printBoard()