"""player_test.py

    Here are all the tests for Player class.
    """

from unittest import TestCase
from entities.player import Player


class TestPlayer(TestCase):
    """TestPlayer entities for all Player entities tests."""

    def setUp(self):
        """Init for Player entities tests"""
        self.player = Player("TestPlayer", 1000)

    def test_player_name(self):
        """Test if Player gets its name right on init."""
        self.assertEqual(self.player.name, "TestPlayer")

    def test_cash_balance(self):
        """Check that player has a right cash balance on init."""
        self.assertEqual(self.player.cash_balance, 1000)

    def test_cash_add(self):
        """Check that Player's cash balance is correct after adding some cash."""
        self.player.cash_add(1000)
        self.assertEqual(self.player.cash_balance, 2000)

    def test_cash_reduce(self):
        """Check that Player's cash balance is correct after reducing some cash."""
        self.player.cash_reduce(1000)
        self.assertEqual(self.player.cash_balance, 0)

    def test_save_game(self):
        """Test that saved game data is returned correctly."""
        self.player.name = "TestBot"
        self.player.cash_balance = 99
        self.assertEqual(self.player.save_game(), ("TestBot", 99))

    def test_load_game(self):
        """Test that loaded game data is saved correctly to variables."""
        self.player.load_game(("TestBot", 99))
        self.assertEqual(self.player.name, "TestBot")
        self.assertEqual(self.player.cash_balance, 99)
