from os import path

IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fnt')

WIDTH = 1200
HEIGHT = 600
FPS = 60

PLAYER_HEIGHT = 120
PLAYER_WIDTH = 120
PATH_HEIGHT = 180
PATH_WIDTH = 1200
PATH_DISTANCE = 120
CAR_WIDTH = 150
CAR_HEIGHT = 150

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

INIT = 0
INFO = 1
GAME = 2
GAME_OVER = 3
QUIT = 4