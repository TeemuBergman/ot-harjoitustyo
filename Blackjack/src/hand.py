"""Hand class for every played hand."""


class Hand:
    """Hand class contains values for current hands and possibility to split hand."""

    def __init__(self):
        """Initialize two hands for Player."""
        self.hand_1 = []
        self.hand_2 = []

    def add_card(self, card):
        """Add card to Player's hand."""
        self.hand_1.append(card)

    def get_first_card(self):
        """Returng first card in Player's hand."""
        return self.hand_1[0]

    def get_cards(self):
        """Return every card in Player's hand."""
        return self.hand_1

    def get_sum_of_cards(self):
        """Return sum of every card in Player's hand."""
        return sum(self.hand_1)

    def clear_hand(self):
        """In beginning of a new hand, clear out old cards."""
        self.hand_1.clear()
