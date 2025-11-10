import pygame
import random
from config import *
from init_screen import init_screen
from info_screen import info_screen
from game_screen import game_screen
from game_over_screen import game_over_screen

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('-')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == INFO:
        state = info_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == GAME_OVER:
        state = game_over_screen(window)
    else:
        state = QUIT

pygame.quit()