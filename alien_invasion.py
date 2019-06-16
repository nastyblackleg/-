"""
Alien Invasion game with right-left arrow to move and spacebar to shoot
"""
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button


def run_game():
        pygame.init()
        ai_settings = Settings()

        # Making screen resolution with width and height from settings.
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # Create an instance to store game stats and create a scoreboard
        stats = GameStats(ai_settings)
        scoreboard = Scoreboard(ai_settings, screen, stats)

        # Creating ship object
        ship = Ship(ai_settings, screen)

        # Game name in window
        pygame.display.set_caption('Alien Invasion')

        # Make a group to store bullets in.
        bullets = Group()

        # Make a group of aliens.
        aliens = Group()

        # Make play button.
        play_button = Button(ai_settings, screen, 'Play')

        # Create fleet of aliens.
        gf.create_fleet(ai_settings, screen, ship, aliens)

        while True:
                gf.check_events(ai_settings, screen, stats, scoreboard, play_button, ship, aliens, bullets)

                if stats.game_active:
                        ship.update()
                        gf.update_bullets(ai_settings, screen, stats, scoreboard, ship, aliens, bullets)
                        gf.update_aliens(ai_settings, screen, stats, scoreboard, ship, aliens, bullets)
                # Make changes visible to the screen.
                gf.update_screen(ai_settings, screen, stats, scoreboard, ship, aliens, bullets, play_button)


run_game()

