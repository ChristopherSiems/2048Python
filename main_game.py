from game_logic import App2048
import sys
import json
import pygame
from pygame.locals import *

# set up pygame for main gameplay
pygame.init()
pygame.font.init()

#this file contains all the formats, font, and colors for 
#the game in a dictionary in a json file
file = open("formats.json", mode = "r")
formats = json.load(file)

#setting up the screen and font for the game, creating the main board
screen = pygame.display.set_mode((formats["size_y"], formats["size_x"]))
my_font = pygame.font.SysFont(formats["font"], formats["game_font_size"], bold=True)
sidebar_font = pygame.font.SysFont(formats["font"], formats["sidebar_font_size"], bold=True)
gameover_font = pygame.font.SysFont(formats["font"], formats["gameover_font_size"])

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
    pygame.display.set_caption('2048 Game by Sai Chanda, Chris Siems,and Sam Szymanski')
    board_copy = boardnum.copy()
    #creates background for game, box size per cube, and gets the padding from that json file
    screen.fill(tuple(formats["colors"]["background"]))
    box = formats["size_x"] // 4
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
                text_color = formats["colors"]["text"]
            else:
                text_color = tuple((255,255,255))
            screen.blit(my_font.render('{:>3}'.format(boardnum.board[y][x]), True, text_color), (x * box + 4 * padding, y * box + 7 * padding))
    score_text = sidebar_font.render('Score:', True, formats["colors"]["text"])
    score_count = sidebar_font.render(str(boardnum.score), True, formats["colors"]["text"])
    move_text = sidebar_font.render('Your Move:', True, formats["colors"]["text"])
    your_move = sidebar_font.render(boardnum.move_name, True, formats["colors"]["text"])
    # controls = 'Game Controls:\n\
    #                                W or ^:    Up\n\
    #                                A or <:    Left\n\
    #                                S or v:    Down\n\
    #                                D or >:    Right\n\
    #                                Q:         Quit'
    # sentences = [word for word in controls.splitlines()]
    
    # controlsRect = controls.get_rect()
    score_textRect = score_text.get_rect()
    score_countRect = score_count.get_rect()
    move_textRect = move_text.get_rect()
    your_moveRect = your_move.get_rect()

    # controlsRect.bottomleft = (1050, 500)
    score_textRect.center = (1050, 100)
    score_countRect.center = (1050, 150)
    move_textRect.center = (1050, 250)
    your_moveRect.center = (1050, 400) 

    # screen.blit(controls, controlsRect)
    screen.blit(score_text, score_textRect)
    screen.blit(score_count, score_countRect)
    screen.blit(your_move, your_moveRect) 
    screen.blit(move_text, move_textRect)
    pygame.display.update()

def playGame(boardnum):
    running  = True
    while running :
        for event in pygame.event.get():
            if event.type == QUIT or event.type == pygame.KEYDOWN and event.key == K_q:
                    running = False

            elif event.type == pygame.KEYDOWN:
                key = formats['buttons'][str(event.key)]
                if key == 'w':
                    boardnum.fullUp()
                    boardnum.pickTwoOrFour()
                    display(boardnum)
                elif key == 'a':
                    boardnum.fullLeft()
                    boardnum.pickTwoOrFour()
                    display(boardnum)
                elif key == 's':
                    boardnum.fullDown()
                    boardnum.pickTwoOrFour()
                    display(boardnum)
                elif key == 'd':
                    boardnum.fullRight()
                    boardnum.pickTwoOrFour()
                    display(boardnum)
                #checking status of the game
                if boardnum.check():
                    continue
                else:
                    size_x = formats['size_x']
                    size_y = formats['size_y']
                    s = pygame.Surface((size_x, size_y), pygame.SRCALPHA)
                    s.fill(formats["colors"]["game_over"])
                    screen.blit(s, (0, 0))
                    gameOverText = gameover_font.render('Game Over', True, formats["colors"]["text"])
                    gameOverTextRect = gameOverText.get_rect()
                    gameOverTextRect.center = ((900-90)/2 + 50,400)
                    screen.blit(gameOverText,gameOverTextRect)
                    # pygame.quit()
                    # sys.exit()
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if str(event.key) not in formats['buttons']:
                                key == formats['buttons'][str(event.key)]
                                if key == 'n':
                                    pygame.quit()
                                    sys.exit()
                                elif key == 'y':
                                    newGame()
                                    playGame()
                                

if __name__ == '__main__':
    json.load(open('formats.json', mode = 'r'))
    file.close()
    pygame.init()
    newGame()
    playGame(game1)