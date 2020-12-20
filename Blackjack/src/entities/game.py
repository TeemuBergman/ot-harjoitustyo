""" game.py

    Blackjack game logic.
    """

import sys
from entities.player import Player
from entities.shoe import Shoe
from entities.bank import Bank
from ui.ui_cli import Ui


class Game:
    """Blackjack games main Game entities. This contains all logic for house dealer and player."""

    def __init__(self):
        self.ui_cli = Ui()
        self.bank = Bank()
        self.shoe = Shoe()
        self.dealer = Player("Dealer")
        self.player = Player("Player")
        self.players_turn = True
        self.running = True

    def main_game(self):
        """Main loop of the game."""
        self.ui_cli.title()
        while True:
            self.start_options()
            self.deal_first_cards()
            if self.running and self.players_turn:
                self.player_deal_cards()
            if self.running:
                self.dealer_deal_cards()
            self.ui_cli.play_again()

    def start_options(self):
        """Give Player some options before next hand."""
        # Reset status
        self.players_turn = True
        self.running = True
        # Options menu
        while True:
            if self.player.cash_balance >= self.bank.min_bet:
                # Check and cap bet size
                self.bank.bet_cap(self.player)
                # Player options
                self.ui_cli.player_cash_balance(self.player, self.bank.current_bet)
                ans = self.ui_cli.player_selection_start()
                if ans == "d":
                    break
                if ans == "+":
                    self.bank.bet_raise()
                if ans == "-":
                    self.bank.bet_reduce()
                if ans == "q":
                    sys.exit()
            else:
                self.ui_cli.game_over()
                sys.exit()

    def deal_first_cards(self):
        """Reset table for a new hand and deal first two hand_num to Dealer and Player."""
        # Clear Dealers and Players previous hands.
        self.player.hand.clear_hand()
        self.dealer.hand.clear_hand()
        # Deal two cards to Player and Dealer.
        self.ui_cli.new_hand()
        for _ in range(2):
            self.player.hand.add_card(self.shoe.get_card())
            self.dealer.hand.add_card(self.shoe.get_card())
        self.ui_cli.dealer_top_card(self.dealer)
        # Check for player blackjack
        if self.check_for_blackjack(self.player):
            self.running = False
            self.player.cash_add(self.bank.current_bet * 1.5)
            self.ui_cli.player_blackjack(self.player, self.bank.current_bet)
            return
        # Check if Players first two hand_num are the same value.
        if self.player.hand.check_for_split():
            if self.player.cash_balance >= (self.bank.current_bet * 2):
                self.player_split_hand()
            else:
                self.ui_cli.player_no_cash_for_split(self.player, self.bank.current_bet)

    def player_split_hand(self):
        """Split Players hand."""
        ans = self.ui_cli.player_split_hand(self.player, self.bank.current_bet)
        if ans == "s":
            self.player.hand.split()
            self.player.hand.add_card(self.shoe.get_card(), 1)
            self.player.hand.add_card(self.shoe.get_card(), 2)
            self.ui_cli.player_selection_split_hand(self.player)
            # Go through new hands
            for i in range(1, 3):
                while True:
                    if self.check_for_bust(self.player, i) or self.check_for_21(self.player, i):
                        break
                    ans = self.ui_cli.player_selection_hand(i)
                    if ans == "h":
                        self.player.hand.add_card(self.shoe.get_card(), i)
                        self.ui_cli.player_selection_split_hand(self.player)
                    if ans == "p":
                        break
            self.players_turn = False
        elif ans == "p":
            return

    def player_deal_cards(self):
        """Deal players hand_num and give options."""
        while self.players_turn and not self.check_for_bust(self.player):
            self.ui_cli.player_status_hand(self.player)
            ans = self.ui_cli.player_selection_hand()
            if ans == "h":
                self.player.hand.add_card(self.shoe.get_card())
                self.player_check_status()
            if ans == "p":
                self.players_turn = False
                return

    def player_check_status(self, hand_num = 0):
        """Check the get_info of player during one hand."""
        if self.check_for_bust(self.player, hand_num):
            self.players_turn = False
            self.running = False
            self.player.cash_reduce(self.bank.current_bet)
            self.ui_cli.player_busted(self.player, self.bank.current_bet, hand_num)
        if self.check_for_21(self.player, hand_num):
            self.players_turn = False
            self.running = False
            self.player.cash_add(self.bank.current_bet)
            self.ui_cli.player_got_21(self.player, self.bank.current_bet)

    def dealer_deal_cards(self):
        """Set cards to Dealers hand while.
        Check Dealers hand and if its >=17 then compare it to Players hand."""
        while self.running and not self.check_for_bust(self.player):
            if self.dealer.hand.get_sum_of_cards() >= 17:
                self.running = False
                self.ui_cli.showdown()
                if self.player.hand.hand_split:
                    for i in range(1, 3):
                        self.compare_hands(self.player, i)
                else:
                    self.compare_hands(self.player)
            else:
                self.dealer.hand.add_card(self.shoe.get_card())
        self.ui_cli.dealer_status(self.dealer)

    def compare_hands(self, player, hand_num = 0):
        """Compare hands between Dealer and Player."""
        dealer_sum = self.dealer.hand.get_sum_of_cards()
        player_sum = player.hand.get_sum_of_cards(hand_num)
        if self.check_for_bust(player, hand_num):
            player.cash_reduce(self.bank.current_bet)
            self.ui_cli.player_busted(player, self.bank.current_bet, hand_num)
        elif self.check_for_21(player, hand_num):
            player.cash_add(self.bank.current_bet)
            self.ui_cli.player_got_21(player, self.bank.current_bet, hand_num)
        elif self.check_for_21(self.dealer):
            player.cash_reduce(self.bank.current_bet)
            self.ui_cli.dealer_21(self.dealer)
        elif self.check_for_bust(self.dealer):
            player.cash_add(self.bank.current_bet)
            self.ui_cli.player_won(player, self.bank.current_bet, hand_num)
        elif dealer_sum == player_sum:
            self.ui_cli.player_tie(player, self.bank.current_bet, hand_num)
        elif dealer_sum > player_sum:
            player.cash_reduce(self.bank.current_bet)
            self.ui_cli.player_lost(player, self.bank.current_bet, hand_num)
        else:
            player.cash_add(self.bank.current_bet)
            self.ui_cli.player_won(player, self.bank.current_bet, hand_num)

    def check_for_blackjack(self, player):
        """Check if Player has a blackjack."""
        if 1 in player.hand.cards[0] and 10 in player.hand.cards[0]:
            return True
        return False

    def check_for_21(self, player, cards = 0):
        """Check if a Player has 21 points."""
        if player.hand.get_sum_of_cards(cards) == 21:
            return True
        return False

    def check_for_bust(self, player, cards = 0):
        """Check if a Player has gone over 21 points."""
        if player.hand.get_sum_of_cards(cards) > 21:
            return True
        return False
