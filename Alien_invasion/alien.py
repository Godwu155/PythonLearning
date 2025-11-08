import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        #加载图片
        self.image = pygame.image.load('Alienship(1).png')
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.x = float(self.rect.x)