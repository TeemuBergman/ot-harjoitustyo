""" player.py

    This is where dealer and every player in blackjack table get initialized.
    Default cash balance is 1000.
    """

from entities.hand import Hand


class Player:
    """ Functionality for Player object. """

    def __init__(self, name, amount = 1000):
        self.name = name
        self.cash_balance = amount
        self.hand = Hand()

    def cash_add(self, amount):
        """ Add cash to Players stack. """
        self.cash_balance += amount
        return self.cash_balance

    def cash_reduce(self, bet):
        """ Reduce Players stack of cash by the amount of current bet. """
        self.cash_balance -= bet
        return self.cash_balance
