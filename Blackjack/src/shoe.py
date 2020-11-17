import random


class Shoe:
    def __init__(self):
        self.shoe = []
        self.init_deck()

    def init_deck(self):
        for shoe in range(6):
            for deck in range(4):
                for card in range(13):
                    self.shoe.append(card + 1)
        random.shuffle(self.shoe)

    def get_card(self):
        if len(self.shoe) == 0:
            print("SHUFFLING DECK")
            self.init_deck()
        card = self.shoe.pop()
        if card > 10:
            card = 10
        return card

    def get_size(self):
        return
