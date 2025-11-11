import pygame 
from config import *
from assets import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.direction = 'f'

        self.image = assets[PLAYER_F]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT
        self.groups = groups
        self.assets = assets

    def update(self, assets):
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < HEIGHT * 2 / 5:
            self.rect.top = HEIGHT * 2 / 5

        self.image = assets['player'+self.direction]
        self.mask = pygame.mask.from_surface(self.image)
