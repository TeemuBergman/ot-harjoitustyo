""" shoe.py

    In Blackjack shoe is a combination of 6 card decks of 52 cards, total of 312 cards.
    Point where shoe will be resuffled is marked by the cut card.
    """

import random
from ui.cli_ui import Ui


class Shoe:
    """Shoe entities and its functionality."""

    def __init__(self):
        self.ui = Ui()
        self.shoe = []
        self.cut_card = 0
        self.__create_shoe()

    def __create_shoe(self):
        """Create a Shoe and place a "cut card" between cards 237-252."""
        for _ in range(6):
            for _ in range(4):
                for card in range(13):
                    self.shoe.append(card + 1)
        random.shuffle(self.shoe)
        self.cut_card = random.randrange(60, 75)

    def get_card(self):
        """Get one card from Shoe."""
        if len(self.shoe) == self.cut_card:
            self.ui.shuffling_deck()
            self.__create_shoe()
        card = self.shoe.pop()
        if card > 10:
            card = 10
        return card

    def get_size(self):
        """Return how many cards are left in Shoe."""
        return len(self.shoe)
