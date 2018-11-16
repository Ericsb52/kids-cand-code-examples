# platformer game
# Ericsb52
# 9/18
#imports
from settings import *
from sprites import *
import pygame as pg
import random
from os import path


class Game:
    
    def __init__(self):
        #initialive game window ect
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("TITLE")
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        # load high score
        self.dir = path.dirname(__file__)

        with open(path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

        img_dir = path.join(self.dir, 'img')
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))
        #loud sound
        self.snd_dir = path.join(self.dir, 'snd')
        self.jump_sound = pg.mixer.Sound(path.join(self.snd_dir,"Jump36.wav"))
        self.boost_sound = pg.mixer.Sound(path.join(self.snd_dir, "Powerup36.wav"))





        
    
    def new(self):
        #start a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.player = Player(self)

        for plat in PLATFORM_LIST:
            Platform(self,*plat)

        pg.mixer.music.load(path.join(self.snd_dir,'happytune.ogg'))

        self.run()
       
    
    def run(self):
        #game loop
        pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            #keep loop running at the right speed
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(1000)
            
        
    
    def update(self):
        #game loop update

        self.all_sprites.update()
        #check if player hits platform
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms,False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.x < lowest.rect.right +8 and self.player.pos.x > lowest.rect.left -8:
                    if self.player.pos.y < lowest.rect.centery:
                        self.player.pos.y = lowest.rect.top
                        self.player.vel.y = 0
                        self.player.jumping = False

        #scroll screen at top 1/4
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += max(abs(self.player.vel.y), 2)
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.vel.y), 2)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10

        pow_hits = pg.sprite.spritecollide(self.player,self.powerups, True)
        for pow in pow_hits:
            if pow.type == "boost":
                self.boost_sound.play()
                self.player.vel.y = -BOOST_POWER
                self.player.jumping = False

        # if we die
        if self.player.rect.top > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms ) == 0:
            self.playing= False
        #spawn new platform
        while len(self.platforms)< 6:
            width = random.randrange(50,100)
            Platform(self,random.randrange(0,WIDTH-width),random.randrange(-75,-30))

    
    def events(self):
        #game loop events
        for event in pg.event.get():
        #closing the window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()
    def draw(self):
        #game loop draw
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.player.image,self.player.rect)
        self.draw_text(str(self.score), 22, WHITE, WIDTH /2,15)
        #after drawing every thing
        pg.display.flip()
    
    def show_start_screen(self):
        #start screen
        # game splash/start screen
        pg.mixer.music.load(path.join(self.snd_dir,"Yippee.ogg"))
        pg.mixer.music.play(loops=-1)
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Arrows to move, Space to jump", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def show_go_screen(self):
        # game over/continue
        pg.mixer.music.load(path.join(self.snd_dir, "Yippee.ogg"))
        pg.mixer.music.play(loops=-1)
        if not self.running:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!", 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self,text,size,color,x,y):
        font = pg.font.Font(self.font_name,size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)

    
g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
    
pg.quit()
