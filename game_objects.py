from random import randint, choice, uniform
import pygame
from settings import *

class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.img = pygame.transform.scale(BACKGROUND, (WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.font = pygame.font.Font(None, 80)
        
    def draw_mine(self, ball):
        for mine in ball.list_mine:
            mine.draw(self.screen)
            
    def show_score(self, blue_player, red_player):
        player1_score_surface = self.font.render(str(red_player.score), True, (44, 174, 247))
        player2_score_surface = self.font.render(str(blue_player.score), True, (191, 19, 21))

        self.screen.blit(player1_score_surface, (425, 150))
        self.screen.blit(player2_score_surface, (1020, 150))
        
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_SIZE,BALL_SIZE)
        self.img = pygame.transform.scale(BALL_IMG, (BALL_SIZE,BALL_SIZE))
        self.list_mine = []
        self.speed_x = BALL_SPEED
        self.speed_y = BALL_SPEED
        
        
    def draw(self,screen):
        screen.blit(self.img, self.rect)
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.x < 0: self.speed_x *= -1
        if self.rect.x + BALL_SIZE > WIDTH: self.speed_x *= -1
        
        if self.rect.y < 218: self.speed_y *= -1
        if self.rect.y + BALL_SIZE > HEIGHT: self.speed_y *= -1
        
    def paddle_collision(self, player_red, player_blue):
        if self.rect.right >= WIDTH:
            player_blue.score += 1
            self.start_pos()
            self.list_mine = []
            
        if self.rect.left <= 0:
            player_red.score += 1
            self.start_pos()
            self.list_mine = []
            
        if self.rect.colliderect(player_blue.rect):
            self.rect.left = player_blue.rect.right + 1
            self.speed_x *= -1
            
            r = uniform(0.5, 1.5)
            if (self.speed_x < 0):
                self.speed_x = -BALL_SPEED * r
            else:
                self.speed_x = BALL_SPEED * r
        
            self.speed_y *= uniform(0.5, 1.5)

            new_mine = Mines(MINES_RED)
            self.list_mine.append(new_mine)
            
        if self.rect.colliderect(player_red.rect):
            self.rect.right = player_red.rect.left - 1
            self.speed_x *= -1
            
            r = uniform(0.5, 1.5)
            if (self.speed_x < 0):
                self.speed_x = -BALL_SPEED * r
            else:
                self.speed_x = BALL_SPEED * r
        
            self.speed_y *= uniform(0.5, 1.5)
                
            new_mine = Mines(MINES_RED)
            self.list_mine.append(new_mine)
    
    def start_pos(self):
        self.rect.center = (WIDTH//2, HEIGHT//2)
        self.speed_x = choice([-1,1]) * BALL_SPEED
        self.speed_y = choice([-1,1]) * BALL_SPEED
        
    def mine_collision(self):
        for mine in self.list_mine:
            if self.rect.colliderect(mine.rect):
                if abs(self.speed_x) < 10:
                    self.speed_x *= uniform(-1.25, -2.5)
                else:
                    self.speed_x *= -1
                
                if abs(self.speed_y) < 10:
                    self.speed_y *= uniform(1.25, 2.5)
                self.list_mine.remove(mine)

class Player:
    def __init__(self, data, img, key_up, key_down, color_player):
        self.rect = pygame.Rect(data)
        self.img = pygame.transform.scale(img, (PADDLE_WIDTH, PADDLE_HEIGHT))
        self.key_up = key_up
        self.key_down = key_down
        self.speed = 0
        self.score = 0
        self.color = color_player
        
    def draw(self, screen):
        screen.blit(self.img, self.rect)
        self.rect.y += self.speed
        
        if self.rect.top < 218: self.rect.top = 218
        if self.rect.bottom > HEIGHT: self.rect.bottom = HEIGHT
        
    def check_key(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.key_up:
                self.speed = -PADDLE_SPEED
            if event.key == self.key_down:
                self.speed = PADDLE_SPEED
                
        if event.type == pygame.KEYUP:
            if (event.key == self.key_up) or (event.key == self.key_down):
                self.speed = 0

                
class Mines:
    def __init__(self, img):
        self.rect = pygame.Rect(randint(400, WIDTH - 400),
                                randint(MINES_SIZE*2 + 218, HEIGHT - MINES_SIZE*3),
                                MINES_SIZE, MINES_SIZE)
        self.img = pygame.transform.scale(img, (MINES_SIZE, MINES_SIZE))
        
    def draw(self, screen):
        screen.blit(self.img, self.rect)
        
        