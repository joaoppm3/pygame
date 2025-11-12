#Importa biblioteca
import pygame
from config import *
from assets import *
from sprites import *

def game_screen(window):
    #Inicialização
    clock = pygame.time.Clock()

    assets = load_assets()

    assets[SOM_INICIO].play() #Cocoricó para marcar começo

    all_sprites = pygame.sprite.Group()
    all_cars = pygame.sprite.Group()
    cars = [0] * 6

    #Cria os sprites
    player = Player(assets)
    all_sprites.add(player)

    for i in range (0, 6):
        carro = Obstacle(assets, i)
        all_cars.add(carro)
        all_sprites.add(carro)
        cars[i] = carro

    #Fases do jogo
    PLAY = 0
    HIT = 1
    OVER = 2
    gameplay = PLAY

    keys_down = {}
    score = 0
    cenario = 1 #Layout inicial das pistas e grama

    while gameplay != OVER:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Fechar janela
                state = QUIT
                return state
            
            if gameplay == PLAY:
                #Movimentação do player com as setas
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                    if event.key == pygame.K_UP:
                        player.rect.y -= 120
                        player.direction = 'b'
                        if player.rect.top == HEIGHT * 1 / 5: #Quando chega na metade, o layout muda, como se centralizasse no player e o chão fica para trás
                            cenario *= -1 #Mudança do layout das pistas e grama
                            score += 5
                            for i in range (0, 6):
                                cars[i].down()
                    if event.key == pygame.K_DOWN:
                        player.rect.y += 120
                        player.direction = 'f'
                    if event.key == pygame.K_LEFT:
                        player.rect.x -= 120
                        player.direction = 'l'
                    if event.key == pygame.K_RIGHT:
                        player.rect.x += 120
                        player.direction = 'r'

                        
                    if event.key == pygame.K_ESCAPE: #Tecla Esc para fechar janela
                        state = QUIT
                        return state

        all_sprites.update(score) #Atualiza os sprites (Posição, imagem, velocidade etc.)

        if gameplay == PLAY:
            
            #Detecta colisões
            hits = pygame.sprite.spritecollide(player, all_cars, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                player.kill()
                gameplay = HIT
                assets[SOM_MORTE].play()

        if gameplay == HIT:
            pygame.time.delay(1000) #Morte com delay, instantâneo fica confuso
            gameplay = OVER
        
        if cenario == 1: #Layout inicial: grama, rua, grama, rua, grama
            window.fill(YELLOW)

            window.blit(assets[STREET_IMG], (0, HEIGHT - 6 * PATH_DISTANCE))
            window.blit(assets[GRASS_IMG], (0, HEIGHT - 5 * PATH_DISTANCE))
            window.blit(assets[STREET_IMG], (0, HEIGHT - 4 * PATH_DISTANCE))
            window.blit(assets[GRASS_IMG], (0, HEIGHT - 3 * PATH_DISTANCE))
            window.blit(assets[STREET_IMG], (0, HEIGHT - 2 * PATH_DISTANCE))
            window.blit(assets[GRASS_IMG], (0, HEIGHT - PATH_DISTANCE))

        else: #Layout 2: rua, grama, rua, grama, rua
            window.fill(YELLOW)

            window.blit(assets[GRASS_IMG], (0, HEIGHT - 6 * PATH_DISTANCE))
            window.blit(assets[STREET_IMG], (0, HEIGHT - 5 * PATH_DISTANCE))
            window.blit(assets[GRASS_IMG], (0, HEIGHT - 4 * PATH_DISTANCE))
            window.blit(assets[STREET_IMG], (0, HEIGHT - 3 * PATH_DISTANCE))
            window.blit(assets[GRASS_IMG], (0, HEIGHT - 2 * PATH_DISTANCE))
            window.blit(assets[STREET_IMG], (0, HEIGHT - 1 * PATH_DISTANCE))


        all_sprites.draw(window) #Coloca os sprites depois do cenário

        #Texto de pontuação
        text_score = assets[bit_FONT].render('{:05d}'.format(score), True, BLACK)
        text_score_rect = text_score.get_rect()
        text_score_rect.bottomright = (WIDTH - 10, HEIGHT - 10)
        window.blit(text_score, text_score_rect)

        pygame.display.update()

    state = GAME_OVER

    return [state, score] #Devolve pontuação para guardar o highscore