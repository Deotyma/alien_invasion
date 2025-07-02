import sys
import pygame

from .settings import Settings
from .ship import Ship
from .bullet import Bullet
from .alien import Alien
from time import sleep
from .game_stats import GameStats
from .button import Button

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (self.settings.bg_color)
        self.button = Button(self, "Play")
        self.stats = GameStats(self.settings)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.game_over = False

    def _create_fleet(self):
        """Create a fleet of 15 aliens in 3 rows."""
        number_aliens_x = 5  # 5 aliens per row
        number_rows = 3      # 3 rows

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def run_game(self):
        """Start the main loop for the game."""
        clock = pygame.time.Clock()
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()
            clock.tick(60)  # Limit to 60 frames per second

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if self.button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            # Reset the game stats and start a new game
            self.stats.reset_stats()
            self.stats.game_active = True
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            self.game_over = False
            pygame.mouse.set_visible(False)  # Hide the mouse cursor when game starts
            
        button_clicked = self.button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            pygame.mouse.set_visible(False)  # Hide the mouse cursor
        else:
            pygame.mouse.set_visible(True)  
                    
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break       
    
    def _update_bullets(self):
        """Update position of bullets and remove old bullets."""
        self.bullets.update()

        # Remove bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for bullet-alien collisions
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
        self._check_aliens_bottom()

        # Check for collisions with the ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit by alien!")  # Just print a message
            # sys.exit()  # Remove or comment out this line
            self._ship_hit()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left and reset the ship's position
            self.stats.ships_left -= 1
            self.ship.center_ship()
            # Empty the list of aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet of aliens
            self._create_fleet()
            # Pause the game for a moment
            sleep(0.5)
        else:
            self.stats.game_active = False
            self.game_over = True  # Set game over flag
            print("Game Over!")
            sleep(3)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change its direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1  # Reverse direction

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        if not self.stats.game_active:
            pygame.mouse.set_visible(True)  # Show the mouse cursor when game is not active
            if self.game_over:
                font = pygame.font.SysFont(None, 74)
                game_over_surface = font.render("GAME OVER", True, (255, 0, 0))
                rect = game_over_surface.get_rect(center=self.screen.get_rect().center)
                self.screen.blit(game_over_surface, rect)
            else:
                self.button.draw_button()
        pygame.display.flip()
        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()