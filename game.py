import pygame
import sys
from ship import Ship

TILE_SIZE = 64
pygame.init()
screen = pygame.display.set_mode((10*TILE_SIZE,10*TILE_SIZE))
watertile = pygame.image.load('Assets/water_tile.png')
water_rect = watertile.get_rect()
screen_rect = screen.get_rect()
topleft = pygame.image.load('Assets/tile_01.png')
topright = pygame.image.load('Assets/tile_03.png')
bottomleft = pygame.image.load('Assets/tile_33.png')
bottomright = pygame.image.load('Assets/tile_35.png')
ship = Ship()
#water
def draw_background():
    for x in range(screen_rect.height//water_rect.width):
        for y in range(screen_rect.width//water_rect.height):
            screen.blit(watertile, (x * water_rect.width, y * water_rect.height))
    screen.blit(topleft, (250, 250))
    screen.blit(topright, (250 + topleft.get_width(), 250))
    screen.blit(bottomleft, (250, 250 + topleft.get_height()))
    screen.blit(bottomright, (250 + topleft.get_width(), 250 + topleft.get_height()))

(x,y) = (0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("thanks for playing")
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            (x,y) = pygame.mouse.get_pos()

    draw_background()
    ship.move(x,y)
    ship.draw(screen)
    pygame.display.flip()




