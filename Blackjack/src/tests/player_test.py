"""player_test.py

    Here are all the tests for Player entities.
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
        self.assertEqual(self.player.get_name(), "TestPlayer")

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
