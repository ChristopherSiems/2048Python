from game_logic import App2048
import sys
import json
import pygame
from pygame.locals import *

# set up pygame for main gameplay
pygame.init()
file = open("formats.json", mode = "r")
formats = json.load(file)
screen = pygame.display.set_mode((formats["size"], formats["size"]))
my_font = pygame.font.SysFont(formats["font"], formats["font_size"], bold=True)


def newGame():
    global game1
    game1 = App2048()
    game1.preGameSetUp()
    display(game1)

def display(board):
    screen.fill(tuple(formats["colors"]["background"]))
    box = formats["size"] // 4
    padding = formats["padding"]
    for i in range(4):
        for j in range(4):
            color = tuple(formats["colors"][str(game1.board[i][j])])
            pygame.draw.rect(screen, color, (j * box + padding,
                                             i * box + padding,
                                             box - 2 * padding,
                                             box * 2 - padding), 0)
            if game1.board[i][j] == 0:
                text_color = tuple(formats["colors"]["0"])
            
            screen.blit(my_font.render('{:>4}'.format(game1.board[i][j]), 1, text_color), (j * box + 5 * padding, i * box + 14 * padding))
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


if __name__ == '__main__':
    json.load(open('formats.json', mode = 'r'))
    file.close()
    pygame.init()
    newGame()
    playGame()


            
