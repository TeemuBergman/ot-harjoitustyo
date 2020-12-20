"""hand_test.py

    Here are all the tests for Hand class.
    """

from unittest import TestCase
from entities.player import Player


class TestHand(TestCase):
    """Test Hand classes different functionalitites."""

    def setUp(self):
        """Init for Player entities tests"""
        self.player = Player("TestPlayer")
        self.card1 = 7
        self.card2 = 4
        self.card3 = 10
        self.card4 = 1

    def test_add_and_get_cards(self):
        """"Add two hand_num to Player's hand and check that both of them are correct."""
        self.player.hand.add_card(self.card1)
        self.player.hand.add_card(self.card2)
        self.assertEqual(self.player.hand.cards[0], [self.card1, self.card2])

    def test_get_sum_of_cards(self):
        """Add two hand_num to Players hand check that the sum of them is correct."""
        self.player.hand.add_card(self.card1)
        self.player.hand.add_card(self.card2)
        sum_of_cards = self.card1 + self.card2
        self.assertEqual(self.player.hand.get_sum_of_cards(), sum_of_cards)

    def test_ace(self):
        """If hand contains an ace and sum of cards is less or equal than 11, return sum of cards + 10."""
        self.player.hand.add_card(self.card3)
        self.player.hand.add_card(self.card4)
        self.assertEqual(self.player.hand.get_sum_of_cards(), 21)

    def test_clear_hand(self):
        """Add two hand_num to players hand, clear the hand and check that hand is empty."""
        self.player.hand.add_card(self.card1)
        self.player.hand.add_card(self.card2)
        self.assertEqual(self.player.hand.clear_hand(), [])

    def test_split_true(self):
        """There is a possibility of hand split"""
        self.player.hand.add_card(self.card1)
        self.player.hand.add_card(self.card1)
        self.assertEqual(self.player.hand.check_for_split(), True)

    def test_split_false(self):
        """There is a possibility of hand split"""
        self.player.hand.add_card(self.card1)
        self.player.hand.add_card(self.card2)
        self.assertEqual(self.player.hand.check_for_split(), False)

    def test_split_hand_singles(self):
        """Split hand in two and check that left and right splits are the same value."""
        self.player.hand.add_card(self.card1)
        self.player.hand.add_card(self.card1)
        self.player.hand.split()
        self.assertEqual((self.player.hand.cards[1][0], self.player.hand.cards[2][0]), (7, 7))

    def test_split_hand_left(self):
        """Add value of 41 to left hand and get 31 as result."""
        self.player.hand.add_card(self.card1)
        self.player.hand.add_card(self.card1)
        self.player.hand.split()
        self.player.hand.add_card(self.card2, 1)
        self.player.hand.add_card(self.card3, 1)
        self.assertEqual(self.player.hand.add_card(self.card3, 1), 31)

    def test_split_hand_right(self):
        """Add value of 41 to right hand and get 31 as result."""
        self.player.hand.add_card(self.card1)
        self.player.hand.add_card(self.card1)
        self.player.hand.split()
        self.player.hand.add_card(self.card2, 2)
        self.player.hand.add_card(self.card3, 2)
        self.assertEqual(self.player.hand.add_card(self.card3, 2), 31)
