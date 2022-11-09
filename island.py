import pygame

class Island:
    def __init__(self):
        self.image = pygame.image.load('Assets/tile_01.png')
        self.rect = self.image.get_rect()

    def move(self, x, y):
        self.rect.center = (x,y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)