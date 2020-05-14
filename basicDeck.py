from card import *
import random

value = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
suit = ['h', 's', 'c', 'd']


class basic:
    def __init__(self):
        self.deck = []

    def addCard(self, card):
        self.deck.append(card)

    def fullDeck(self):
        for x in range(0, len(value)):
            for y in range(0, len(suit)):
                self.deck.append(card(value[x] + suit[y], value[x]))

    def shuffle(self):
        random.shuffle(self.deck)

    def drawCard(self):
        thisCard = self.deck.pop(0)
        return thisCard
