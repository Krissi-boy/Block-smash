import pygame as pg
vec = pg.math.Vector2
from random import randint


enemy_image = pg.image.load("enemy.png")
player_image = pg.image.load("player.png")
block_image = pg.image.load("block.png")

WIDTH = 1200
HEIGHT = 900

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.image = pg.transform.scale(self.image, (300,30))
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, 850)
        self.rect.center = self.pos
        self.speed = 6
        self.hp = 100
    # linjen over setter en ny verdi på self.image,tallene til slutt er størrelsen på bilde i x og y



    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.pos.x -= self.speed
        if keys[pg.K_d]:
            self.pos.x += self.speed  

        self.rect.center = self.pos




class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.image = pg.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, randint(90, 100)) # start posisjon
        self.rect.center = self.pos
        self.speed_x = 3
        self.speed_y = 3
       


    def update(self):
        self.pos.x += self.speed_x
        self.pos.y += self.speed_y
        if self.pos.x > WIDTH: # hvis til høyre for skjerm
            self.speed_x = -1
        if self.pos.x < 0: # hvis til venstre for skjerm
            self.speed_x = 1
    
        if self.pos.y <= 0:
            self.speed_y = 3
            

        self.rect.center = self.pos

        


class Block(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = block_image
        self.image = pg.transform.scale(self.image, (150,100))
        self.rect = self.image.get_rect()
        self.pos = vec(800, 100)
        self.rect.center = self.pos
        self.speed = 0.1
        self.pos.x = randint(0, WIDTH)
    


        self.rect.center = self.pos
    def update(self):
        self.pos.y += self.speed
        if self.pos.x > 800: # hvis til høyre for skjerm
            self.speed_x = -1
        if self.pos.x < 0: # hvis til venstre for skjerm
            self.speed_x = 1
        self.rect.center = self.pos
    













      


        

        