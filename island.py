import pygame
from pygame.sprite import Sprite
class Island(Sprite):
    def __init__(self):
        self.image = pygame.surface.Surface((128,128))
        self.image.blit(pygame.image.load('Assets/water_tile.png'), (0, 0))
        self.image.blit(pygame.image.load('Assets/water_tile.png'), (64, 0))
        self.image.blit(pygame.image.load('Assets/water_tile.png'), (0, 64))
        self.image.blit(pygame.image.load('Assets/water_tile.png'), (64, 64))
        self.image.blit(pygame.image.load('Assets/tile_01.png'), (0,0))
        self.image.blit(pygame.image.load('Assets/tile_03.png'), (64, 0))
        self.image.blit(pygame.image.load('Assets/tile_33.png'), (0, 64))
        self.image.blit(pygame.image.load('Assets/tile_35.png'), (64, 64))
        self.rect = self.image.get_rect()

    def move(self, x, y):
        self.rect.center = (x,y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)