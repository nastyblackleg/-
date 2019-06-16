class GameStats():
    """Track statistics"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = 0

        # Start game in an  inactive mode.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.game_active = True
        self.score = 0
        self.level = 1


