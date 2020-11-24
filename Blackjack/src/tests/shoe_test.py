"""Here are all the tests for Shoe class."""

from unittest import TestCase
from shoe import Shoe


class TestShoe(TestCase):
    """TestShoe class for all Shoe class tests."""

    def setUp(self):
        """Init for Shoe class tests"""
        self.shoe = Shoe()

    def test_create_shoe(self):
        """Check that the shoe size is 312 cards after initialization."""
        self.assertEqual(self.shoe.get_size(), 312)

    def test_get_card(self):
        """Does shoe return a correct card."""
        self.shoe.shoe.clear()
        self.shoe.shoe.append(1)
        print("SHOE SIZE:", self.shoe.get_size)
        self.assertEqual(self.shoe.get_card(), 1)
