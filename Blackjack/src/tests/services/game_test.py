"""game_test.py

    Here are all the tests for Game class.
    """

from unittest import TestCase, mock
from services.game import Game


class TestGame(TestCase):
    """TestGame entities for all Game entities tests."""

    def setUp(self):
        """Init for Game entities tests"""
        self.game = Game()

    # Player tests

    def test_boolean_player_blackjack_true(self):
        """Sum of Players hand does equal to 21 (blackjack)."""
        self.game.player.hand.add_card(10)
        self.game.player.hand.add_card(1)
        self.assertTrue(self.game.check_for_blackjack(self.game.player))

    def test_boolean_player_blackjack_false(self):
        """Sum of Players hand does not equal to 21 (blackjack)."""
        self.game.player.hand.add_card(1)
        self.game.player.hand.add_card(1)
        self.assertFalse(self.game.check_for_blackjack(self.game.player))

    def test_boolean_player_21_false(self):
        """The sum of Players hand is under 21."""
        self.game.player.hand.add_card(1)
        self.game.player.hand.add_card(1)
        self.assertFalse(self.game.check_for_21(self.game.player))

    def test_boolean_player_21_true(self):
        """The sum of Players hand is 21."""
        self.game.player.hand.add_card(10)
        self.game.player.hand.add_card(1)
        self.assertTrue(self.game.check_for_21(self.game.player))

    def test_boolean_player_busted_false(self):
        """The sum of Players hand is less than 21 (busted!)."""
        self.game.player.hand.add_card(10)
        self.game.player.hand.add_card(10)
        self.assertFalse(self.game.check_for_bust(self.game.player))

    def test_boolean_player_busted_true(self):
        """The sum of Players hand is more than 21 (busted!)."""
        self.game.player.hand.add_card(10)
        self.game.player.hand.add_card(10)
        self.game.player.hand.add_card(10)
        self.assertTrue(self.game.check_for_bust(self.game.player))

    def test_compare_player_21(self):
        """Sum of Players hand does equal to 21 (blackjack)."""
        self.game.player.hand.add_card(10)
        self.game.player.hand.add_card(1)
        self.game.compare_hands(self.game.player)
        self.assertEqual(self.game.player.cash_balance, 1100)

    def test_compare_player_busted(self):
        """Sum of Players hand is more than 21."""
        self.game.dealer.hand.add_card(10)
        self.game.dealer.hand.add_card(7)
        self.game.player.hand.add_card(10)
        self.game.player.hand.add_card(10)
        self.game.player.hand.add_card(10)
        self.game.compare_hands(self.game.player)
        self.assertEqual(self.game.player.cash_balance, 900)

    def test_player_status_busted(self):
        """The sum of Players hand is more than 21 (busted!)."""
        self.game.players_turn = True
        self.game.player.hand.add_card(10)
        self.game.player.hand.add_card(10)
        self.game.player.hand.add_card(10)
        self.game.player_check_status()
        self.assertFalse(self.game.players_turn)

    def test_player_status_21(self):
        """The sum of Players hand is 21."""
        self.game.players_turn = True
        self.game.player.hand.add_card(10)
        self.game.player.hand.add_card(1)
        self.game.player_check_status()
        self.assertFalse(self.game.players_turn)

    def test_deal_player_cards_pass(self):
        """Player decides to (p)ass his turn."""
        with mock.patch("builtins.input", return_value = "p"):
            self.game.player_deal_cards()
            self.assertFalse(self.game.players_turn)

    def test_deal_player_cards_hit_one(self):
        """Player takes one card."""
        with mock.patch("builtins.input", return_value = "h"):
            self.game.player_deal_cards()
            self.assertGreaterEqual(len(self.game.player.hand.cards[0]), 2)

    def test_deal_split_hand_pass(self):
        """Player does not split hand."""
        with mock.patch("builtins.input", return_value = "p"):
            self.game.player.hand.add_card(1)
            self.game.player.hand.add_card(1)
            self.game.player_split_hand()
            self.assertEqual(len(self.game.player.hand.cards[0]), 2)

    # Dealer tests

    def test_dealer_21(self):
        """The sum of Dealers hand equals to 21 (blackjack)."""
        self.game.dealer.hand.add_card(10)
        self.game.dealer.hand.add_card(1)
        self.game.compare_hands(self.game.player)
        self.assertEqual(self.game.player.cash_balance, 900)

    def test_dealer_busted(self):
        """The sum of Dealers hand is more than 21 (busted!)."""
        self.game.dealer.hand.add_card(10)
        self.game.dealer.hand.add_card(10)
        self.game.dealer.hand.add_card(10)
        self.game.compare_hands(self.game.player)
        self.assertEqual(self.game.player.cash_balance, 1100)

    # Dealer and Player tests

    def test_dealer_at_17_and_player_at_20(self):
        """The sum of Dealers hand is under 21."""
        self.game.dealer.hand.add_card(10)
        self.game.dealer.hand.add_card(7)
        self.game.player.hand.add_card(10)
        self.game.player.hand.add_card(10)
        self.game.compare_hands(self.game.player)
        self.assertEqual(self.game.player.cash_balance, 1100)

    def test_dealer_at_20_and_player_at_17(self):
        """The sum of Dealers hand is under 21."""
        self.game.dealer.hand.add_card(10)
        self.game.dealer.hand.add_card(10)
        self.game.player.hand.add_card(10)
        self.game.player.hand.add_card(7)
        self.game.compare_hands(self.game.player)
        self.assertEqual(self.game.player.cash_balance, 900)

    def test_dealer_at_20_and_player_at_20(self):
        """Dealer and Player got the same points."""
        self.game.dealer.hand.add_card(10)
        self.game.dealer.hand.add_card(10)
        self.game.player.hand.add_card(10)
        self.game.player.hand.add_card(10)
        self.game.compare_hands(self.game.player)
        self.assertEqual(self.game.player.cash_balance, 1000)

    def test_deal_dealer_cards_not_running(self):
        """When game is not running the Dealers hand stays empty."""
        self.game.running = False
        self.game.dealer_deal_cards()
        self.assertEqual(self.game.dealer.hand.cards[0], [])

    def test_deal_dealer_cards_running(self):
        """When game is running the Dealers hand gets 2 or more cards."""
        self.game.running = True
        self.game.dealer_deal_cards()
        self.assertGreaterEqual(len(self.game.dealer.hand.cards[0]), 2)

    def test_deal_dealer_cards_split(self):
        """When game is running and Players hand is split the Dealers hand gets 2 or more cards."""
        self.game.running = True
        self.game.player.hand.hand_split = True
        self.game.dealer_deal_cards()
        self.assertGreaterEqual(len(self.game.dealer.hand.cards[0]), 2)

    # Variables

    def test_start_options_players_turn(self):
        """Change players_turn back to True."""
        with mock.patch("builtins.input", return_value = "d"):
            self.game.players_turn = False
            self.game.start_options()
            self.assertTrue(self.game.players_turn)
