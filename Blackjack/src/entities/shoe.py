""" shoe.py

    In Blackjack shoe is a combination of 6 card decks of 52 cards, total of 312 cards.
    Point where shoe will be resuffled is marked by the cut card.
    """

import random
from ui.ui_cli import Ui


class Shoe:
    """ Shoe and its functionality."""

    def __init__(self):
        self.ui_cli = Ui()
        self.shoe = []
        self.card = -1
        self.cut_card = 0
        self.create_shoe()

    def create_shoe(self):
        """Create a Shoe and place a "cut card" between cards 237-252."""
        self.shoe.clear()
        for _ in range(6):
            for _ in range(4):
                for card in range(13):
                    self.shoe.append(card + 1)
        random.shuffle(self.shoe)
        self.cut_card = random.randrange(60, 75)

    def get_card(self):
        """Get one card from Shoe."""
        if len(self.shoe) == self.cut_card:
            self.ui_cli.shuffling_deck()
            self.create_shoe()
        self.card = self.shoe.pop()
        if self.card > 10:
            self.card = 10
        return self.card
