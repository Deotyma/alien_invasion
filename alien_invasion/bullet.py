import pygame
from pygame.sprite import Sprite
from .settings import Settings

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the bullet image and set its rect attribute.
        self.image = pygame.Surface((self.settings.bullet_width, self.settings.bullet_height))
        self.image.fill(self.settings.bullet_color)
        self.rect = self.image.get_rect()

        # Start each new bullet at the ship's current position.
        self.rect.centerx = ai_game.ship.rect.centerx
        self.rect.top = ai_game.ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)