# Workspace for working on War
from card import *
from basicDeck import *
import pygame

# Adding Temp Functions to add to basicDeck
def printDeck(self):
    for card in self.deck:
        print(card.id)
    print("Number of Cards = " + str(len(self.deck)))
basic.printDeck = printDeck

class Player():
    def __init__(self,id):
        self.id = id
        self.hand = basic()
        self.deck = basic()
        self.discard = basic()

def split_deck(start_deck, players):
    while len(start_deck.deck) != 0:
        #print("cards left = " str())
        for player in players:
            if len(start_deck.deck) == 0:
                break
            moving_card = start_deck.drawCard()
            player.deck.addCard(moving_card)
    return players

# Phase 1: Set up 52 Card Deck, Player 1 Hand
##Main Deck
start_deck = basic()
start_deck.fullDeck()
#main_deck.printDeck()

num_players = 2

#Set Up players
players = [Player(i) for i in range(num_players)]

#Splitting the deck for each player
players = split_deck(start_deck,players)

players[0].deck.printDeck()