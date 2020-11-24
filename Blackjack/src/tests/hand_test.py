"""Here are all the tests for Hand class."""

from unittest import TestCase
from hand import Hand
from player import Player
from shoe import Shoe


class TestHand(TestCase):
    """TestShoe class for all Shoe class tests."""

    def setUp(self):
        """Init for Player class tests"""
        self.player = Player("TestPlayer", 1000)
        self.card_1 = 7
        self.card_2 = 4
        self.card_3 = 10

    def test_add_and_get_first_card(self):
        """Add two cards to Player's hand and check that the first card is correct."""
        self.player.hand.add_card(self.card_1)
        self.player.hand.add_card(self.card_2)
        self.assertEqual(self.player.hand.get_first_card(), self.card_1)

    def test_add_and_get_cards(self):
        """"Add two cards to Player's hand and check that both of them are correct."""
        self.player.hand.add_card(self.card_1)
        self.player.hand.add_card(self.card_2)
        self.assertEqual(self.player.hand.get_cards(), [self.card_1, self.card_2])

    def test_get_sum_of_cards(self):
        """Add two cards to Players hand check that the sum of them is correct."""
        self.player.hand.add_card(self.card_1)
        self.player.hand.add_card(self.card_2)
        sum_of_cards = self.card_1 + self.card_2
        self.assertEqual(self.player.hand.get_sum_of_cards(), sum_of_cards)

    def test_clear_hand(self):
        """Add two cards to players hand, clear the hand and check that hand is empty."""
        self.player.hand.add_card(self.card_1)
        self.player.hand.add_card(self.card_2)
        self.player.hand.clear_hand()
        self.assertEqual(self.player.hand.get_cards(), [])