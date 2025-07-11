class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (3, 4, 94)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_width = 60
        self.ship_height = 80
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (217, 4, 41)
        self.bullets_allowed = 100

        # Alien settings
        self.alien_speed = 1
        self.alien_width = 60   # Try 60 instead of 80
        self.alien_height = 40  # Try 40 instead of 60
        self.fleet_drop_speed = 1
        self.fleet_direction = 1  # 1 represents right; -1 represents left   

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.alien_points = 50  # Points for each alien hit

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings for the game."""
        self.ship_speed *= 1.1
        self.bullet_speed *= 1.1
        self.alien_speed *= 1.1

    def _get_number_aliens_x(self, alien_width):
        """Determine the number of aliens that fit in a row."""
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        return int(number_aliens_x)

    def _get_number_rows(self, alien_height, ship_height):
        """Determine the number of rows of aliens that fit on the screen."""
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        return int(number_rows)