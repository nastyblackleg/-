import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullet class to shoot bullets from ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's currenct position."""
        super().__init__()
        self.screen = screen

        # Create bullet at (0,0) and set current location.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed_factor


    def update(self):
        """Moving up bullets."""
        self.y -= self.speed
        # Update decimal position of the bullet.
        self.rect.y = self.y


    def draw_bullets(self):
        """Draws bullets to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
