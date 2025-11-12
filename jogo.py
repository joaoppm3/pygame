#Importa biblitecas
import pygame
import random
from config import *
from init_screen import init_screen
from info_screen import info_screen
from game_screen import game_screen
from game_over_screen import game_over_screen

#Inicia pygame
pygame.init()
pygame.mixer.init()

#Abre a janela
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Por que Atravessou?')

highscore = 0

#Define a alteração entre as 4 telas do jogo
state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == INFO:
        state = info_screen(window)
    elif state == GAME:
        gameplayed = game_screen(window)
        state = gameplayed[0]
        score = gameplayed[1] #Pegamos a pontuação para guardar o highscore
    elif state == GAME_OVER:
        if score > highscore:
            highscore = score #Guardado aqui
        state = game_over_screen(window, score, highscore)
    else:
        state = QUIT

pygame.quit()