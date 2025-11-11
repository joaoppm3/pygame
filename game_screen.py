import pygame
from config import *
from assets import *
from sprites import *

def game_screen(window):
    clock = pygame.time.Clock()

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites

    player = Player(groups, assets)
    all_sprites.add(player)

    PLAY = 0
    HIT = 1
    OVER = 2
    gameplay = PLAY

    keys_down = {}

    cenario = 1

    while gameplay != OVER:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                return state
            
            if gameplay == PLAY:
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                    if event.key == pygame.K_UP:
                        player.rect.y -= 120
                        player.direction = 'b'
                        if player.rect.top == HEIGHT * 1 / 5:
                            cenario *= -1
                    if event.key == pygame.K_DOWN:
                        player.rect.y += 120
                        player.direction = 'f'
                    if event.key == pygame.K_LEFT:
                        player.rect.x -= 120
                        player.direction = 'l'
                    if event.key == pygame.K_RIGHT:
                        player.rect.x += 120
                        player.direction = 'r'

                        
                    if event.key == pygame.K_ESCAPE:
                        state = QUIT
                        return state

        player.update(assets)


        if cenario == 1:
            window.fill(YELLOW)

            window.blit(assets[STREET_IMG], (0, HEIGHT - 6 * PATH_DISTANCE))
            window.blit(assets[GRASS_IMG], (0, HEIGHT - 5 * PATH_DISTANCE))
            window.blit(assets[STREET_IMG], (0, HEIGHT - 4 * PATH_DISTANCE))
            window.blit(assets[GRASS_IMG], (0, HEIGHT - 3 * PATH_DISTANCE))
            window.blit(assets[STREET_IMG], (0, HEIGHT - 2 * PATH_DISTANCE))
            window.blit(assets[GRASS_IMG], (0, HEIGHT - PATH_DISTANCE))

        else:
            window.fill(YELLOW)

            window.blit(assets[GRASS_IMG], (0, HEIGHT - 6 * PATH_DISTANCE))
            window.blit(assets[STREET_IMG], (0, HEIGHT - 5 * PATH_DISTANCE))
            window.blit(assets[GRASS_IMG], (0, HEIGHT - 4 * PATH_DISTANCE))
            window.blit(assets[STREET_IMG], (0, HEIGHT - 3 * PATH_DISTANCE))
            window.blit(assets[GRASS_IMG], (0, HEIGHT - 2 * PATH_DISTANCE))
            window.blit(assets[STREET_IMG], (0, HEIGHT - 1 * PATH_DISTANCE))


        all_sprites.draw(window)



        pygame.display.update()

    state = GAME_OVER

    return state