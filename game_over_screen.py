#Importa bibliotecas
import pygame
from os import path
from config import *
from assets import *

def game_over_screen(window, score, highscore):
    #Inicialização
    clock = pygame.time.Clock()

    assets = load_assets()

    #Imagem de fundo
    background = pygame.image.load(path.join(IMG_DIR, 'gameover.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    #Música de game over
    pygame.mixer.music.load(os.path.join(SND_DIR, 'musicagameover.mp3'))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Fecha janela
                state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #Fecha janela
                    state = QUIT
                    running = False
                if event.key == pygame.K_RETURN: #Volta para a tela de início
                    state = INIT
                    running = False

        window.fill(BLACK)
        window.blit(background, background_rect) #Coloca imagem de fundo na tela

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

        #Coloca textos na tela depois da imagem
        window.blit(try_again, try_again_rect)
        window.blit(final_score, final_score_rect)
        window.blit(highscore_text, highscore_text_rect)
        pygame.display.flip()

    return state