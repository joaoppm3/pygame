import pygame
import random
from config import *
from init_screen import init_screen

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('-')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    #elif state == GAME:
        #gameplayed = game_screen(window)
    #elif state == INFO:
        #state = info_screen(window)
    #elif state == GAME_OVER:
        #state = game_over_screen(window)
    #else:
        state = QUIT

pygame.quit()