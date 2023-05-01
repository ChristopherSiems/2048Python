'''Game Logic file has all the functions necessary to make all the moves in the game and make it playable'''
#importing necessary modules for the game
import random

'''this Class creates the board and all its properties such as the score, the move name, and the values in the board'''
class App2048:

    '''initializing board, score, and the move name'''
    def __init__(self): 
        #board starts off as all values being 0
        #score starts of being 0
        #move name starts off as None because no move has been made yet
        self.board = [[0] * 4, [0] * 4, [0] * 4,  [0] * 4]
        self.score = 0
        self.move_name = 'None'

    '''creates the string that prints the board to the terminal or retuns it when called in the main_game.py file'''
    def __repr__(self):
        string = f'''{self.board[0][0]} {self.board[0][1]} {self.board[0][2]} {self.board[0][3]}
{self.board[1][0]} {self.board[1][1]} {self.board[1][2]} {self.board[1][3]} 
{self.board[2][0]} {self.board[2][1]} {self.board[2][2]} {self.board[2][3]}
{self.board[3][0]} {self.board[3][1]} {self.board[3][2]} {self.board[3][3]}
'''
        return string

    '''Allows us to define the board however we want
            Currently used as a way to clear the board for a new game if the user chooses to reset and play again
            Was used previously as a way to test specific moves based on certain situations'''
    def define(self, b):
        self.board = b
    
    '''Creates a copy of the board
            Used in the main_game.py as a way to compare the copied board to the modified board to make sure a change was made'''
    def copy(self):
        c = [[0] * 4, [0] * 4, [0] * 4,  [0] * 4]
        for y in range(4):
            for x in range(4):
                c[y][x] = self.board[y][x]
        return c
    
    '''Pregame set up adds two '2's into the game in random positions'''
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
    
    '''This method will automatically generate a 2 or a 4 after 
        1. a move is made
        2. if the board was actually modifed with the move made'''
    def pickTwoOrFour(self):
        assigned = False
        while not assigned:
            x = random.randrange(0, 4)
            y = random.randrange(0, 4)
            if self.board[y][x] == 0:
                self.board[y][x] = random.choice((2, 4))
                assigned = True

    '''This method will compare if the values on the board have changed
    Reason why:
        1. Determines if we add the pickTwoOrFour() after the move is done
        2. Makes sure the user isn't cheating the game'''
    def compare(self, other):
        for y in range(4):
            for x in range(4):
                if self.board[y][x] != other[y][x]:
                    return False
        return True
    
    '''This method checks to see if the game is playable
    Game is playable if 
        1. There are any possible merges
        2. Any of the spaces are 0
    If both of these are False, then the game is considered over'''
    def check(self):
        for y in range(4):
            for x in range(4):
                # check if a merge is possible
                if x != 3 and self.board[y][x] == self.board[y][x+1] or \
                    y != 3 and self.board[y][x] == self.board[y + 1][x]:
                    return True
        for y in range(0, 4):
                if 0 in self.board[y]:
                    return True
        return False

    '''This method controls the up move (when up arrow or 'w' is pressed)
    moves all the values up and if merge can happen, merges the cells up and the value below becomes 0'''
    def upMove(self):

        #move name is up, which will be displayed on the side bar
        self.move_name = 'Up'

        #This for loop shifts all the values up if the value above is 0
            #utilizes a shift variable that increases by 1 for every value above is 0
                #once it sees a value above thats not 0, impliments its specific shift value 
                #and subracts it from the y value, causing the value to go up
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

        #This for loop checks to see if the value below it is the same value
            #If so, then the current value gets multiplied by 2 and the value below becomes 0
        for x in range(0, 4):
            for y in range(0, 3):
                if self.board[y][x] != 0 and self.board[y][x] == self.board[y + 1][x]:
                    self.board[y][x] *= 2
                    self.score += self.board[y][x]
                    self.board[y + 1][x] = 0

    '''This method controls the down move (when down arrow or 's' is pressed)
    moves all the values down and if merge can happen, merges the cells down and the value above becomes 0'''
    def downMove(self):   

        #move name is up, which will be displayed on the side bar
        self.move_name = 'Down'

        #This for loop shifts all the values down if the value below is 0
            #utilizes a shift variable that increases by 1 for every value below is 0
                #once it sees a value below thats not 0, impliments its specific shift value 
                #and adds it from the y value, causing the value to go down
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
        
        #This for loop checks to see if the value above it is the same value
            #If so, then the current value gets multiplied by 2 and the value above becomes 0
        for x in range(0, 4):
            for y in range(3, 0, -1):
                if self.board[y][x] != 0 and self.board[y][x] == self.board[y - 1][x]:
                    self.board[y][x] *= 2
                    self.score += self.board[y][x]
                    self.board[y - 1][x] = 0

    '''This method controls the left move (when left arrow or 'a' is pressed)
    moves all the values to the left and if merge can happen, merges the cells left and the value on the right becomes 0''' 
    def leftMove(self):

        #move name is left, which will be displayed on the side bar
        self.move_name = 'Left'

        #This for loop shifts all the values to the left if the value leftwards is 0
            #utilizes a shift variable that increases by 1 for every value leftward is 0
                #once it sees a value leftward thats not 0, impliments its specific shift value 
                #and subtract it from the x value, causing the value to go to the left
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

        #This for loop checks to see if the value to the left is the same value
            #If so, then the current value gets multiplied by 2 and the value to the left becomes 0
        for y in range(0, 4):
            for x in range(0, 3):
                if self.board[y][x] != 0 and self.board[y][x] == self.board[y][x + 1]:
                    self.board[y][x] *= 2
                    self.score += self.board[y][x]
                    self.board[y][x + 1] = 0

    '''This method controls the right move (when right arrow or 'd' is pressed)
    moves all the values to the right and if merge can happen, merges cells right and the value on the lefr becomes 0'''
    def rightMove(self):

        #move name is up, which will be displayed on the side bar
        self.move_name = 'Right'

        #This for loop shifts all the values to the right if the value rightwards is 0
            #utilizes a shift variable that increases by 1 for every value rightward is 0
                #once it sees a value rightward thats not 0, impliments its specific shift value 
                #and adds it from the x value, causing the value to go to the right
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

        #This for loop checks to see if the value to the right is the same value
            #If so, then the current value gets multiplied by 2 and the value to the right becomes 0
        for y in range(0, 4):
            for x in range(3, 0, -1):
                if self.board[y][x] != 0 and self.board[y][x] == self.board[y][x - 1]:
                    self.board[y][x] *= 2
                    self.score += self.board[y][x]
                    self.board[y][x - 1] = 0
    
    '''Completes the up move by calling the upMove() 5 times'''
    def fullUp(self):
        self.upMove()
        self.upMove()
        self.upMove()
        self.upMove()
        self.upMove()
    
    '''Completes the down move by calling the downMove() 5 times'''    
    def fullDown(self):
        self.downMove()
        self.downMove()
        self.downMove()
        self.downMove()
        self.downMove()

    '''Completes the left move by calling the leftMove() 5 times'''
    def fullLeft(self):
        self.leftMove()
        self.leftMove()
        self.leftMove()
        self.leftMove()
        self.leftMove()
    
    '''Completes the right move by calling the rightMove() 5 times'''
    def fullRight(self):
        self.rightMove()
        self.rightMove()
        self.rightMove()
        self.rightMove()
        self.rightMove()
