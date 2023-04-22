import random

class App2048:
    def __init__(self): #initializing board
        self.board = [[0] * 4, [0] * 4, [0] * 4,  [0] * 4] 

    def __repr__(self):
        string = f'''{self.board[0][0]} {self.board[0][1]} {self.board[0][2]} {self.board[0][3]}
{self.board[1][0]} {self.board[1][1]} {self.board[1][2]} {self.board[1][3]} 
{self.board[2][0]} {self.board[2][1]} {self.board[2][2]} {self.board[2][3]}
{self.board[3][0]} {self.board[3][1]} {self.board[3][2]} {self.board[3][3]}
'''
        return string

    def define(self, b):
        self.board = b
    
    def copy(self):
        new_board = self.board
        return new_board
    
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
    
    def check(self):
        for y in range(0,4):
            for x in range(0,4):
                if self.board[y][x] == self.board[y + 1] or self.board[y][x] == self.board[y][x + 1]:
                    return True
        for y in range(0, 4):
            if 0 in self.board[y]:
                return True
        return False

    def upMove(self):
        '''this function will move up'''
        for x in range(0, 4):
            shift = 0
            for y in range(0, 4):
                if self.board[y][x] == 0:
                    shift += 1
                elif shift == 0:
                    continue
                else:
                    self.board[y - shift][x] = self.board[y][x]
                    self.board[y][x] = 0
        for x in range(0, 4):
            for y in range(0, 3):
                if self.board[y][x] != 0 and self.board[y][x] == self.board[y + 1][x]:
                    self.board[y][x] *= 2
                    self.board[y + 1][x] = 0

    def downMove(self):   
        '''this function will move down'''
        for x in range(0, 4):
            shift = 0
            for y in range(3, -1, -1):
                if self.board[y][x] == 0:
                    shift += 1
                elif shift == 0:
                    continue
                else:
                    self.board[y + shift][x] = self.board[y][x]
                    self.board[y][x] = 0
        for x in range(0, 4):
            for y in range(3, 0, -1):
                if self.board[y][x] != 0 and self.board[y][x] == self.board[y - 1][x]:
                    self.board[y][x] *= 2
                    self.board[y - 1][x] = 0
    
    def leftMove(self):
        '''this function will move left'''
        for y in range(0, 4):
            shift = 0
            for x in range(0, 4):
                if self.board[y][x] == 0:
                    shift += 1
                elif shift == 0:
                    continue
                else:
                    self.board[y][x - shift] = self.board[y][x]
                    self.board[y][x] = 0
        for y in range(0, 4):
            for x in range(0, 3):
                if self.board[y][x] != 0 and self.board[y][x] == self.board[y][x + 1]:
                    self.board[y][x] *= 2
                    self.board[y][x + 1] = 0

    def rightMove(self):
        '''this function goes right'''
        for y in range(0, 4):
            shift = 0
            for x in range(3, -1, -1):
                if self.board[y][x] == 0:
                    shift += 1
                elif shift == 0:
                    continue
                else:
                    self.board[y][x + shift] = self.board[y][x]
                    self.board[y][x] = 0
        for y in range(0, 4):
            for x in range(3, 0, -1):
                if self.board[y][x] != 0 and self.board[y][x] == self.board[y][x - 1]:
                    self.board[y][x] *= 2
                    self.board[y][x - 1] = 0
    
    def fullUp(self):
        self.upMove()
        self.upMove()
        self.upMove()
        self.upMove()
        self.upMove()
    
    def fullDown(self):
        self.downMove()
        self.downMove()
        self.downMove()
        self.downMove()
        self.downMove()

    def fullLeft(self):
        self.leftMove()
        self.leftMove()
        self.leftMove()
        self.leftMove()
        self.leftMove()
    
    def fullRight(self):
        self.rightMove()
        self.rightMove()
        self.rightMove()
        self.rightMove()
        self.rightMove()
    

    def copy(self):
        new_board = App2048()
        return new_board