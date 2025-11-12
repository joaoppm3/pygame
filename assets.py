import pygame
import os
from config import *

STREET_IMG = 'street'
GRASS_IMG = 'grass'
PLAYER_F = 'playerf'
PLAYER_B = 'playerb'
PLAYER_R = 'playerr'
PLAYER_L = 'playerl'
CAR_RD = 'rd'
CAR_YD = 'yd'
CAR_BD = 'bd'
CAR_RE = 're'
CAR_YE = 'ye'
CAR_BE = 'be'

bit_FONT = 'bit_font'

def load_assets():
    assets = {}

    assets[GRASS_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'grama.png')).convert_alpha()
    assets[STREET_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'rua.png')).convert_alpha()
    assets[PLAYER_F] = pygame.image.load(os.path.join(IMG_DIR, 'player.png')).convert_alpha()
    assets[PLAYER_B] = pygame.image.load(os.path.join(IMG_DIR, 'player_back.png')).convert_alpha()
    assets[PLAYER_R] = pygame.image.load(os.path.join(IMG_DIR, 'player_right.png')).convert_alpha()
    assets[PLAYER_L] = pygame.image.load(os.path.join(IMG_DIR, 'player_left.png')).convert_alpha()
    assets[CAR_RD] = pygame.image.load(os.path.join(IMG_DIR, 'carro_rd.png')).convert_alpha()
    assets[CAR_YD] = pygame.image.load(os.path.join(IMG_DIR, 'carro_yd.png')).convert_alpha()    
    assets[CAR_BD] = pygame.image.load(os.path.join(IMG_DIR, 'carro_bd.png')).convert_alpha()
    assets[CAR_RE] = pygame.image.load(os.path.join(IMG_DIR, 'carro_re.png')).convert_alpha()
    assets[CAR_YE] = pygame.image.load(os.path.join(IMG_DIR, 'carro_ye.png')).convert_alpha()
    assets[CAR_BE] = pygame.image.load(os.path.join(IMG_DIR, 'carro_be.png')).convert_alpha()

    assets[PLAYER_F] = pygame.transform.scale(assets[PLAYER_F], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[PLAYER_B] = pygame.transform.scale(assets[PLAYER_B], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[PLAYER_R] = pygame.transform.scale(assets[PLAYER_R], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[PLAYER_L] = pygame.transform.scale(assets[PLAYER_L], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[CAR_RD] = pygame.transform.scale(assets[CAR_RD], (CAR_WIDTH, CAR_HEIGHT))
    assets[CAR_YD] = pygame.transform.scale(assets[CAR_YD], (CAR_WIDTH, CAR_HEIGHT))    
    assets[CAR_BD] = pygame.transform.scale(assets[CAR_BD], (CAR_WIDTH, CAR_HEIGHT))
    assets[CAR_RE] = pygame.transform.scale(assets[CAR_RE], (CAR_WIDTH, CAR_HEIGHT))
    assets[CAR_YE] = pygame.transform.scale(assets[CAR_YE], (CAR_WIDTH, CAR_HEIGHT))
    assets[CAR_BE] = pygame.transform.scale(assets[CAR_BE], (CAR_WIDTH, CAR_HEIGHT))

    assets[GRASS_IMG] = pygame.transform.scale(assets[GRASS_IMG], (PATH_WIDTH, PATH_HEIGHT))
    assets[STREET_IMG] = pygame.transform.scale(assets[STREET_IMG], (PATH_WIDTH, PATH_HEIGHT))

    assets[bit_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2p.ttf'), 28)
    return assets