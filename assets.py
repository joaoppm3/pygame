import pygame
import os
from config import *

STREET_IMG = 'street'
GRASS_IMG = 'grass'
PLAYER_F = 'playerf'
PLAYER_B = 'playerb'
PLAYER_R = 'playerr'
PLAYER_L = 'playerl'


def load_assets():
    assets = {}

    assets[GRASS_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'grama.png')).convert_alpha()
    assets[STREET_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'rua.png')).convert_alpha()
    assets[PLAYER_F] = pygame.image.load(os.path.join(IMG_DIR, 'player.png')).convert_alpha()
    assets[PLAYER_B] = pygame.image.load(os.path.join(IMG_DIR, 'player_back.png')).convert_alpha()
    assets[PLAYER_R] = pygame.image.load(os.path.join(IMG_DIR, 'player_right.png')).convert_alpha()
    assets[PLAYER_L] = pygame.image.load(os.path.join(IMG_DIR, 'player_left.png')).convert_alpha()

    assets[PLAYER_F] = pygame.transform.scale(assets[PLAYER_F], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[PLAYER_B] = pygame.transform.scale(assets[PLAYER_B], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[PLAYER_R] = pygame.transform.scale(assets[PLAYER_R], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[PLAYER_L] = pygame.transform.scale(assets[PLAYER_L], (PLAYER_WIDTH, PLAYER_HEIGHT))
    
    assets[GRASS_IMG] = pygame.transform.scale(assets[GRASS_IMG], (PATH_WIDTH, PATH_HEIGHT))
    assets[STREET_IMG] = pygame.transform.scale(assets[STREET_IMG], (PATH_WIDTH, PATH_HEIGHT))
    return assets