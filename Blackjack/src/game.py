from player import Player
from shoe import Shoe


class Game:
    def __init__(self):
        self.shoe = Shoe()
        self.dealer = Player("Dealer", 1000000)
        self.player = Player("Player", 1000)
        self.bet = 100
        self.game_over = False

    def main_game(self):
        while True:
            print("P R O -----------")
            print("B L A C K J A C K")
            print("--------- 2 0 2 0")
            print(self.player.ingame_status()[1], "\n")
            self.game_over = False
            self.check_player_status()
            self.set_dealer_first_card()
            self.set_player_cards()
            if not self.game_over:
                self.set_dealer_cards()

    def set_player_cards(self):
        self.player.clear_hand()
        for i in range(2):
            self.deal_to_player()
        while self.check_player_status():
            print(self.player.ingame_status()[0])
            ans = input("(D)eal, (S)tay or (Q)uit: ").upper()
            if ans == "D":
                self.deal_to_player()
            elif ans == "S":
                return False
            elif ans == "Q":
                exit()

    def deal_to_player(self):
        card = self.shoe.get_card()
        if card == 1:
            card = self.ace()
        self.player.add_card(card)

    def check_player_status(self):
        cards_sum = self.player.get_sum_of_cards()
        if self.player.get_cash_balance() < self.bet:
            print("OUT OF MONEY!")
            self.game_over = True
            return
        if cards_sum > 21:
            self.player.add_cash(-self.bet)
            self.game_over = True
            print(f"\nYOU BUSTED!\n{self.player.ingame_status()}\n")
            return False
        elif cards_sum == 21:
            self.player.add_cash(self.bet * 1.5)
            self.game_over = True
            print(f"\nYOU GOT BLACKJACK!\n{self.player.ingame_status()}\n")
            return False
        else:
            return True

    def set_dealer_first_card(self):
        self.dealer.clear_hand()
        self.deal_to_dealer()
        print(self.dealer.ingame_status()[0])

    def set_dealer_cards(self):
        while self.check_dealer_status():
            self.deal_to_dealer()

    def check_dealer_status(self):
        player_sum = self.player.get_sum_of_cards()
        dealer_sum = self.dealer.get_sum_of_cards()
        if dealer_sum > 21:
            self.player.add_cash(self.bet)
            print("DEALER BUSTED!", self.dealer.ingame_status()[0], "\n")
            return False
        elif dealer_sum == 21:
            self.player.add_cash(-self.bet)
            print("DEALER GOT BLACKJACK!", self.dealer.ingame_status()[0], "\n")
            return False
        elif dealer_sum >= 17 and dealer_sum == player_sum:
            print("ITS A TIE!", self.dealer.ingame_status()[0], "\n")
            return False
        elif dealer_sum >= 17 >= dealer_sum > player_sum:
            self.player.add_cash(-self.bet)
            print("DEALER WON!", self.dealer.ingame_status()[0], "\n")
            return False
        elif 17 <= dealer_sum < player_sum:
            self.player.add_cash(self.bet)
            print("PLAYER WON!", self.dealer.ingame_status()[0], "\n")
            return False
        else:
            return True

    def deal_to_dealer(self):
        card = self.shoe.get_card()
        if card == 1 and self.dealer.get_sum_of_cards() <= 10:
            card = 11
        self.dealer.add_card(card)

    def ace(self):
        print(self.player.ingame_status())
        selection = input("You got an ACE, select 1 or 11?")
        if selection == "1":
            return 1
        else:
            return 11

    def get_cash_stats(self):
        print("BANK:", self.player.get_cash_balance() - self.bet, "€ CURRENT BET:", self.bet, "€")
