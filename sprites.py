import pygame as pg
vec = pg.math.Vector2
from random import randint

enemy_image = pg.image.load("enemy.png")
player_image = pg.image.load("player.png")
block_image = pg.image.load("block.png")



class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.image = pg.transform.scale(self.image, (150,100))
        self.rect = self.image.get_rect()
        self.pos = vec(500, 500)
        self.rect.center = self.pos
        self.speed = 3
        self.hp = 100


    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.pos.y -= self.speed
            print("w")
        if keys[pg.K_s]:
            self.pos.y += self.speed
        if keys[pg.K_a]:
            self.pos.x -= self.speed
        if keys[pg.K_d]:
            self.pos.x += self.speed  

        self.rect.center = self.pos




class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.image = pg.transform.scale(self.image, (80,80))
        self.rect = self.image.get_rect()
        self.pos = vec(1000, randint(0, 600)) # start posisjon
        self.rect.center = self.pos
        self.speed = 1
        self.pos


    def update(self):
        self.pos.x += self.speed
        self.pos.y += self.speed
        if self.pos.x > 800: # hvis til høyre for skjerm
            self.speed_x = -1
        if self.pos.x < 0: # hvis til venstre for skjerm
            self.speed_x = 1
    





class Block(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = block_image
        self.image = pg.transform.scale(self.image, (150,100))
        self.rect = self.image.get_rect()
        self.pos = vec(300, 300)
        self.rect.center = self.pos
        self.speed = 1


        self.rect.center = self.pos












      


        

        