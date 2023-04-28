'''This is the code that will launch and play the game 2048'''

#These imported modules allow us to run the game and load all the necessary functions
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
format_file = open("formats.json", mode = "r")
formats = json.load(format_file)

'''This section creates the screen and grabs all the fonts from the imported json file'''
screen = pygame.display.set_mode((formats["size_y"], formats["size_x"]))
my_font = pygame.font.SysFont(formats["font"], formats["game_font_size"], bold=True)
sidebar_font = pygame.font.SysFont(formats["font"], formats["sidebar_font_size"], bold=True)
title_controls_font = pygame.font.SysFont(formats["font"], int(formats["sidebar_font_size"]/1.15), bold=True)
controls_font = pygame.font.SysFont(formats["font"], int(formats["sidebar_font_size"]/1.25), bold=False)
gameover_font = pygame.font.SysFont(formats["font"], formats["gameover_font_size"])

'''This function is called before the game starts to intialize the board and display the start of the game'''
def newGame():
        
    #created variable running to make sure the game is playable and still turned on
    global running 
    running = True

    #creating a global variable for the board that we can call anywhere in the code
    #this variable is an object in the App2048 class that can be modified
    global game1
    game1 = App2048()
    game1.preGameSetUp()
    display(game1, running)

'''creating a function that updates the display after every move or if the game is over'''
def display(boardnum, over_check):
    #creating the title of the window
    pygame.display.set_caption('2048 Game by Sai Chanda, Chris Siems, and Sam Szymanski')
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
            #takes the created box + color and adds it to the screen with its value. 
            #The adjustments in the last argument give the necessary formating for the number
            screen.blit(my_font.render('{:>3}'.format(boardnum.board[y][x]), True, text_color), (x * box + 4 * padding, y * box + 7 * padding))

    #Creating the Sidebar Menue for the Game
    pygame.draw.rect(screen, formats['colors']['sidebar'],  (905, 10, formats['size_x'] - 620 , formats['size_y'] - 320), 0)


    '''All sidebar text is created here, giving the text, font, and if bold or not'''
    #Text includes:
    #     Score and Score Count
    #     Letting user know their move
    #     All the controls in the game

    score_text = sidebar_font.render('Score:', True, formats["colors"]["text"])
    score_count = sidebar_font.render(str(boardnum.score), True, formats["colors"]["text"])
    move_text = sidebar_font.render('Your Move: ' + boardnum.move_name, True, formats["colors"]["text"])
    game_controls_text = title_controls_font.render('Game Controls:', True, formats["colors"]["text"])
    w_control = controls_font.render('W or ^:         Up', True, formats["colors"]['text'])
    a_control = controls_font.render('A or <:        Left', True, formats["colors"]['text'])
    s_control = controls_font.render('S or v:      Down', True, formats["colors"]['text'])
    d_control = controls_font.render('D or >:       Right', True, formats["colors"]['text'])
    q_control = controls_font.render('Q:              Quit', True, formats["colors"]['text'])
    

    #creating a rectangle for all of the specific texts variables
    score_textRect = score_text.get_rect()
    score_countRect = score_count.get_rect()
    move_textRect = move_text.get_rect()
    game_controls_textRect = game_controls_text.get_rect()
    w_controlRect = w_control.get_rect()
    a_controlRect = s_control.get_rect()
    s_controlRect = s_control.get_rect()
    d_controlRect = d_control.get_rect()
    q_controlRect = q_control.get_rect()

    #identifying the space where the text will be printed, by giving the top left corner as the starting value
    score_textRect.topleft = (920, 100)
    score_countRect.topleft = (920, 150)
    move_textRect.topleft = (920, 250)
    game_controls_textRect.topleft = (940, 400)
    w_controlRect.topleft = (950, 450)
    a_controlRect.topleft = (950, 475)
    s_controlRect.topleft = (950, 500)
    d_controlRect.topleft = (950, 525)
    q_controlRect.topleft = (950, 550)

    #Adds all of the text to the display
    screen.blit(game_controls_text,game_controls_textRect)
    screen.blit(score_text, score_textRect)
    screen.blit(score_count, score_countRect)
    screen.blit(move_text, move_textRect)
    screen.blit(w_control, w_controlRect)
    screen.blit(a_control, a_controlRect)
    screen.blit(s_control, s_controlRect)
    screen.blit(d_control, d_controlRect)
    screen.blit(q_control, q_controlRect)
    
    #if the game is over, then it will add the "Game Over" screen on top of the game.
    #Adds a opaque cover on the game
    if over_check == False:
        size_x = formats['size_x']
        size_y = formats['size_y']
        s = pygame.Surface((size_x, size_y), pygame.SRCALPHA)
        s.fill(formats["colors"]["game_over"])
        screen.blit(s, (0, 0))
        gameOverText = gameover_font.render('Game Over', True, formats["colors"]["text"])
        gameOverTextRect = gameOverText.get_rect()
        gameOverTextRect.center = ((900-90)/2 + 50,400)
        screen.blit(gameOverText,gameOverTextRect)

    #Updating the display to include all changes made in the move
    pygame.display.update()


