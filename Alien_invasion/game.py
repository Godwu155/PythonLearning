import  pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullet = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self._update_bullets()
            pygame.display.flip()
            self.clock.tick(60)


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_KEYDOWN_events(event)
            elif event.type == pygame.KEYUP:
                self._check_KEYUP_events(event)

    def _check_KEYDOWN_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            self._fire_buller()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_KEYUP_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_buller(self):
        if len(self.bullet) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullet.add(new_bullet)

    def _update_bullets(self):
        self.bullet.update()

        for bullet in self.bullet.copy():
            if bullet.rect.bottom <= 0:
                self.bullet.remove(bullet)
        print(len(self.bullet))

    def _create_fleet(self):

        #创建外星人舰队
        alien = Alien(self)
        alien_width = alien.rect.width

        current_x = alien_width
        while current_x < (self.settings.screen_width - 2 * alien_width):
            self._create_alien(current_x)
            current_x += 2*alien_width

    def _create_alien(self, x_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()



if __name__ == '__main__':
    alien = AlienInvasion()
    alien.run_game()