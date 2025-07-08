import pygame.font
import platform

class ButtonMusic:
    """A class to create a button for toggling music."""

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 255)  # Blue color
        self.text_color = (255, 255, 255)  # White color

        # Determine the font name based on the operating system
        if platform.system() == "Windows":
            font_name = "Segoe UI Emoji"
        else:
            font_name = None  # fallback to default
        self.font = pygame.font.SysFont(font_name, 48)

        # Create the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button with its message."""
        # Draw the button rectangle and then the message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class YourGameClass:
    def __init__(self):
        # ... your initialization code ...
        self.button_music = ButtonMusic(self, "🎵̶")  # or "🔇"
    # ... rest of your game class code ...