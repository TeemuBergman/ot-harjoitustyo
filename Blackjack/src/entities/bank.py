""" bank.py

    This class contains all of the money handling methods.
    """


class Bank:
    """
        Kirjoita!
    """

    def __init__(self):
        self.current_bet = 100
        self.max_bet = 500
        self.min_bet = 100

    def bet_raise(self):
        """Raises bet by 100. Max = max_bet."""
        if self.current_bet < self.max_bet:
            self.current_bet += 100
        self.bet_cap()

    def bet_reduce(self):
        """Reduces bet by 100. Min = min_bet."""
        if self.current_bet >= self.min_bet:
            self.current_bet -= 100
        self.bet_cap()

    def bet_cap(self, player = None):
        """Checks and caps the current_bet to max_bet or min_bet."""
        if self.current_bet > self.max_bet:
            self.current_bet = self.max_bet
        if self.current_bet < self.min_bet:
            self.current_bet = self.min_bet
        if player and self.current_bet > player.cash_balance:
            self.current_bet = player.cash_balance
