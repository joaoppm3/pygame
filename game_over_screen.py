import pygame
from os import path
from config import *
from assets import *

def game_over_screen(window, score, highscore):
    clock = pygame.time.Clock()

    assets = load_assets()

    background = pygame.image.load(path.join(IMG_DIR, 'gameover.png')).convert()
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
                    state = QUIT
                    running = False
                if event.key == pygame.K_RETURN:
                    state = INIT
                    running = False

        window.fill(BLACK)
        window.blit(background, background_rect)

        #Texto para jogar de novo
        try_again = assets[bit_FONT].render('Pressione Enter para jogar de novo', True, WHITE)
        try_again_rect = try_again.get_rect()
        try_again_rect.midbottom = (WIDTH/2, HEIGHT/2)

        #Texto de pontuação
        final_score = assets[bit_FONT].render('Sua pontuação foi de {} pontos'.format(score), True, BLACK)
        final_score_rect = final_score.get_rect()
        final_score_rect.midbottom = (WIDTH/2, HEIGHT - 100)

        #Texto de recorde (Por programa rodado)
        highscore_text = assets[bit_FONT].render('A maior pontuação é de {} pontos'.format(highscore), True, BLACK)
        highscore_text_rect = highscore_text.get_rect()
        highscore_text_rect.midbottom = (WIDTH/2, HEIGHT - 50)

        #Coloca tudo na tela
        window.blit(try_again, try_again_rect)
        window.blit(final_score, final_score_rect)
        window.blit(highscore_text, highscore_text_rect)
        pygame.display.flip()

    return state