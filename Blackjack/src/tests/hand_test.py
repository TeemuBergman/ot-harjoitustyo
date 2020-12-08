"""hand_test.py

    Here are all the tests for Hand entities.
    """

from unittest import TestCase
from entities.player import Player


class TestHand(TestCase):
    """TestShoe entities for all Shoe entities tests."""

    def setUp(self):
        """Init for Player entities tests"""
        self.player = Player("TestPlayer", 1000)
        self.card_1 = 7
        self.card_2 = 4
        self.card_3 = 10

    def test_add_and_get_cards(self):
        """"Add two cards to Player's hand and check that both of them are correct."""
        self.player.hand.add_card(self.card_1)
        self.player.hand.add_card(self.card_2)
        self.assertEqual(self.player.hand.get_all_cards(), [self.card_1, self.card_2])

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
        self.assertEqual(self.player.hand.clear_hand(), ([], [], []))

    def test_split_hand_singles(self):
        """Split hand in two and check that left and right splits are the same value."""
        self.player.hand.add_card(self.card_1)
        self.player.hand.add_card(self.card_1)
        self.assertEqual(self.player.hand.split_hand(), (7, 7))

    def test_split_hand_left(self):
        """Add value of 41 to left hand and get 31 as result."""
        self.player.hand.add_card(self.card_1)
        self.player.hand.add_card(self.card_1)
        self.player.hand.split_hand()
        self.player.hand.add_card(self.card_2, "left")
        self.player.hand.add_card(self.card_3, "left")
        self.assertEqual(self.player.hand.add_card(self.card_3, "left"), 31)

    def test_split_hand_right(self):
        """Add value of 41 to right hand and get 31 as result."""
        self.player.hand.add_card(self.card_1)
        self.player.hand.add_card(self.card_1)
        self.player.hand.split_hand()
        self.player.hand.add_card(self.card_2, "right")
        self.player.hand.add_card(self.card_3, "right")
        self.assertEqual(self.player.hand.add_card(self.card_3, "right"), 31)
