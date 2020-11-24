"""Here are all the tests for Player class."""

from unittest import TestCase
from player import Player


class TestPlayer(TestCase):
    """TestPlayer class for all Player class tests."""

    def setUp(self):
        """Init for Player class tests"""
        self.player = Player("TestPlayer", 1000)

    def test_player_name(self):
        """Test if Player gets its name right on init."""
        self.assertEqual(self.player.get_player_name(), "TestPlayer")

    def test_cash_balance(self):
        """Check that player has a right cash balance on init."""
        self.assertEqual(self.player.get_cash_balance(), 1000)

    def test_cash_add(self):
        """Check that Player's cash balance is correct after adding some cash."""
        self.player.cash_add(1000)
        self.assertEqual(self.player.get_cash_balance(), 2000)

    def test_cash_reduce(self):
        """Check that Player's cash balance is correct after reducing some cash."""
        self.player.cash_reduce(1000)
        self.assertEqual(self.player.get_cash_balance(), 0)
