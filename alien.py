import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    aliens = ['alien_1.bmp', 'alien_2.bmp']

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting point."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load(self.aliens[randint(0, 1)])
        self.image = pygame.transform.scale(self.image, (65, 65))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """Move the aliens right or right."""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x


    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

