#Importa bibliotecas
import pygame 
import random
from config import *
from assets import *

#Define o player (Galinha)
class Player(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.direction = 'f' #Começa de frente

        #Sprite inicial
        self.image = assets[PLAYER_F]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        #Posição inicial
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT
        self.assets = assets

    def update(self, score):
        
        #Impede de sair da tela pelos lados
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
        #Impede de sair da tela por baixo e passar da metade
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < HEIGHT * 2 / 5:
            self.rect.top = HEIGHT * 2 / 5

        #Muda o sprite de acordo com a direção
        self.image = self.assets['player'+self.direction]
        self.mask = pygame.mask.from_surface(self.image)

#Define os obstáculos (Carros)
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, assets, i):
        pygame.sprite.Sprite.__init__(self)

        speed = random.randint(5, 15) #Velocidade aleatória

        #Posições de início dos carros
        if i % 2 == 0:
            direcao = 'e'
            posix = WIDTH
            posiy = -120 + 240 * (i / 2)
            speed *= -1
        else:
            direcao = 'd'
            posix = 0 - CAR_WIDTH
            posiy = -120 + 240 * (i // 2) + 48
            speed = speed

        #Cor aleatória
        colour = random.randint(1, 3)
        if colour == 1:
            colour = 'r'
        elif colour == 2:
            colour = 'y'
        else:
            colour = 'b'

        #Define tudo para cada Sprite (usando o self.)
        self.assets = assets
        self.direcao = direcao
        self.image = assets[colour+direcao]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = posix
        self.rect.y = posiy
        self.speed = speed

    def update(self, score):
        self.rect.x += self.speed #Muda a posição

        speed = random.randint(5, 15) + score / 10 #Velocidade aleatória, dependendo dos pontos

        #Mesmo sistema de cor aleatória
        colour = random.randint(1, 3)
        if colour == 1:
            colour = 'r'
        elif colour == 2:
            colour = 'y'
        else:
            colour = 'b'

        #Controla saída do carro da tela
        if self.direcao == 'e':
            if self.rect.right < 0: #Se sair pelo lado, volta do começo mudando velocidade e a cor
                self.image = self.assets[colour+self.direcao]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect.x = WIDTH
                self.speed = - speed
            if self.rect.centery > HEIGHT: #Se sair por baixo (pista ficou para trás), vai para uma pista de cima (fora da tela)
                self.rect.y = -120
        else:
            if self.rect.left > WIDTH: #Mesmo aqui
                self.image = self.assets[colour+self.direcao]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect.right = 0
                self.speed = speed
            if self.rect.top > HEIGHT: #Mesmo aqui
                self.rect.y = -120 + 48
    
    #Para o carro acompanhar a mudança do layout (pista ficar para trás)
    def down(self):
        self.rect.y += 120