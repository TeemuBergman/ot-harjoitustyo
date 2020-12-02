"""Here are all the tests for Game class."""

from unittest import TestCase
from game import Game


class TestGame(TestCase):
    """TestGame class for all Game class tests."""

    def setUp(self):
        """Init for Game class tests"""
        self.game = Game()
        self.card_1 = 7
        self.card_2 = 4
        self.card_3 = 10

    def test_bet_size(self):
        """Bet size is correct on init."""
        self.assertEqual(self.game.get_bet(), 100)

    def test_bet_raise(self):
        """Bet size is correct on after one raise (100 -> 200)."""
        self.game.bet_raise()
        self.assertEqual(self.game.get_bet(), 200)

    def test_bet_reduce(self):
        """Bet size is correct on after one reduce (100 -> 100)."""
        self.game.bet_reduce()
        self.assertEqual(self.game.get_bet(), 100)

    def test_player_under_21_status(self):
        """The sum of Players hand is under 21."""
        self.game.player.hand.add_card(self.card_1)
        self.game.player.hand.add_card(self.card_2)
        self.assertEqual(self.game.get_player_status(), True)

    def test_player_blackjack_status(self):
        """The sum of Players hand equals to 21 (blackjack)."""
        self.game.player.hand.add_card(self.card_1)
        self.game.player.hand.add_card(self.card_2)
        self.game.player.hand.add_card(self.card_3)
        self.assertEqual(self.game.get_player_status(), False)

    def test_player_busted_status(self):
        """The sum of Players hand is more than 21 (busted!)."""
        self.game.player.hand.add_card(self.card_1)
        self.game.player.hand.add_card(self.card_2)
        self.game.player.hand.add_card(self.card_3)
        self.game.player.hand.add_card(self.card_1)
        self.assertEqual(self.game.get_player_status(), False)

    def test_dealer_under_21_status(self):
        """The sum of Dealers hand is under 21."""
        self.game.dealer.hand.add_card(self.card_1)
        self.game.dealer.hand.add_card(self.card_2)
        self.assertEqual(self.game.get_dealer_status(), True)

    def test_dealer_blackjack_status(self):
        """The sum of Dealers hand equals to 21 (blackjack)."""
        self.game.dealer.hand.add_card(self.card_1)
        self.game.dealer.hand.add_card(self.card_2)
        self.game.dealer.hand.add_card(self.card_3)
        self.assertEqual(self.game.get_dealer_status(), False)

    def test_dealer_busted_status(self):
        """The sum of Dealers hand is more than 21 (busted!)."""
        self.game.dealer.hand.add_card(self.card_1)
        self.game.dealer.hand.add_card(self.card_2)
        self.game.dealer.hand.add_card(self.card_3)
        self.game.dealer.hand.add_card(self.card_1)
        self.assertEqual(self.game.get_dealer_status(), False)
