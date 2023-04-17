import random

class App2048:
    
    def __init__(self): #initializing board
        self.board = [[0] * 4] * 4

    def __repr__(self):
        string = f'''{self.board[0][0]} {self.board[1][0]} {self.board[2][0]} {self.board[3][0]}
{self.board[0][1]} {self.board[1][1]} {self.board[2][1]} {self.board[3][1]} 
{self.board[0][2]} {self.board[1][2]} {self.board[2][2]} {self.board[3][2]}
{self.board[0][3]} {self.board[1][3]} {self.board[2][3]} {self.board[3][3]}
'''
        return string

    def define(self, b):
        self.board = b
    
    def step(self):
        assigned = False
        while not assigned:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            print(x)
            print(y)
            if self.board[x][y] == 0:
                self.board[x][y] = random.choice(2,4)
                assigned = True

    '''def up(self):
        for ix, column in enumerate(self.board):
            for iy, num in enumerate(column):
                if iy != 0:
                    for other in column[:iy:-1]:
                        if num == other:'''

    '''def right(self):
        for column in range(4):
            for row in range(4):
                if self.board[row][column] == 0:
                    for num in range(row,-1):
                        if num != 0:'''

game1 = App2048()
print(game1)
game1.step()
print(game1)