import pygame
from os import path
from config import *
from assets import *

def info_screen(window):
    clock = pygame.time.Clock()

    assets = load_assets()

    background = pygame.image.load(path.join(IMG_DIR, 'infos.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = INIT
                    running = False

        window.fill(GREEN)
        window.blit(background, background_rect)

        pygame.display.flip()

    return state