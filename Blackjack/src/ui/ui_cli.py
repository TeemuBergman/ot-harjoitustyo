class Ui:
    """UI class responsible for the CLI UI."""

    def player_cash_balance(self, player, bet):
        print("")
        print("Your cash balance:",
              player.cash_balance, "€")
        print("Current bet:", bet, "€")

    def player_status_hand(self, player, cards = 0):
        print("Your current hand:",
              player.hand.get_sum_of_cards(),
              "points",
              player.hand.cards[cards])

    def player_selection_start(self):
        return input("Select: (d)eal a new hand | modify bet: (+)100, (-)100 | (o)ptions: ").lower()

    def player_options(self):
        return input("Select: (s)ave game | (l)oad game | (q)uit: ").lower()

    def player_saved(self):
        print("")
        print("----- Game saved!")

    def player_loaded(self):
        print("")
        print("----- Game loaded!")

    def player_selection_hand(self, hand_num = 0):
        if hand_num == 0:
            print("Deal a new card?")
        else:
            print("Deal a new card to hand", str(hand_num) + "?")
        return input("Select: (h)it | (p)ass: ").lower()

    def player_split_hand(self, player, current_bet):
        print("Your first two cards have the same value:", player.hand.cards[0])
        print("Do you want to split your hand (cost", current_bet, "€)?")
        return input("Select: (s)plit | (p)ass: ").lower()

    def player_selection_split_hand(self, player):
        print("")
        print("----- SPLIT HANDS:")
        print("----- Hand 1:",
              player.hand.get_sum_of_cards(1),
              player.hand.cards[1])
        print("----- Hand 2:",
              player.hand.get_sum_of_cards(2),
              player.hand.cards[2])

    def player_blackjack(self, player, current_bet):
        print(player.name,
              "got a BLACKJACK! and won", current_bet * 2.5, "€",
              "from house with", player.hand.cards[0])

    def player_got_21(self, player, current_bet, hand_num = 0):
        print(player.name,
              "got 21 points and won",
              current_bet * 2, "€",
              "from house with", player.hand.cards[hand_num])

    def player_won(self, player, current_bet, hand_num = 0):
        print(player.name,
              "won", current_bet * 2, "€",
              "from house with", player.hand.get_sum_of_cards(hand_num), "points",
              player.hand.cards[hand_num])

    def player_busted(self, player, current_bet, hand_num = 0):
        print(player.name,
              "busted and lost", current_bet, "€",
              "to house with", player.hand.get_sum_of_cards(hand_num), "points",
              player.hand.cards[hand_num])

    def player_tie(self, player, current_bet, hand_num = 0):
        print("It's a tie and",
              player.name, "gets a bet of",
              current_bet, "€ back with",
              player.hand.get_sum_of_cards(hand_num), "points",
              player.hand.cards[hand_num])

    def player_lost(self, player, current_bet, hand_num = 0):
        print(player.name,
              "lost", current_bet, "€",
              "to house with", player.hand.get_sum_of_cards(hand_num), "points",
              player.hand.cards[hand_num])

    def player_no_cash_for_split(self, player, current_bet):
        print("Not enough cash for split:", player.cash_balance, "/", current_bet)

    # Dealer

    def dealer_status(self, dealer):
        print("Dealers hand is",
              dealer.hand.get_sum_of_cards(),
              "points",
              dealer.hand.cards[0])

    def dealer_top_card(self, dealer):
        print("Dealers top card:", dealer.hand.cards[0][1])

    def dealer_21(self, dealer):
        print("Dealers got 21!")

    # Common

    def title(self):
        print("")
        print("Welcome to...")
        print("P R O -------♠♥♦♣")
        print("B L A C K J A C K")
        print("♠♥♦♣----- 2 0 2 0")

    def play_again(self):
        print("")
        print("P L A Y -------♦♣")
        print("♠♥--- A G A I N ?")

    def new_hand(self):
        print("")
        print("----- DEALING A NEW HAND!")

    def showdown(self):
        print("")
        print("----- SHOWDOWN!")

    def shuffling_deck(self):
        print("----- SHUFFLING DECK")

    def game_over(self):
        print("Player is out of cash! :(")
        print("G A M E  O V E R")
