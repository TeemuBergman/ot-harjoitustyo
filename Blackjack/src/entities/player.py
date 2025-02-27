from entities.hand import Hand


class Player:
    """ This is where dealer and every player in blackjack table get initialized.
        Default cash balance is 1000.

        Attributes:
            name: Player name
            amount: Cash amount. Default is 1000.
        """

    def __init__(self, name, amount = 1000):
        self.name = name
        self.cash_balance = amount
        self.hand = Hand()

    def cash_add(self, amount):
        """Add cash to Players stack. """
        self.cash_balance += amount
        return self.cash_balance

    def cash_reduce(self, bet):
        """Reduce Players stack of cash by the amount of current bet. """
        self.cash_balance -= bet
        return self.cash_balance

    def save_game(self):
        """Return Player data as tuple."""
        return self.name, self.cash_balance

    def load_game(self, data):
        """Load saved game data as a tuple and replace current data."""
        self.name = data[0]
        self.cash_balance = int(data[1])
