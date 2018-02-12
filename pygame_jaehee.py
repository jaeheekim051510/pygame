
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
        self.x = random.randrange(215, 680, 100)
        self.y = 100
        self.speed = speed

    def update (self, screen_x, screen_y):
        self.x += self.speed
        self.y += self.speed
        if self.x > screen_x:
            self.x = 0
        if self.y > screen_y:
            self.y = 0
    
    def display(self, screen):
        # Police image
        police  = pygame.image.load("image/police1.png").convert_alpha()
        police = pygame.transform.scale(police, (160,170))
        # # Ambulance image
        # ambulance = pygame.image.load("image/ambulance1.png").convert_alpha()
        # ambulance = pygame.transform.scale(ambulance, (160,170))
        
        screen.blit(police, (self.x, self.y))
    
    #     self.rect = self.image.get_rect()

def main():
    # declare the size of the canvas
    screen_x = 1000
    screen_y = 600

    pygame.init()
    screen = pygame.display.set_mode((screen_x,screen_y))
    pygame.display.set_caption('My first Game')

    # Background image
    background = pygame.image.load('image/background-1.png')
    background = pygame.transform.scale(background, (screen_x,screen_y))

    # othercar_list = [
    #     police, 
    #     ambulance
    # ]

    car = User_car(screen)
    other_car = Other_cars(screen)

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                # pygame.quit()
                # sys.exit()
                stop_game = True

            #User_car Key Function 
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
            # Other cars logic
            # for othercar in othercar_list:
            #     othercar.display(screen)
        
        screen.blit(background,(0,0))
        screen.blit(car.image, (car.user_carx, car.user_cary))
        pygame.display.update()
        mainClock.tick(clock)
    
    pygame.quit()

if __name__ == '__main__':
    main()