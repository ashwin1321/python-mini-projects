import pygame
import sys
import os
import random
import math


pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.speed()


#global variables

speed = 0.30
SNAKE_SIZE =0
APPLE_SIZE = SNAKE_SIZE    # food and snake size same
SEPERATION = 10 # pixels seperations

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 30
KEY = {"UP":1, "DOWN":2, "LEFT":3, "RIGHT":4}


#initialize screen

screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH),pygame.HWSURFACE)
# HWSURFACE stands for hardware surface referes to using memory on the video card for storing draws as opposed ti maun memory

#resourses

score_font = pygame.font.Font(None,38)
score_numb_font = pygame.font.Font(None,28)
game_over_font = pygame.font.Font(None,48)
play_again_font = score_numb_font
score_msg = score_font.render("Score: ",1,pygame.Color("green"))
score_msg_size = score_font.size("Score")
background_color = pygame.Color(0,0,0)       # background color black xa la
black = pygame.Color(0,0,0)

# for clock at the left corner
gameClock = pygame.time.Clock()

# we will define keys

def getKey():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return KEY["UP"]
            
            elif event.key == pygame.K_DOWN:
                return KEY["DOWN"]
            
            elif event.key == pygame.K_LEFT:
                return KEY["LEFT"]
            
            elif event.key == pygame.K_RIGHT:
                return KEY["RIGHT"]

            # for exit
            elif event.key == pygame.K_ESCAPE:
                return "exit"

            # If we want to continue playing again
            elif event.key == pygame.K_y:
                return "yes"
            
            # If we dont want to play again
            elif event.key == pygame.K_n:
                return "no"

        if event.type == pygame.QUIT:
            sys.exit(0)   

def endgame():
    message = game_over_font.render("Game Over", 1, pygame.Color("white"))
    message_play_again = play_again_font.render("Play again ? (Y/N)",1, pygame.Color("green"))
    screen.blit(message,(320,240))
    screen.blit(message_play_again,(320+12,240+40))

    pygame.display.flip()
    pygame.display.update()

    mKey = getKey()
    while(mKey != "exit"):
        if (mKey == "yes"):
            main()
        elif(mKey == "no"):
            break
        mKey = getKey()
        gameClock.tick(FPS)
    sys.exit(0)

def drar
def main():



