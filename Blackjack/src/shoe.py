""""In Blackjack shoe is a combination of 6 card decks of 52 cards, total of 312 cards."""

import random


class Shoe:
    """Shoe class and its functionality."""

    def __init__(self):
        self.shoe = []
        self.create_shoe()

    def create_shoe(self):
        """This is where Shoe is created."""
        for _ in range(6):
            for _ in range(4):
                for card in range(13):
                    self.shoe.append(card + 1)
        random.shuffle(self.shoe)

    def get_card(self):
        """Get one card from Shoe."""
        if len(self.shoe) == 0:
            print("SHUFFLING DECK")
            self.create_shoe()
        card = self.shoe.pop()
        if card > 10:
            card = 10
        return card

    def get_size(self):
        """Return how many cards left in Shoe."""
        return len(self.shoe)
