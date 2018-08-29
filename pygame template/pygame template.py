# pygame template --skeleton for a new py game project--

#imports
import pygame
import random

#constants
WIDTH = 380
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE =(0, 0, 255)
GREEN = (0, 255, 0)

#initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my game title")
clock = pygame.time.clock()

all_sprites = pygame.sprite.Group()

#game loop
running = True
while running:
    #keep loop running at the right speed
    clock.tick(FPS)
    #process input (events)
    for event in pygame.event.get():
        #closing the window
        if event.type == pygame.QUIT:
            running = False


            
    #update
    all_sprites.update()


            
    #draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #after drawing every thing
    pygame.display.flip()


    
pygame.quit()
