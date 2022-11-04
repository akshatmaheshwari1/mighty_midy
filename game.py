import pygame
import sys

TILE_SIZE = 64
pygame.init()
screen = pygame.display.set_mode((10*TILE_SIZE,10*TILE_SIZE))
watertile = pygame.image.load('Assets/water_tile.png')

water_rect = watertile.get_rect()
screen_rect = screen.get_rect()
for x in range(screen_rect.height//water_rect.width):
    for y in range(screen_rect.width//water_rect.height):
        screen.blit(watertile, (x * water_rect.width, y * water_rect.height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("thanks for playing")
            sys.exit()
    pygame.display.flip()


