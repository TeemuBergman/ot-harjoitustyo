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
        self.bet = 100.0
        self.game_over = False

    def main_game(self):
        """Main loop of the game."""
        while True:
            print("P R O -----------")
            print("B L A C K J A C K")
            print("--------- 2 0 2 0")
            self.start_options()
            self.deal_first_cards()
            self.deal_player_cards()
            self.deal_dealer_cards()

    def start_options(self):
        """Give Player some options before next hand."""
        # Reset game status
        self.game_over = False
        # Options menu
        while True:
            if self.player.get_cash_balance() >= 100:
                # Cap bet size to player cash balance
                if self.bet > self.player.get_cash_balance():
                    self.bet = self.player.get_cash_balance()
                # Player options
                print("Cash balance:", self.player.get_cash_balance(),
                      "€ Current bet:", self.get_bet())
                ans = input("(d)eal new hand or modify bet: (+)100, (-)100. (q)uit: ").lower()
                if ans == "d":
                    break
                elif ans == "+":
                    self.bet_raise()
                elif ans == "-":
                    self.bet_reduce()
                elif ans == "q":
                    sys.exit()
            else:
                print("GAME OVER")
                sys.exit()

    def get_bet(self):
        """Returns current bet size."""
        return self.bet

    def bet_raise(self):
        """Raises bet by 100. Max = 500"""
        if self.get_bet() < 500:
            self.bet += 100

    def bet_reduce(self):
        """Reduces bet by 100. Min = 100"""
        if self.get_bet() >= 200:
            self.bet -= 100

    def deal_first_cards(self):
        """Reset table for a new hand and deal first two cards to Dealer and Player."""
        # Clear Dealers and Players hand.
        self.player.hand.clear_hand()
        self.dealer.hand.clear_hand()
        # Deal two cards to Dealer and Player
        for _ in range(2):
            self.dealer.hand.add_card(self.shoe.get_card())
            self.player.hand.add_card(self.shoe.get_card())
        # Check for blackjack
        if self.player.hand.check_for_blackjack() and not self.dealer.hand.check_for_blackjack():
            # Player got blackjack
            self.get_player_status()
        if self.dealer.hand.check_for_blackjack() and not self.player.hand.check_for_blackjack():
            # Dealer got blackjack
            self.get_dealer_status()
        if self.player.hand.check_for_blackjack() and self.dealer.hand.check_for_blackjack():
            # Both got blackjack
            self.get_dealer_status()
        # Check if Players first two cards are the same value.
        if self.player.hand.split_available():
            # self.player.hand.split_hand()
            pass

    def deal_player_cards(self):
        """Deal players cards and give options."""
        # Players main loop
        while not self.game_over and not self.player.busted():
            print("Player's hand:", self.player.hand.get_sum_of_cards(), self.player.hand.get_all_cards())
            ans = input("(d)eal, (s)tay or (q)uit: ").lower()
            if ans == "d":
                self.player.hand.add_card(self.shoe.get_card())
                self.get_player_status()
            elif ans == "s":
                return False
            elif ans == "q":
                sys.exit()

    def get_player_status(self):
        """Check the get_info of player during one hand."""
        cards_sum = self.player.hand.get_sum_of_cards()
        if cards_sum > 21:
            self.player.cash_reduce(self.bet)
            self.game_over = True
            self.print_status("PLAYER BUSTED!", self.player)
            return False
        if cards_sum == 21:
            self.game_over = True
            self.player.cash_add(self.bet * 1.5)
            self.print_status("PLAYER GOT 21!", self.player)
            return False
        return True

    def deal_dealer_cards(self):
        """Set cards to dealer while checking dealers hand get_info."""
        while not self.game_over and not self.player.busted():
            self.get_dealer_status()
            print("Dealer's hand:", self.dealer.hand.get_sum_of_cards(), "pts", self.dealer.hand.get_all_cards())
            self.dealer.hand.add_card(self.shoe.get_card())

    def get_dealer_status(self):
        """Check the get_info of dealers hand."""
        player_sum = self.player.hand.get_sum_of_cards()
        dealer_sum = self.dealer.hand.get_sum_of_cards()
        if dealer_sum > 21:
            self.game_over = True
            self.player.cash_add(self.bet)
            self.print_status("DEALER BUSTED!", self.dealer)
            return False
        if dealer_sum == 21:
            self.game_over = True
            self.player.cash_reduce(self.bet)
            self.print_status("DEALER GOT 21!", self.dealer)
            return False
        if dealer_sum >= 17:
            if dealer_sum == player_sum:
                self.print_status("IT'S A TIE!", self.player)
            if dealer_sum > player_sum:
                self.player.cash_reduce(self.bet)
                self.print_status("DEALER WON!", self.dealer)
            if dealer_sum < player_sum:
                self.player.cash_add(self.bet)
                self.print_status("PLAYER WON!", self.player)
            self.game_over = True
            return False
        return True

    def print_status(self, message, player):
        """Print Player status."""
        print("\n" + message, player.get_name() + "'s hand:", player.hand.get_sum_of_cards(), "pts", player.hand.get_all_cards(), "\n")
