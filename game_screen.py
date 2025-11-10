import pygame
from config import *

def game_screen(window):
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    state = GAME_OVER
                    running = False
                if event.key == pygame.K_ESCAPE:
                    state = QUIT
                    running = False

        window.fill(BLUE)

        pygame.display.flip()

    return state