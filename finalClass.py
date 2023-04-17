import random

class App2048:
    def __init__(self): #initializing board
        self.board = [[0] * 4, [0] * 4, [0] * 4,  [0] * 4] 

    def __repr__(self):
        string = f'''{self.board[0][0]} {self.board[1][0]} {self.board[2][0]} {self.board[3][0]}
{self.board[0][1]} {self.board[1][1]} {self.board[2][1]} {self.board[3][1]} 
{self.board[0][2]} {self.board[1][2]} {self.board[2][2]} {self.board[3][2]}
{self.board[0][3]} {self.board[1][3]} {self.board[2][3]} {self.board[3][3]}
'''
        return string

    def define(self, b):
        self.board = b
    
    def pickTwoOrFour(self):
        assigned = False
        while not assigned:
            x = random.randrange(0, 4)
            y = random.randrange(0, 4)
            if self.board[x][y] == 0:
                self.board[x][y] = random.choice(2, 4)
                assigned = True

    def up(self):
        for ix, column in enumerate(self.board):
            for iy, item in enumerate(column):
                if item != 0:
                    if 0 <= iy - 1 < len(column):
                        if item == self.board[ix][iy - 1]:
                            self.board[ix][iy - 1] = item * 2
                        else:


                    



    def rightMove(self):
        for row in range(4):
            for column in range(3,0,-1):
                if self.board[row][column] == self.board[row][column - 1] and self.board[row][column] != 0:
                    self.board[row][column] *= 2
                    self.board[row][column - 1] = 0
                    column = 0


game1 = App2048()
print(game1)
game1.step()
print(game1)