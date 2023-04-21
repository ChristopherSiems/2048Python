from game_logic import App2048
import sys
import json
import pygame
from pygame.locals import *

# set up pygame for main gameplay
pygame.init()

#this file contains all the formats, font, and colors for 
#the game in a dictionary in a json file
file = open("formats.json", mode = "r")
formats = json.load(file)

#setting up the screen and font for the game, creating the main board
screen = pygame.display.set_mode((formats["size"], formats["size"]))
my_font = pygame.font.SysFont(formats["font"], formats["font_size"], bold=True)

'''whenever the code is run and this function is called
there will be a new game'''
def newGame():
    #creating a global variable for the board that we can call anywhere in the code
    #this variable is an object in the App2048 class that can be modified
    global game1
    game1 = App2048()
    game1.preGameSetUp()
    display(game1)

'''creating a function that updates the display after every move. There will be some animations using sprite module in python'''
def display(boardnum):

    board_copy = boardnum.copy()
    #creates background for game, box size per cube, and gets the padding from that json file
    screen.fill(tuple(formats["colors"]["background"]))
    box = formats["size"] // 4
    padding = formats["padding"]

    #creating the box for each cube, filling it with the color based on the rgb values from json file
    for y in range(4):
        for x in range(4):
            color = tuple(formats["colors"][str(boardnum.board[y][x])])
            pygame.draw.rect(screen, color, (x * box + padding,
                                             y * box + padding,
                                             box - 2 * padding,
                                             box - 2 * padding), 0)
            
            if boardnum.board[y][x] == 0:
                text_color = color
            elif boardnum.board[y][x] in (2,4):
                text_color = tuple((160,160,160))
            else:
                text_color = tuple((255,255,255))
            
            screen.blit(my_font.render('{:>4}'.format(boardnum.board[y][x]), 1, text_color), (x * box + 5 * padding, y * box + 14 * padding))
    pygame.display.update()

def playGame():
     while True:
         for event in pygame.event.get():
            if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == K_q):
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if str(event.key) not in formats['buttons']:
                    return "please type a valid key"
                else:
                    key = formats['buttons'][str(event.key)]
                    if key == 'w':
                        game1.fullUp()
                        display(game1)
                    elif key == 'a':
                        game1.fullLeft()
                        display(game1)
                    elif key == 's':
                        game1.fullDown()
                        display(game1)
                    elif key == 'd':
                        game1.fullRight()
                        display(game1)
                
                #checking status of the game
                if game1.check():
                    game1.pickTwoOrFour()
                else:
                    pygame.draw.rect(screen, (255, 204, 153),  )


if __name__ == '__main__':
    json.load(open('formats.json', mode = 'r'))
    file.close()
    pygame.init()
    newGame()
    playGame()


            
