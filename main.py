import pygame as pg
from sprites import *
 
pg.init()
#pg.font.init()
 
WIDTH = 1000
HEIGHT = 1000


 
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED= (255,0,0)


# lager font/teksstype med størrelse 30 
comic_sans30 = pg.font.SysFont('Comic Sans MS', 30)
screen = pg.display.set_mode((WIDTH,HEIGHT))
 
clock = pg.time.Clock()
FPS = 120

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
block_group = pg.sprite.Group()


block = Block()
all_sprites.add(block)
block_group.add(block)





player1 = Player()
all_sprites.add(player1)