import pygame
from os import path
from config import *

def init_screen(window):
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state = GAME
                    running = False
                if event.key == pygame.K_SPACE:
                    state = INFO
                    running = False

        window.fill(WHITE)

        pygame.display.flip()

    return state