"""cli_ui.py

    UI for the command line interface.
    """


class Ui:
    def __init__(self):
        pass

    def title(self):
        print("P R O -----------")
        print("B L A C K J A C K")
        print("--------- 2 0 2 0")

    def dealer_status(self, dealer):
        print("Dealer's hand:", dealer.hand.get_sum_of_cards(),
              "pts", dealer.hand.get_all_cards())

    def shuffling_deck(self):
        print("SHUFFLING DECK")

    def player_select(self):
        return input("(d)eal a new hand or modify bet: (+)100, (-)100. (q)uit: ").lower()

    def player_select_during_hand(self):
        return input("(d)eal, (s)tay or (q)uit: ").lower()

    def player_status(self, player, bet):
        print("Cash balance:", player.get_cash_balance(),
              "€ Current bet:", bet)

    def player_status_during_hand(self, player):
        print("Player's hand:",
              player.hand.get_sum_of_cards(),
              player.hand.get_all_cards())

    def player_status_end_game(self, player):
        return str(player.hand.get_sum_of_cards()) + "pts", player.hand.get_all_cards()

    def status_player_busted(self, player):
        print(player.get_name(), "busted!", self.player_status_end_game(player))

    def status_player_got_21(self, player):
        print(player.get_name(), "got 21!", self.player_status_end_game(player))

    def status_its_a_tie(self, player):
        print("It's a tie!", self.player_status_end_game(player))

    def status_won(self, player):
        print(player.get_name(), "won!", self.player_status_end_game(player))

    def game_over(self):
        print("GAME OVER")
