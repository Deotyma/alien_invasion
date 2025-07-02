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

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (217, 4, 41)
        self.bullets_allowed = 100

        # Alien settings
        self.alien_speed = 1
        self.alien_width = 80
        self.alien_height = 60  
        self.fleet_drop_speed = 1
        self.fleet_direction = 1  # 1 represents right; -1 represents left   