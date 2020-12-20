"""shoe_test.py

    Here are all the tests for Shoe class.
    """

from unittest import TestCase
from entities.shoe import Shoe


class TestShoe(TestCase):
    """TestShoe entities for all Shoe entities tests."""

    def setUp(self):
        """Init for Shoe entities tests"""
        self.shoe = Shoe()

    def test_create_shoe(self):
        """Check that the shoe size is 312 hand_num after initialization."""
        self.assertEqual(len(self.shoe.shoe), 312)

    def test_get_card(self):
        """Does shoe return a correct card."""
        self.shoe.shoe.clear()
        self.shoe.shoe.append(1)
        self.assertEqual(self.shoe.get_card(), 1)

    def test_get_high_card(self):
        """Does shoe return a correct card if its value is greater than 10."""
        self.shoe.shoe.clear()
        self.shoe.shoe.append(13)
        self.assertEqual(self.shoe.get_card(), 10)

    def test_cut_card(self):
        """Does shoe get rebuilt after cutcard position is met."""
        self.shoe.shoe.clear()
        for i in range(10):
            self.shoe.shoe.append(i)
        self.shoe.cut_card = 2
        for j in range(10):
            self.shoe.get_card()
        self.assertEqual(len(self.shoe.shoe), 310)