import pygame
from settings import *
from game_objects import *

pygame.init()
pygame.mixer.init()

game_screen = Screen()
ball = Ball()
red_player = Player(red_player_rect, PADDLE_IMG_RED, pygame.K_w, pygame.K_s, 'red')
blue_player = Player(blue_player_rect, PADDLE_IMG_BLUE, pygame.K_UP, pygame.K_DOWN, 'blue')

# Цикл игры
running = True
while running:
    game_screen.clock.tick(FPS)
    game_screen.screen.blit(game_screen.img, (0,0))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        blue_player.check_key(event)
        red_player.check_key(event)
    
    ball.paddle_collision(blue_player, red_player)
    ball.mine_collision()
    game_screen.draw_mine(ball)
    
    blue_player.draw(game_screen.screen)
    red_player.draw(game_screen.screen)
    
    ball.draw(game_screen.screen)
    game_screen.show_score(blue_player, red_player)
    
    pygame.display.flip() # Двойная буферизация
    

pygame.quit() # Закрытие окна