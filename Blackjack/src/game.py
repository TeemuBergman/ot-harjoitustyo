"""Blackjack games logic."""

import sys
from player import Player
from shoe import Shoe


class Game:
    """Blackjack games main Game class. This contains all logic for house dealer and player."""

    def __init__(self):
        """Init Game"""
        self.shoe = Shoe()
        self.dealer = Player("Dealer", 1000000)
        self.player = Player("Player", 1000)
        self.bet = 100
        self.game_status = True

    def main_game(self):
        """Main loop of the game."""
        while True:
            print("P R O -----------")
            print("B L A C K J A C K")
            print("--------- 2 0 2 0")
            print(self.player.ingame_status()[1], "\n")
            self.clear_table()
            self.set_player_cards()
            if self.game_status:
                self.set_dealer_cards()

    def clear_table(self):
        """Clear table before start of a new hand."""
        self.game_status = True
        # Clear Dealers and Players hand.
        self.player.hand.clear_hand()
        # Deal one card to Dealer.
        self.dealer.hand.clear_hand()
        self.deal_to_dealer()

    def bet_size(self):
        """Returns current bet size."""
        return self.bet

    def bet_raise(self):
        """Raises bet by 100."""
        self.bet += 100

    def bet_reduce(self):
        """Reduces bet by 100."""
        self.bet -= 100

    def set_player_cards(self):
        """Loop for dealing Players cards and giving options during one hand."""
        # Deal first two cards.
        for _ in range(2):
            self.deal_to_player()
        # Check if the first two cards are same value.
        self.player.hand.split_available()
        # Player makes a decision.
        while self.check_player_status():
            print(self.player.ingame_status()[0])
            ans = input("(D)eal, (S)tay or (Q)uit: ").upper()
            if ans == "D":
                self.deal_to_player()
            elif ans == "S":
                return False
            elif ans == "Q":
                sys.exit()

    def deal_to_player(self):
        """Deal one card to player and check if it's an ACE."""
        card = self.shoe.get_card()
        if card == 1:
            card = self.ace()
        self.player.hand.add_card(card)

    def check_player_status(self):
        """Check the status of player during one hand."""
        cards_sum = self.player.hand.get_sum_of_cards()
        if self.player.get_cash_balance() < self.bet:
            print("OUT OF CASH!")
            self.game_status = False
            return False
        if cards_sum > 21:
            self.player.cash_reduce(self.bet)
            self.game_status = False
            print("YOU BUSTED!\n", self.player.ingame_status(), "\n")
            return False
        if cards_sum == 21:
            self.player.cash_add(self.bet * 1.5)
            self.game_status = False
            print("\n", "YOU GOT BLACKJACK!\n", self.player.ingame_status(), "\n")
            return False
        return True

    def set_dealer_cards(self):
        """Set cards to dealer while checking dealers hand status."""
        while self.check_dealer_status():
            self.deal_to_dealer()

    def check_dealer_status(self):
        """Check the status of dealers hand."""
        player_sum = self.player.hand.get_sum_of_cards()
        dealer_sum = self.dealer.hand.get_sum_of_cards()
        if dealer_sum > 21:
            self.player.cash_add(self.bet)
            print("DEALER BUSTED!", self.dealer.ingame_status()[0], "\n")
            return False
        if dealer_sum == 21:
            self.player.cash_reduce(self.bet)
            print("DEALER GOT BLACKJACK!", self.dealer.ingame_status()[0], "\n")
            return False
        if dealer_sum >= 17 and dealer_sum == player_sum:
            print("ITS A TIE!", self.dealer.ingame_status()[0], "\n")
            return False
        if dealer_sum >= 17 >= dealer_sum > player_sum:
            self.player.cash_reduce(self.bet)
            print("DEALER WON!", self.dealer.ingame_status()[0], "\n")
            return False
        if 17 <= dealer_sum < player_sum:
            self.player.cash_add(self.bet)
            print("PLAYER WON!", self.dealer.ingame_status()[0], "\n")
            return False
        return True

    def deal_to_dealer(self):
        """Deal cards to dealer and check if dealer got an ACE."""
        card = self.shoe.get_card()
        if card == 1 and self.dealer.hand.get_sum_of_cards() <= 10:
            card = 11
        self.dealer.hand.add_card(card)
        print(self.dealer.ingame_status()[0])

    def ace(self):
        """Give player an option to choose if they got an ACE"""
        print(self.player.ingame_status())
        selection = input("You got an ACE, select 1 or 11?")
        if selection == "11":
            return 11
        return 1

    def get_cash_stats(self):
        """Print players cash balance and current bet."""
        print("BANK:", self.player.get_cash_balance() - self.bet, "€ CURRENT BET:", self.bet, "€")
