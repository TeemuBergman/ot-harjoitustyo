class Player:
    def __init__(self, name, amount):
        self.name = name
        self.cash = amount * 100
        self.cards = []

    def get_cash_balance(self):
        return self.cash / 100

    def get_player_name(self):
        return self.name

    def add_cash(self, amount):
        self.cash += amount * 100
        return self.get_cash_balance()

    def add_card(self, card):
        self.cards.append(card)

    def get_first_card(self):
        return self.cards[0]

    def get_cards(self):
        return self.cards

    def get_sum_of_cards(self):
        return sum(self.cards)

    def clear_hand(self):
        self.cards.clear()

    def ingame_status(self):
        return f"{self.get_player_name()}'s hand: {self.get_sum_of_cards()} {self.get_cards()}", f"Cash balance: {self.get_cash_balance()} €"
