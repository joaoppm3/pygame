import pygame
from os import path
from config import *
from assets import *

def init_screen(window):
    clock = pygame.time.Clock()

    assets = load_assets()

    background = pygame.image.load(path.join(IMG_DIR, 'initscreen.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    pygame.mixer.music.load(os.path.join(SND_DIR, 'musicajogo.mp3'))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)
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
                if event.key == pygame.K_ESCAPE:
                    state = QUIT
                    running = False

        window.fill(WHITE)
        window.blit(background, background_rect)

        #Textos de instrução
        jogar_texto = assets[bit_FONT].render('Pressione ENTER para jogar', True, BLACK)
        jogar_texto_rect = jogar_texto.get_rect()
        jogar_texto_rect.midbottom = (WIDTH/2, HEIGHT - 100)

        infos_texto = assets[bit_FONT].render('Pressione BARRA DE ESPAÇO para informações', True, BLACK)
        infos_texto_rect = infos_texto.get_rect()
        infos_texto_rect.midbottom = (WIDTH/2, HEIGHT - 50)

        #Coloca tudo na tela
        window.blit(jogar_texto, jogar_texto_rect)
        window.blit(infos_texto, infos_texto_rect)
        pygame.display.flip()

    return state