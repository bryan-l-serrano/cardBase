# Workspace for working on War
from card import *
from basicDeck import *
import pygame

##Subclasses and Methods added to basicDeck
# New function to print what is in the deck/player hand, etc
def printDeck(self):
    print("Number of Cards = " + str(len(self.deck)))
    hand = ""
    for card in self.deck:
        hand += str(card.id) + ", "
    print(hand)
basic.printDeck = printDeck
#Return number of cards remaining in deck
def numCards(self):
    return len(self.deck)
basic.numCards = numCards


## New Class defining the Player in the game
class Player():
    def __init__(self,id):
        self.id = id
        self.hand = basic()
        self.deck = basic()
        self.discard = basic()
        self.play = basic()
    def __repr__(self):
        return "**Player ID: " +str(self.id)+ "**"

## functions related to the basic and Player classes
#Evenly split the cards among all the players
def split_deck(start_deck, players):
    while len(start_deck.deck) != 0:
        #print("cards left = " str())
        for player in players:
            if len(start_deck.deck) == 0:
                break
            moving_card = start_deck.drawCard()
            player.deck.addCard(moving_card)
    return players
#Transfer a card from one deck to another. Returns Updated Sender, Updated Reciever, and whether the operation worked
def transfer(sender, reciever):
    transfer_finished = False
    if sender.numCards() == 0:
        return sender, reciever, transfer_finished
    moving_card = sender.drawCard()
    reciever.addCard(moving_card)
    transfer_finished = True
    return sender, reciever, transfer_finished

### Phase 0: Set up 52 Card Deck, Player 1 Hand
#Setting up Starting Deck
start_deck = basic()
start_deck.fullDeck()
#start_deck.shuffle()

#Set Up Number of players, defining the player class, and distributing cards
num_players = 2
players = [Player(i) for i in range(num_players)]
players = split_deck(start_deck,players)
for player in players:
    print ("Player ID: " + str(player.id))
    player.deck.printDeck()
    print("-----")

##1:Draw cards from the players deck and put it into their play area - potential upgrade, put the card into a players hand, then they will pick a card to play
for player in players:
    transfer(player.deck, player.play)
    print(player)
    player.play.printDeck()

##2:Compare the values of the played cards
highest_value = 0
game_status ={"Winner":None, "Ties": []}

for player in players:
    if player.play.deck[0].value > highest_value:
        game_status["Winner"] = player
        highest_value = player.play.deck[0].value
        game_status["Ties"].clear()
        game_status["Ties"].append(player)
    elif player.play.deck[0].value == highest_value:
        game_status["Winner"] = "TIE"
        game_status["Ties"].append(player)


print("===========")
print("Round winner: " + str(game_status["Winner"]))
print("Ties:")
print(game_status["Ties"])
##3 Resolve result of the round.
##3a If the cards are equal value, put them into a holding area
# - Potential upgrade, flag the players that are in a tie for more than 2 people, but it needs to only do that if the tie is also the highest
##3b if one players card is higher than another, put all the play cards into the winners discard pile
#4 Check if the game is over. Is there a player with an empty draw pile, and discard pile, they are gone
# - Exit the game loop if this happens
# - This will mean that a tie ends the last round, the player without cards loses
# - Potential Upgrade, update the status of all players then check if there is a winner.
#5 If a players draw pile is empty, shuffle the discard and put in into the draw pile
# - This might need another function to automate moving the entire card pile.
#6 Return to the start of the cycle

##Bonus Features
#Create a hand and ability to play cards out of your hand. Possibly will make a function that will interface with the above phases.
#Create a player.status to handle the different exceptions that will come up in a 3+ player game
#Let a player enter their name

##Code clean up:
#Change split deck to use transfer card function
#Combine phase 1 and 2 into a single for loop