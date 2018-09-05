# platformer game
# Ericsb52
# 9/18
#imports
from settings import *
import pygame as pg
import random

class Game:
    def __init__(self):
        #initialive game window ect
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("TITLE")
        self.clock = pg.time.Clock()
        self.running = True
        
    
    def new(self):
        #start a new game
        self.all_sprites = pg.sprite.Group()
        g.run()
       
    
    def run(self):
        #game loop
        self.playing = True
        while self.playing:
            #keep loop running at the right speed
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            
        
    
    def update(self):
        #game loop update
        self.all_sprites.update()
    
    def events(self):
        #game loop events
        for event in pg.event.get():
        #closing the window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    
    def draw(self):
        #game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
    #after drawing every thing
        pg.display.flip()
    
    def show_start_screen(self):
        #start screen
        pass

    def show_go_screen(self):
        pass
    
g = Game()
g.show_start_screen()
while g.running:
    g.new()

    g.show_go_screen()
    
pg.quit()
