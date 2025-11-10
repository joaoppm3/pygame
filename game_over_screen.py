import pygame
from os import path
from config import *

def game_over_screen(window):
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = QUIT
                    running = False
                if event.key == pygame.K_RETURN:
                    state = INIT
                    running = False

        window.fill(BLACK)

        pygame.display.flip()

    return state