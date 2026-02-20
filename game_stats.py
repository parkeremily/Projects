import json
from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset
        self.high_score = 0

        # Load high score from file
        self._load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        """Load high score from file."""
        path = Path("high_score.json")
        if path.exists():
            self.high_score = json.loads(path.read_text())
        else:
            self.high_score = 0

    def save_high_score(self):
        """Save high score to file."""
        path = Path("high_score.json")
        path.write_text(json.dumps(self.high_score))
