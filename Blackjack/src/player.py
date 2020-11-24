"""This is where dealer and every player in blackjack table get initialized."""

from hand import Hand


class Player:
    """Functionality for Player object."""

    def __init__(self, name, amount):
        self.name = name
        self.cash = amount * 100
        self.hand = Hand()

    def get_cash_balance(self):
        """Check Player cash balance."""
        return self.cash / 100

    def cash_add(self, amount):
        """Add cash to Players stack."""
        self.cash += amount * 100
        return self.get_cash_balance()

    def cash_reduce(self, bet):
        """Reduce Players stack of cash by the amount of current bet."""
        self.cash -= bet * 100
        return self.get_cash_balance()

    def get_player_name(self):
        """Get Player name"""
        return self.name

    def ingame_status(self):
        """Return Player's status as a tuple.
        Tuple contains: Player's name, sum of cards,
        all the cards and cash balance."""
        return [self.get_player_name(), self.hand.get_sum_of_cards(), self.hand.get_all_cards()], \
               ["Cash balance:", self.get_cash_balance(), "€"]
