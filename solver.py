# -*- coding: utf-8 -*-
import random
class Genotype:
    def __init__(self, board):
        self.board = board
        self.fitness = self.getFitness()
    
    def getFitness(self):
        fit = 0
        for i in range(0,9):
            fit += 9 - len(set(self.board.get_row(i))) + 9 - len(set(self.board.get_col(i)))
            
        self.fitness = fit
        return self.fitness
        
        
class Board:
    def __init__(self, grids, mask):
        self.grids = grids
        self.mask = mask
                
        
    def get_row(self, index):
        row = []
        for i in range (0,3):
            for item in self.grids[i + index - index%3][3*(index%3):3*(index%3+1)]:
                row.append(item)
        return row
        
    def get_col(self, index):
        col = []
        for i in range(0,3):
            for j in range(0,3):
                col.append(self.grids[index//3 + 3*i][index%3 + 3*j])
        return col
    
    def random_swap(self):
        gridIndex = random.sample(range(0,9), 1)[0]
        
        grid = self.grids[gridIndex]
        possibleSwaps = [i for i, x in enumerate(self.mask[gridIndex]) if x]
        #print(mask)
        
        fst, sec = random.sample(possibleSwaps, 2)
        print('Swapping ', fst, ' and ', sec, ' in grid ', gridIndex)
        temp = grid[fst]
        grid[fst] = grid[sec]
        grid[sec] = temp
    
    def printBoard(self):
        print('*'*41)
        for i in range(0,9):
            line = '|| '
            for j in range(0,9):
                if(j%3 != 2):
                    line += str(self.get_row(i)[j]) + ' | '
                else:
                    line += str(self.get_row(i)[j]) + ' || '
            print(line)
            #print('-'*37)
            if(i%3 == 2):
                print('*'*41)
            else:
                print('-'*41)
     
def maskBoard(grids):
    mask = []
    for grid in grids:
        newGrid = []
        for num in grid:
            newGrid.append(True if num == 0 else False)
        mask.append(newGrid)
        
    return mask

def randomiseBoard(grids):
    randBoard = []
    for grid in grids:
        newGrid = []
        missing = list(set(range(1,10)) - set(grid))
        random.shuffle(missing)
        for i in range(0,9):
            newGrid.append([missing.pop() if grid[i] == 0 else grid[i]])
            
        randBoard.append(newGrid)
    return randBoard

a = [[7,3,5,8,4,2,9,1,6],
     [6,1,4,9,7,3,2,8,5],
     [8,9,2,5,6,1,3,7,4],
     [2,8,6,4,1,3,5,7,9],
     [3,4,9,8,5,7,1,2,6],
     [1,5,7,9,2,6,4,3,8],
     [1,5,7,6,9,4,3,2,8],
     [4,9,2,7,3,8,5,6,1],
     [6,8,3,2,1,5,7,4,9]]

sudoku = [
            [0,0,6,3,0,0,0,5,0],
            [0,2,7,4,0,6,0,0,0],
            [0,0,0,0,0,9,7,0,4],
            [0,0,0,0,9,0,8,0,7],
            [0,0,2,1,6,0,3,0,0],
            [9,1,8,0,0,0,2,0,0],
            [0,3,9,7,0,0,0,2,0],
            [6,0,5,0,1,0,0,4,0],
            [0,0,0,0,3,0,0,9,7]
        ]

mask = maskBoard(sudoku)
a[0][3:6]
randomiseBoard(sudoku)
a[1//3]

b = Board(sudoku, mask)
b.printBoard()
print()
b.random_swap()
b.printBoard()
for i in range(0,9):
    print(b.get_col(i))
b.get_row(0)
b.get_col(8)

test = [1,2,3,4,5,6,7]


g = Genotype(b)

g.getFitness()

print(list(set(range(1,10)) - set([0, 1, 5, 10])))

board = []
for i in range(0,9):
    board.append(random.sample(range(1,10), 9))
    
gene = Genotype(Board(board))
gene.fitness

gene.getFitness()
for i in range(0,9):
    print(Board(board).get_row(i))
    
b1 = Board(board)
b1.printBoard()
b1.random_swap()
print()
b1.printBoard()