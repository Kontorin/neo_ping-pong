import pygame

# Параметры экрана
WIDTH = 1268
HEIGHT = 850
FPS = 120
BACKGROUND = pygame.image.load('assets/back_neon_1.png')
TITLE = "NEO ping-pong"

# Параметры мяча
BALL_SIZE = 50
BALL_IMG = pygame.image.load('assets/ball_neon_green.png')
BALL_SPEED = 5

# Параметры ракеток
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 200
PADDLE_IMG_RED = pygame.image.load('assets/blue.png')
PADDLE_IMG_BLUE = pygame.image.load('assets/red.png')
PADDLE_SPEED = 10

red_player_rect = (0, HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
blue_player_rect = (WIDTH - PADDLE_WIDTH, HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)


# Параметры мин
MINES_RED = pygame.image.load('assets/mine_neon_red.png')
MINES_SIZE = 30

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)