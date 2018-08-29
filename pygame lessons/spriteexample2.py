# pygame template --skeleton for a new py game project--

#imports
import pygame
import random
import os


#constants
WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE =(0, 0, 255)
GREEN = (0, 255, 0)

#set up assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
    #sprite for player
    def__init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.imag.load(os.path.join(img_folder, "file name")).convert()
        self.image.set_colorkey(BLACK)
                                    
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2 )
        self.y_speed = 5
        

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT -200:
            self.y_speed = -5
            
        if self.rect.top < 200:
            self.y_speed = 5
            
        if self.rect.left > WIDTH:
            self.rect.right = 0

#initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my game title")
clock = pygame.time.clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

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
