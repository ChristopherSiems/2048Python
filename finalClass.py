import random
import pygame
from pygame.locals import *

class App2048:
    def __init__(self): #initializing board
        self.board = [[0] * 4, [0] * 4, [0] * 4,  [0] * 4] 
        self.status = 'Keep Playing'

    def __repr__(self):
        string = f'''{self.board[0][0]} {self.board[1][0]} {self.board[2][0]} {self.board[3][0]}
{self.board[0][1]} {self.board[1][1]} {self.board[2][1]} {self.board[3][1]} 
{self.board[0][2]} {self.board[1][2]} {self.board[2][2]} {self.board[3][2]}
{self.board[0][3]} {self.board[1][3]} {self.board[2][3]} {self.board[3][3]}
'''
        return string

    def define(self, b):
        self.board = b
    
    def updateGameStatus(self):
        '''There are three different possible game status
            1. Win
                - If any of the tiles equal 2048
            2. Lose
                - If there are no possible mergers
                - There is so value 0 on the board
            3. Play
                - If there are possible mergers 
                - If there is space to play like values with 0
            '''
        
        for row in self.board:
            for column in self.board:
                
                #This if-statement determines if the user has won the game
                if self.board[row][column] == 2048:
                    return 'You Win!'
                
                #This if statement determines if there is a possible merger in the row or column
                if (column != 3 and self.board[row][column] == self.board[row][column+1]) \
                    or (row != 3 and self.board[row][column] == self.board[row+1][column]):
                    return 'Keep Playing'
                
                #This elif statement will determine if there is no zero in the 
                #board knowing there is no merger possible
                elif 0 not in self.board:
                    return 'You Lose :('
                
                #If there is no merger but there are 0, then 
                else:
                    return 'Keep Playing'
        
    
    def pickTwoOrFour(self):
        '''This function will automatically generate 
        a 2 or a 4 after a move is made'''

        assigned = False
        while not assigned:
            x = random.randrange(0, 4)
            y = random.randrange(0, 4)
            if self.board[x][y] == 0:
                self.board[x][y] = random.choice((2,4))
                assigned = True

    def up(self):
        for ix, column in enumerate(self.board):
            for iy, item in enumerate(column):
                if item != 0:
                    if 0 <= iy - 1 < len(column):
                        if item == self.board[ix][iy - 1]:
                            self.board[ix][iy - 1] *= 2
                        # else:
                            


    def rightMove(self):
        for row in range(4):
            for column in range(3,0,-1):
                if self.board[row][column] == self.board[row][column - 1] and self.board[row][column] != 0:
                    self.board[row][column] *= 2
                    self.board[row][column - 1] = 0
                    column = 0


game1 = App2048()
print(game1)
game1.pickTwoOrFour()
print(game1)