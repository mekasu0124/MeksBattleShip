import pygame
import random

from pygame.locals import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, speed):
        super().__init__()

        self.screen_width = screen_width
        self.speed = speed
        self.score = 0
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,self.screen_width-40),0)

    def move(self):
        self.rect.move_ip(0,self.speed)

        if (self.rect.bottom > 600):
            self.score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30,370),0)
            