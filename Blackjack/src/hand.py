"""Hand class for every played hand."""


class Hand:
    """Hand class contains values for current hands and possibility to split hand."""

    def __init__(self):
        """Initialize two hands for Player."""
        self.hand = []
        self.hand_splitted = False
        self.hand_left = []
        self.hand_right = []

    def add_card(self, card, hand = None):
        """Add card to Player's hand."""
        if self.hand_splitted:
            if hand == "left":
                self.hand_left.append(card)
                return sum(self.hand_left)
            if hand == "right":
                self.hand_right.append(card)
                return sum(self.hand_right)
        self.hand.append(card)
        return sum(self.hand)

    def split_available(self):
        """Are the first two cards same value?"""
        if self.hand[0] == self.hand[1]:
            return True
        return False

    def split_hand(self):
        """If Player gets first two cards of the same value,
        it can be split to two different hands."""
        self.hand_splitted = True
        self.hand_left.append(self.hand[0])
        self.hand_right.append(self.hand[1])
        return self.hand_left[0], self.hand_right[0]

    def get_all_cards(self):
        """Return every card in Player's hand."""
        return self.hand

    def get_sum_of_cards(self):
        """Return sum of every card in Player's hand."""
        return sum(self.hand)

    def clear_hand(self):
        """In beginning of a new hand, clear out old cards."""
        self.hand_splitted = False
        self.hand.clear()
        self.hand_left.clear()
        self.hand_right.clear()
        return self.hand, self.hand_left, self.hand_right
