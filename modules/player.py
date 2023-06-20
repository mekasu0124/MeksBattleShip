import pygame

from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()

        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
        self.screen_width = screen_width

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)

        if self.rect.right < self.screen_width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)