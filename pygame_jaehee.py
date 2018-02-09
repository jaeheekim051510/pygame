
import pygame, sys
from pygame.locals import *

clock = 30
mainClock = pygame.time.Clock()

class User_car(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(User_car,self).__init__()
        self.user_carx = 150
        self.user_cary = 380
        self.image = pygame.image.load("Audi.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.screen = screen #resizing image 
        self.resizedcar = pygame.transform.scale(self.image, (160, 170))

# class Police_car(pyagme.sprite.Sprite):
#     def __init__(self, x, y, speed):
#         super(Police_car,self).__init__()
#         self.police_carx = x
#         self.police_cary = y
#         self.speed = speed
#     def update (self, )

def main():
    screen_x = 1000
    screen_y = 600

    pygame.init()
    screen = pygame.display.set_mode((screen_x,screen_y))
    pygame.display.set_caption('My first Game')

    background = pygame.image.load('background-1.png')
    background = pygame.transform.scale(background, (screen_x,screen_y))

    car = User_car(screen)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

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
        
        screen.blit(background,(0,0))
        screen.blit(car.resizedcar, (car.user_carx, car.user_cary))
        pygame.display.update()
        mainClock.tick(clock)
    
    pygmae.quit()
if __name__ == '__main__':
    main()