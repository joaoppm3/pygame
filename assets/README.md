# POR QUE ATRAVESSOU?
O jogo que se coloca na visão da galinha que atravessou a rua para chegar do outro lado

- João Pedro Mendes
- Teo Lacerda
- Caio Sandrini

A pergunta que não quer calar é "Por que a galinha atravessou a rua?" e nesse jogo arcade estilo 8-bit embarcamos na jornada de chegar do outro lado da rua, se enfiando entre os carros e esquivando de motoristas velozes para conseguir levar essa ave corajosa o mais longe possível.

# Como Jogar

- **Setas do teclado** para se mover:
  - ← → ↑ ↓
- **Objetivo:** Ir o mais longe possível com a galinha curiosa.
- **Evite** colisões com os **carros** — ao bater a jornada com a galinha acaba.

# Regras do Jogo

- Tente chegar o mais longe que conseguir
- O cenário acompanha a galinha
- Os carros ficam cada vez mais rápido e imprevisíveis
- Não seja atropelado (Se não é pena para todo lado)



# Estrutura do Projeto

├── assets/                # Recursos do jogo (imagens, fontes, sons)
│   ├── img/               # Imagens como carros, grama, ratos, etc.
│   ├── fnt/               # Fonte usada no jogo (PressStart2P.ttf)
│   ├── snd/               # Recursos auditivos como efeitos sonoros, música etc.
├── config.py              # Constantes globais e configurações do jogo
├── assets.py              # Carregamento de imagens e fontes
├── sprites.py             # Classes dos personagens (Player e Obstáculo)
├── init_screen.py         # Tela inicial
├── game_screen.py         # Tela principal do jogo (loop principal)
├── game_over_screen.py    # Tela de fim de jogo
├── info_screen.py         # Tela de informações sobre o jogo
├── jogo.py                # Arquivo principal que gerencia os estados

# Video de demonstração

A seguir um video curto postado no Youtube demonstrando todo o funcionamento do jogo (de tela de início, gameplay e gameover)

https://youtube.com/shorts/3-xE15UAGtE?si=4R9DzsXpYywBr0M1

