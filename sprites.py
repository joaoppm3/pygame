import pygame 
import random
from config import *
from assets import *

class Player(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.direction = 'f'

        self.image = assets[PLAYER_F]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT
        self.assets = assets

    def update(self):
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < HEIGHT * 2 / 5:
            self.rect.top = HEIGHT * 2 / 5

        self.image = self.assets['player'+self.direction]
        self.mask = pygame.mask.from_surface(self.image)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, assets, i):
        pygame.sprite.Sprite.__init__(self)

        speed = random.randint(8, 15)

        if i % 2 == 0:
            direcao = 'e'
            posix = WIDTH
            posiy = -120 + 240 * (i / 2) - 5
            speed *= -1
        else:
            direcao = 'd'
            posix = 0 - CAR_WIDTH
            posiy = -120 + 240 * (i // 2) + 50
            speed = speed

        colour = random.randint(1, 3)
        if colour == 1:
            colour = 'r'
        elif colour == 2:
            colour = 'y'
        else:
            colour = 'b'

        self.assets = assets
        self.direcao = direcao
        self.image = assets[colour+direcao]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = posix
        self.rect.y = posiy
        self.speed = speed

    def update(self):
        self.rect.x += self.speed

        speed = random.randint(8, 15)

        colour = random.randint(1, 3)
        if colour == 1:
            colour = 'r'
        elif colour == 2:
            colour = 'y'
        else:
            colour = 'b'

        if self.direcao == 'e':
            if self.rect.right < 0:
                self.image = self.assets[colour+self.direcao]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect.x = WIDTH
                self.speed = - speed
            if self.rect.centery > HEIGHT:
                self.rect.y = -120 - 20
        else:
            if self.rect.left > WIDTH:
                self.image = self.assets[colour+self.direcao]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect.right = 0
                self.speed = speed
            if self.rect.top > HEIGHT:
                self.rect.y = -120 + 35

    def down(self):
        self.rect.y += 120