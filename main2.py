import pygame as pg
from sprites import *
from pygame import mixer
 
WIDTH = 1200
HEIGHT = 900
FPS = 120
 
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
 
class Game():
    def __init__(self):
        pg.init()
 
        self.bg_image = pg.image.load("background.jpg")
        self.bg_image = pg.transform.scale(self.bg_image, (WIDTH, HEIGHT))
        # lager font/teksttype med størrelse 30
        self.comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
 
        # Loading the song
        pg.mixer.music.load("song.mp3")
        
        # Setting the volume
        self.jumpsmash_sound = pg.mixer.Sound("jumpsmash.wav")
        self.blocksmash_sound = pg.mixer.Sound("blocksmash.wav")

        self.new()

    
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.balls = pg.sprite.Group()
        self.projectiles = pg.sprite.Group()
        self.blocks = pg.sprite.Group()

 
        self.my_player = Player()
        self.all_sprites.add(self.my_player)
 
        self.ball = Ball(self)
        self.all_sprites.add(self.ball)
        self.balls.add(self.ball)


        self.spawn_blocks()
        
        mixer.music.set_volume(0.7)
  
        # Start playing the song
        mixer.music.play(-1)
    
 
        self.run()
 
    def run(self):
        self.playing = True
        while self.playing: # game loop
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
 
        self.new() 
 
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                pg.quit()
 
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    self.playing = False

    def spawn_blocks(self):        
        x = 150
        y = -100
        for block in range(0,5):
            self.block = Block(x, y)
            self.all_sprites.add(self.block)
            self.blocks.add(self.block)
            x += 150
            block += 1
  
        x = 150
        y = -200
        for block in range(0,5):
            self.block = Block(x, y)
            self.all_sprites.add(self.block)
            self.blocks.add(self.block)
            x += 150
            block += 1
       
        x = 400
        y = -300
        for block in range(0,5):
            self.block = Block(x, y)
            self.all_sprites.add(self.block)
            self.blocks.add(self.block)
            x += 150
            block += 1

        x = 500
        y = -400
        for block in range(0,8):
            self.block = Block(x, y)
            self.all_sprites.add(self.block)
            self.blocks.add(self.block)
            x += 150
            block += 1

        x = 400
        y = -350
        for block in range(0,8):
            self.block = Block(x, y)
            self.all_sprites.add(self.block)
            self.blocks.add(self.block)
            x += 150
            block += 1

        x = 400
        y = -450
        for block in range(0,8):
            self.block = Block(x, y)
            self.all_sprites.add(self.block)
            self.blocks.add(self.block)
            x += 150
            block += 1

        x = 400
        y = -250
        for block in range(0,8):
            self.block = Block(x, y)
            self.all_sprites.add(self.block)
            self.blocks.add(self.block)
            x += 150
            block += 1

        x = 400
        y = -150
        for block in range(0,3):
            self.block = Block(x, y)
            self.all_sprites.add(self.block)
            self.blocks.add(self.block)
            x += 150
            block += 1

        x = 400
        y = -325
        for block in range(0,8):
            self.block = Block(x, y)
            self.all_sprites.add(self.block)
            self.blocks.add(self.block)
            x += 150
            block += 1

        x = 400
        y = -425
        for block in range(0,8):
            self.block = Block(x, y)
            self.all_sprites.add(self.block)
            self.blocks.add(self.block)
            x += 150
            block += 1

    def update(self):
        self.all_sprites.update()
 
        self.hits = pg.sprite.spritecollide(self.my_player, self.balls, False)
        if self.hits:
            if self.my_player.pos.x > self.ball.pos.x:
                self.ball.speed_x = -3

            else:
                self.ball.speed_x = 3

            self.ball.speed_y = -3


            pg.mixer.Sound.play(self.jumpsmash_sound)

        self.hits = pg.sprite.groupcollide(self.balls, self.blocks, False, True)
        if self.hits:
            self.ball.speed_y *= -1
            pg.mixer.Sound.play(self.blocksmash_sound)
 
        # spawn enemies
        while len(self.balls) < 1:
            self.ball = Ball()
            self.all_sprites.add(self.ball)
            self.balls.add(self.ball)
        
        if len(self.blocks) <= 0:
            self.spawn_blocks()
 
    def draw(self):
        # tegner ting til skjerm på valgt posisjon, og størrelse
        #self.screen.fill(WHITE)
        self.screen.blit(self.bg_image, (0, 0))
 
        self.all_sprites.draw(self.screen)
 
        # rendrer/generer teksten som vi kan tegne til game screen
        # dette viser ikke teksten enda, men har bare laget den klar
        self.text_player_hp = self.comic_sans30.render(str(self.my_player.hp), False, (RED))
        
        # tegn teksten til skjermen på en satt posisjon
        self.screen.blit(self.text_player_hp, (10, 10))
 
        # oppdaterer alle endringer på spill vinduet
        pg.display.update()


            

           

 
g = Game()



       