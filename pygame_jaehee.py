
import pygame, sys
from pygame.locals import *
from pygame.sprite import Sprite
import random

clock = 30
mainClock = pygame.time.Clock()

class User_car(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(User_car,self).__init__() #Don't know what it does yet.
        self.user_carx = 150
        self.user_cary = 380
        self.screen = screen 
        self.image = pygame.image.load("image/Audi.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (160, 170))
        self.rect = self.image.get_rect()

class Other_cars(pygame.sprite.Sprite):
    def __init__(self, speed):
        super(Other_cars,self).__init__()
        self.x = random.randrange(100, 700, 30)
        self.y = 100
        self.speed = speed

    def update (self, screen_x, screen_y):
        self.y += self.speed
        if self.x > screen_x:
            self.x = 0     
        if self.y > screen_y:
            self.y = 0
    
    def display_car(self, screen):
        police = pygame.image.load("image/police1.png").convert_alpha()
        police = pygame.transform.scale(police, (160,170))
        screen.blit(police, (self.x, self.y))
        
def main():
    # Declare the size of the canvas
    screen_x = 1000
    screen_y = 600

    # Game Initialization
    pygame.init()
    screen = pygame.display.set_mode((screen_x,screen_y))
    pygame.display.set_caption('On my way')

    # Background image
    background = pygame.image.load('image/background-1.png')
    background = pygame.transform.scale(background, (screen_x,screen_y))

    car = User_car(screen)
    other_car = Other_cars(screen)

    car_list = [Other_cars(10), Other_cars(12), Other_cars(9)]

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                stop_game = True

            # User_car Logic
            if event.type == KEYDOWN: 
                if event.key == K_RIGHT:
                    if car.user_carx <= 680:
                        car.user_carx += 110
                    else:
                        car.user_carx += 0
                elif event.key == K_LEFT:
                    if car.user_carx >= 215:
                        car.user_carx -= 110
                    else:
                        car.user_carx += 0
                elif event.key == K_UP:
                    if car.user_cary >= 0:
                        car.user_cary -= 50
                    else:
                        car.user_cary += 0
                elif event.key == K_DOWN:
                    if car.user_cary <= 450:
                        car.user_cary += 50
                    else:
                        car.user_cary += 0

        # Other_cars Logic
        for a in car_list:
            a.update(screen_x, screen_y)
        
        for a in car_list:
            a.display_car(screen)

        pygame.display.update()
        
        screen.blit(background,(0,0))
        screen.blit(car.image, (car.user_carx, car.user_cary))
        mainClock.tick(clock)
    
    pygame.quit()

if __name__ == '__main__':
    main()