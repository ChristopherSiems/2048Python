import random
import pygame
from pygame.locals import *

class App2048:
    def __init__(self): #initializing board
        self.board = [[0] * 4, [0] * 4, [0] * 4,  [0] * 4] 
        self.status = 'Keep Playing'

    def preGameSetUp(self):
        #creates the 2 random '2's for the start of the game
        i = 0
        while i < 2:
            x = random.randrange(0,4)
            y = random.randrange(0,4)
            if self.board[y][x] == 0:
                self.board[y][x] = 2
                i += 1
            else:
                continue

    def __repr__(self):
        string = f'''{self.board[0][0]} {self.board[0][1]} {self.board[0][2]} {self.board[0][3]}
{self.board[1][0]} {self.board[1][1]} {self.board[1][2]} {self.board[1][3]} 
{self.board[2][0]} {self.board[2][1]} {self.board[2][2]} {self.board[2][3]}
{self.board[3][0]} {self.board[3][1]} {self.board[3][2]} {self.board[3][3]}
'''
        return string

    def define(self, b):
        self.board = b
    

    def pickTwoOrFour(self):
        '''This function will automatically generate 
        a 2 or a 4 after a move is made'''
        assigned = False
        while not assigned:
            x = random.randrange(0, 4)
            y = random.randrange(0, 4)
            if self.board[y][x] == 0:
                self.board[y][x] = random.choice((2, 4))
                assigned = True

    def upMove(self):
        # '''this function will move'''
        # for x in range(0, 4):
        #     shift = 0
        #     for y in range(0, 4):
        #         if self.board[y][x] == 0:
        #             shift += 1
        #         else:
        #             self.board[y - shift][x] = self.board[y][x]
        #             self.board[y][x] = 0
        # for x in range(0, 4):
        #     for y in range(3, 1, -1):
        #         # print(self.board[y][x])
        #         if self.board[y][x] != 0 and self.board[y][x] == self.board[y + 1][x]:
        #             self.board[y + 1][x] *= 2
        #             self.board[y][x] = 0

    def downMove(self):
        for ix, column in enumerate(self.board):
            for iy, item in enumerate(column):
                if 3 >= (ix + 1) and self.board[ix][iy] != 0:
                    if self.board[ix + 1][iy] == 0:
                        self.board[ix + 1][iy] = self.board[ix][iy]
                        self.board[ix][iy] = 0
                    elif self.board[ix][iy] == self.board[ix + 1][iy]:
                        self.board[ix + 1][iy] *= 2
                        self.board[ix][iy] = 0
            
        # '''this function will move dowm'''
        # for x in range(0,4):
        #     shift = 0
        #     for y in range(0, 4):
        #         if self.board[x + 1][y] == 0:
        #             shift += 1
        #         elif self.board[x + 1][y] == self.board[x][y]:
        #             self.board[x + 1][y] *= 2
        #             self.board[x][y] = 0
        #         else:
        #             self.board[x + shift][y] = self.board[x][y]
        #             self.board[x][y] = 0
    
    def leftMove(self):
        for ix, column in enumerate(self.board):
            for iy, item in enumerate(column):
                if 0 <= (iy - 1) and self.board[ix][iy] != 0:
                    if self.board[ix][iy - 1] == 0:
                        self.board[ix][iy - 1] = self.board[ix][iy]
                        self.board[ix][iy] = 0
                    elif self.board[ix][iy] == self.board[ix][iy - 1]:
                        self.board[ix][iy - 1] *= 2
                        self.board[ix][iy] = 0
        # '''this function will move left'''
        # for y in range(0, 4):
        #     shift = 0
        #     for x in range(0, 4):
        #         if self.board[x][y - 1] == 0:
        #             shift += 1
        #         elif self.board[x][y - 1] == self.board[x][y]:
        #             self.board[x][y - 1] *= 2
        #             self.board[x][y] = 0
        #         else:
        #             self.board[x][y - 1] = self.board[x][y]
        #             self.board[x][y] = 0
                
        


game1 = App2048()
game1.preGameSetUp()
print(f'pregame set up: \n{game1}')
game1.upMove()
print(f'up move: \n{game1}')
game1.pickTwoOrFour()
print(f'pick two or four: \n{game1}')
game1.downMove()
print(f'down move: \n{game1}')
game1.pickTwoOrFour()
print(f'pick two or four: \n{game1}')
game1.leftMove()
print(f'left move: \n{game1}')
game1.pickTwoOrFour()
print(f'pick two or four: \n{game1}')
game1.downMove()
print(f'down move: \n{game1}')
game1.pickTwoOrFour()
print(f'pick two or four: \n{game1}')
game1.upMove()
print(f'up move: \n{game1}')
game1.pickTwoOrFour()
print(f'pick two or four: \n{game1}')