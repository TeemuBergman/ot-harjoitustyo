import unittest
from player import Player
from shoe import Shoe


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("TestPlayer", 1000)
        self.shoe = Shoe()
        self.card_1 = self.shoe.get_card()
        self.card_2 = self.shoe.get_card()

    def test_player_name(self):
        self.assertEqual(self.player.get_player_name(), "TestPlayer")

    def test_cash_balance(self):
        self.assertEqual(self.player.get_cash_balance(), 1000)

    def test_add_cash(self):
        self.player.add_cash(1000)
        self.assertEqual(self.player.get_cash_balance(), 2000)

    def test_add_and_get_first_card(self):
        self.player.add_card(self.card_1)
        self.player.add_card(self.card_2)
        self.assertEqual(self.player.get_first_card(), self.card_1)

    def test_add_and_get_cards(self):
        self.player.add_card(self.card_1)
        self.player.add_card(self.card_2)
        self.assertEqual(self.player.get_cards(), [self.card_1, self.card_2])

    def test_get_sum_of_cards(self):
        self.player.add_card(self.card_1)
        self.player.add_card(self.card_2)
        sum_of_cards = self.card_1 + self.card_2
        self.assertEqual(self.player.get_sum_of_cards(), sum_of_cards)

    def test_clear_hand(self):
        self.player.add_card(self.card_1)
        self.player.add_card(self.card_2)
        self.player.clear_hand()
        self.assertEqual(self.player.get_cards(), [])

    def test_ingame_status(self):
        self.player.add_card(self.card_1)
        self.player.add_card(self.card_2)
        sum_of_cards = self.card_1 + self.card_2
        self.assertEqual(self.player.ingame_status()[0], f"TestPlayer's hand: {sum_of_cards} {[self.card_1, self.card_2]}")
        self.assertEqual(self.player.ingame_status()[1], f"Cash balance: 1000.0 €")
