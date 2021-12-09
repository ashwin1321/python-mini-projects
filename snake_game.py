import pygame
import sys
import os
import random
import math

from pygame.constants import K_KP_ENTER, TIMER_RESOLUTION


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

def checkCollision(posA, As, posB, Bs):    # As is the size of a and Bs is the size of b
    if (posA.x < posB.x+Bs and posA.x+As > posB.x and posA.y < posB.y+Bs and posA.y+As > posB.y):
        return True
    return False

# to check boundaries, here we are not limiting boundaries like it can pass through screen and come from other side

def checkLimits(snake):
    if (snake.x > SCREEN_WIDTH):
        snake.x = SNAKE_SIZE
    if (snake.x <0):            # Opposite side ma snake bhayo bhane check garxa
        snake.x = SCREEN_WIDTH - SNAKE_SIZE
    if (snake.y > SCREEN_HEIGHT):
        snake.y = SNAKE_SIZE
    if (snake.y < 0):      # same tara y-axix ma laa
        snake.y = SCREEN_HEIGHT - SNAKE_SIZE


# we make a class for food for the snake lets name it apple

class Apple:
    def __init__(self,x,y,state):
        self.x = x
        self.y = y
        self.state = state
        self.color = pygame.color.Color("orange")  # colour of food
        
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,APPLE_SIZE,APPLE_SIZE),0)
        
class segment:
    #initially snake will move in up direction
    def __init__(self,x,y):
        self.x = x
        self.y  =y
        self.direction = KEY["UP"]
        self.color = "white"

class snake:
    def __init__(self,x,y):
        self.x =x 
        self.y =y 
        self.direction = KEY["UP"]
        self.stack = [] #initially empty
        self.stack.append(self)
        blackBox = segment(self.x,self.y + SEPERATION)
        blackBox.direction = KEY['UP']
        blackBox.color = "NULL"
        self.stack.append(blackBox)

# we will define moves of the snake
    def move(self):
        last_element = len(self.stack) -1
        while(last_element !=0):
            self.stack[last_element].direction = self.stack[last_element].direction
            self.stack[last_element].x = self.stack[last_element-1].x
            self.stack[last_element].y = self.stack[last_element-1].y
            last_element -= 1
        if (len(self,stack)<2):
            last_segment = self
        else:
            last_segment = self.stack,pop(last_element) 
            16:09


# we will define keys

def getKey():xy
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

def drawScore(score):
    score_numb = score_numb_font.render(str(score),pygame.Color("red"))
    screen.blit(score_msg,(SCREEN_WIDTH - score_msg_size[0]-60,10))
    screen.blit(score_numb,(SCREEN_WIDTH -45, 14))

def drawGameTime(gameTime):
    game_time = score_font.render("Time:", 1, pygame.Color("white"))
    game_time_numb = score_numb_font.render(str(gameTime/1000),1,pygame.Color("white"))

def main():



