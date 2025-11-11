import pygame
import os
from config import *

STREET_IMG = 'street'
GRASS_IMG = 'grass'
PLAYER_IMG = 'player'

def load_assets():
    assets = {}

    assets[GRASS_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'grama.png')).convert_alpha()
    assets[STREET_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'rua.png')).convert_alpha()
    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'player.png')).convert_alpha()

    assets[PLAYER_IMG] = pygame.transform.scale(assets[PLAYER_IMG], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[GRASS_IMG] = pygame.transform.scale(assets[GRASS_IMG], (PATH_WIDTH, PATH_HEIGHT))
    assets[STREET_IMG] = pygame.transform.scale(assets[STREET_IMG], (PATH_WIDTH, PATH_HEIGHT))
    return assets