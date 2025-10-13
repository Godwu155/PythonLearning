import pygame


class Ship:
    def __init__(self, ai_ship):
        self.screen = ai_ship.screen
        self.settings = ai_ship.settings
        self.screen_rect = ai_ship.screen.get_rect()
        # self.screen_rect.size = (200, 200)

        self.image = pygame.image.load('ship.png')
        # self.image_new = pygame.transform.scale(self.image, self.screen_rect.size)
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_factor


        self.rect.x = self.x



    def blitme(self):
        self.screen.blit(self.image, self.rect)
