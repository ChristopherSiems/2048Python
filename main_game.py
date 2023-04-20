import game_logic
from game_logic import App2048
import pygame
from pygame.locals import *

'''currently using this for logic testing but later this will be 
where we initialize the game and actually play the game'''

def startGame():
    global game1
    game1 = App2048()
    game1.preGameSetUp()

def movingUp():
    game1.upMove()
    game1.pickTwoOrFour()

def movingDown():
    game1.downMove()
    game1.pickTwoOrFour()
