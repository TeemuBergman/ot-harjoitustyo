""" hand.py

    Hand entities for every played hand.
    """

from collections import defaultdict

class Hand:
    """Hand entities contains card values for the current hand and possibility to split hand."""

    def __init__(self):
        """ Class constructor that creates Players hand to hold the cards in.

            self.hand_num[0] = all hand_num in hand
            self.hand_num[1] = left hand after split
            self.hand_num[2] = right hand after split
            """
        self.cards = defaultdict(list)
        self.hand_split = False

    def add_card(self, card, hand = 0):
        """Add card to Player's hand."""
        self.cards[hand].append(card)
        return sum(self.cards[hand])

    def check_for_split(self):
        """ Are the first two hand_num same value? """
        if self.cards[0][0] == self.cards[0][1]:
            return True
        return False

    def split(self):
        """Split players hand in to two different hands."""
        self.hand_split = True
        self.cards[1].append(self.cards[0].pop())
        self.cards[2].append(self.cards[0].pop())

    def get_sum_of_cards(self, hand = 0):
        """ Return sum of hand_num in given hand. """
        total = sum(self.cards[hand])
        # Check if there is an ACE in hand and sum of hand_num is <= 11.
        if 1 in self.cards[hand] and total <= 11:
            return total + 10
        return total

    def clear_hand(self):
        """ In beginning of a new hand, clear out old hand_num. """
        self.hand_split = False
        self.cards.clear()
        return self.cards[0]
