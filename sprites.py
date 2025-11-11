import pygame 
from config import *
from assets import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, assets):

        self.image = assets[PLAYER_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
    
