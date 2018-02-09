
import pygame, sys
from pygame.locals import *

pygame.init()
clock = 30
mainClock = pygame.time.Clock()

screen_x = 1000
screen_y = 600
screen = pygame.display.set_mode((screen_x,screen_y))

pygame.display.set_caption('My first Game')

background = pygame.image.load('background-1.png')
background = pygame.transform.scale(background, (screen_x,screen_y))
user_car = pygame.image.load('Audi.png') #import image
user_car = pygame.transform.scale(user_car, (160, 170)) #resizing image 
user_carx = 150
user_cary = 380


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN: 
            if event.key == K_RIGHT:
                if user_carx <= 680:
                    user_carx += 110
                else:
                    user_carx += 0
            elif event.key == K_LEFT:
                if user_carx >= 215:
                    user_carx -= 110
                else:
                    user_carx += 0
            elif event.key == K_UP:
                if user_cary >= 0:
                    user_cary -= 50
                else:
                    user_cary += 0
            elif event.key == K_DOWN:
                if user_cary <= 450:
                    user_cary += 50
                else:
                    user_cary += 0
       
    screen.blit(background,(0,0))
    screen.blit(user_car, (user_carx, user_cary))
    pygame.display.update()
    mainClock.tick(clock)