'''main game loop that will keep running as long as the tab is open and the game is playable'''
def playGame(boardnum):


    #this while loop will keep playing unless:
    #     User Presses 'q' or the red 'x' at top right corner
    #     User Presses 'n' after game is over and wishes not to play again
    moves = ['''w''', '''a''', '''s''', '''d''']
    running = True
    while True:
        for event in pygame.event.get():
            #running = True
            
            #If statement to see if user has pressed 'q' or the red 'x' in top right corner 
            #to know if they want to exit game
            if event.type == QUIT or event.type == pygame.KEYDOWN and event.key == K_q:
                    running = False
                    pygame.quit()
                    sys.exit()

            #to stop overflow of data in game, when users press a non playable key, the game passes the data and continues the game
            elif event.type == pygame.KEYDOWN and str(event.key) not in formats['''buttons''']:
                continue

            #these 'if' statements determine what move the user wants to do and processes that move
            #Possible moves include
            #     'w' = Up
            #     'a' = Left
            #     's' = Down
            #     'd' = Right
            #Once the move is processed, the game creates a copy of the board, modifes the board, and checks to see if the copy is different from the modified board
            #If the modified board and copy are not the same, it runs the pickTwoOrFour() to place a random '2' or '4' on the board
            #Else, just goes to the display() function and updates the display
            #      The reason for this 'if' statement is to stop the user from not changing the board and getting new values
            #      That would break the intent of the game to add values properly and makes the game too easy
            elif event.type == pygame.KEYDOWN and running:
                key = formats['buttons'][str(event.key)]
                if key == 'w':
                    c = boardnum.copy()
                    boardnum.fullUp()
                    if not boardnum.compare(c):
                        boardnum.pickTwoOrFour()
                    display(boardnum, running)
                elif key == 'a':
                    c = boardnum.copy()
                    boardnum.fullLeft()
                    if not boardnum.compare(c):
                        boardnum.pickTwoOrFour()
                    display(boardnum, running)
                elif key == 's':
                    c = boardnum.copy()
                    boardnum.fullDown()
                    if not boardnum.compare(c):
                        boardnum.pickTwoOrFour()
                    display(boardnum, running)
                elif key == 'd':
                    c = boardnum.copy()
                    boardnum.fullRight()
                    if not boardnum.compare(c):
                        boardnum.pickTwoOrFour()
                    display(boardnum, running)

                #This 'if' statement checks to see if the game is over or not
                #      If playable, then continues the game
                #      Else, runs the end game sequence where the display shows the game over and allows the user to choose if they want to play again or not
                if not boardnum.check():
                    running = False
                    display(boardnum, running)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.type == pygame.KEYDOWN:
                                key == formats['buttons'][str(event.key)]
                                if key == 'n':
                                    pygame.quit()
                                    sys.exit()
                                elif key == 'y':
                                    boardnum.define([[0] * 4, [0] * 4, [0] * 4,  [0] * 4])
                                    display(game1)
                                    playGame(game1)
                                
#Running the actual game
if __name__ == '__main__':
    json.load(open('formats.json', mode = 'r'))
    format_file.close()
    pygame.init()
    newGame()
    playGame(game1)