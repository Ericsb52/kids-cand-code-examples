# flapy bird game
# Ericsb52
# 11/18


#imports
from settings import *
from sprites import*
import pygame as pg
import random

class Game:
    def __init__(self):
        #initialize game window ect
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("TITLE")
        self.clock = pg.time.Clock()
        self.running = True
        
    
    def new(self):
        #start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.pipes = pg.sprite.Group()
        
        
        self.player = Player()
        self.all_sprites.add(self.player)

        ground = Platform(0,HEIGHT-40,WIDTH,40)
        self.all_sprites.add(ground)
        self.platforms.add(ground)

        bottompipe = Pipe(WIDTH+60,HEIGHT, 40, 200)
        self.all_sprites.add(bottompipe)
        self.pipes.add(bottompipe)
        
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
        #game loop  -- update
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player,self.platforms,False)
        if hits:
            self.player.pos.y = hits[0].rect.top
            self.player.vel.y = 0
    
    def events(self):
        #game loop -- events
        for event in pg.event.get():
        #closing the window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    
    def draw(self):
        #game loop  -- draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        #after drawing every thing
        pg.display.flip()
    
    def show_start_screen(self):
        #start screen
        pass

    def show_gameOver_screen(self):
        # game over screen
        pass
    
g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_gameOver_screen()
    
pg.quit()
