from game_logic import App2048
import sys
import json
import pygame
from pygame.locals import *

# set up pygame for main gameplay
pygame.init()
c = json.load(open("formats.json", "r"))
screen = pygame.display.set_mode((c["size"], c["size"]))
my_font = pygame.font.SysFont(c["font"], c["font_size"], bold=True)
WHITE = (255, 255, 255)

def newGame():
    global game1
    game1 = App2048()
    game1.preGameSetUp()
    display(game1)

def display(board):
    screen.fill(tuple(c["colors"]["background"]))
    box = c["size"] // 4
    padding = c["padding"]
    for i in range(4):
        for j in range(4):
            color = tuple(c["color"][str(board[i][j])])
            pygame.draw.rect(screen, color, (j * box + padding,
                                             i * box + padding,
                                             box - 2 * padding,
                                             box * 2 - padding), 0)
            if board[i][j] == 0:
                text_color = tuple(c["color"]["0"])
            
            screen.blit(my_font.render('{:>4}'.format(board[i][j]), 1, text_color), 
                        (j * box + 5 * padding, i * box + 14 * padding))
    pygame.display.update()

def playGame():
     while True:
         for event in pygame.event.get():
            if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == K_q):
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if str(event.key) not in c['buttons']:
                    return "please type a valid key"
                else:
                    key = c['buttons'][str(event.key)]
                    if key == 'w':
                        game1.fullUp()
                    elif key == 'a':
                        game1.fullLeft()
                    elif key == 's':
                        game1.fullDown()
                    elif key == 'd':
                        game1.fullRight()
                
                #checking status of the game
                if 


            
