import sys
import pygame
import time

from pygame.locals import *
from modules.player import Player
from modules.enemy import Enemy

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5

P1 = Player(SCREEN_WIDTH)
E1 = Enemy(SCREEN_WIDTH, SPEED)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
font_medium = pygame.font.SysFont("Verdana", 40)

game_over = font.render("Game Over", True, BLACK)
game_over2 = font_medium.render(f"Your Score: {E1.score}", True, BLACK)

background = pygame.image.load("Space.jpg")

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(f"Score: {E1.score}", True, WHITE)
    DISPLAYSURF.blit(scores, (10,10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        DISPLAYSURF.blit(game_over2, (60,330))

        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)