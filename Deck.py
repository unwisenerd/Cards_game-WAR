#
# Class for creating and managing game deck
#

import random
from Cards import Card
from Utilities import get_suits, get_ranks


def get_deck():
    deck = []
    for suit in get_suits():
        for rank in get_ranks():
            card = Card(suit, rank)
            deck.append(card)
    return deck


class Deck:

    def __init__(self):
        self.all_cards = get_deck()

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
