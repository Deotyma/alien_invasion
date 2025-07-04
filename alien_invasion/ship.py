import pygame
from .settings import Settings

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_width, self.settings.ship_height)
        )  # width, height in pixels
        self.rect = self.image.get_rect()
        self.screen_rect = ai_game.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.x = float(self.rect.x)

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
    
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.centerx = self.screen_rect.centerx
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)