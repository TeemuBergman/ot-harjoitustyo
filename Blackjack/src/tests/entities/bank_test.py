"""bank_test.py

    Here are all the tests for Bank class.
    """

from unittest import TestCase
from entities.bank import Bank
from entities.player import Player


class TestBank(TestCase):
    """Test Bank classes different functionalitites."""

    def setUp(self):
        """Init for Player entities tests."""
        self.bank = Bank()
        self.player = Player("TestPlayer")

    def test_bet_default(self):
        """Confirm default bet."""
        self.assertEqual(self.bank.current_bet, 100)

    def test_bet_raise(self):
        """Confirm bet raise (current_bet + bet_raise)."""
        self.bank.bet_raise()
        self.assertEqual(self.bank.current_bet, 200)

    def test_bet_raise_max(self):
        """Confirm that bet can't be bigger than max_bet."""
        self.bank.current_bet = 550
        self.bank.bet_raise()
        self.assertEqual(self.bank.current_bet, 500)

    def test_bet_reduce(self):
        """Confirm bet reduce ((current_bet + bet_raise) - bet_reduce)."""
        self.bank.bet_raise()
        self.bank.bet_reduce()
        self.assertEqual(self.bank.current_bet, 100)

    def test_bet_reduce_min(self):
        """Confirm that bet can't be smaller than min_bet."""
        self.bank.current_bet = 50
        self.bank.bet_reduce()
        self.assertEqual(self.bank.current_bet, 100)

    def test_player_cash_cap(self):
        """Confirm that bet can't be higher than Players cash balance."""
        self.player.cash_balance = 100
        self.bank.current_bet = 200
        self.bank.bet_raise()
        self.bank.bet_cap(self.player)
        self.assertEqual(self.bank.current_bet, 100)