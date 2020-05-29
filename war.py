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

def isEmpty(self):
    if len(self.deck) == 0:
        return True
    else:
        return False
basic.isEmpty = isEmpty
## New Class defining the Player in the game
class Player():
    def __init__(self,id):
        self.id = id
        self.hand = basic()
        self.deck = basic()
        self.discard = basic()
        self.play = basic()
        self.active = True
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
        return transfer_finished
    moving_card = sender.drawCard()
    reciever.addCard(moving_card)
    transfer_finished = True
    return transfer_finished

### Phase 0: Set up 52 Card Deck, Player 1 Hand
#Setting up Starting Deck
start_deck = basic()
start_deck.fullDeck()
start_deck.shuffle()
#Set up holding area for ties
holding_area = basic()

#Set Up Number of players, defining the player class, and distributing cards
num_players = 2
players = [Player(i) for i in range(num_players)]
players = split_deck(start_deck,players)
game_running = True
print("************************PHASE 0: Setting up Game************************")
for player in players:
    print ("Player ID: " + str(player.id))
    player.deck.printDeck()
    print("-----")

##1:Draw cards from the players deck and put it into their play area - potential upgrade, put the card into a players hand, then they will pick a card to play

round_number = 0
while game_running:
    round_number += 1
    print("************************ROUND  # " + str(round_number)+ " ************************")
    print("************************PHASE 1: DRAWING A CARD FROM EACH PLAYER")
    for player in players:
        transfer(player.deck, player.play)
        print(player)
        player.play.printDeck()

    ##2:Compare the values of the played cards
    highest_value = 0
    game_status ={"Winner":None, "Ties": []}
    print("************************PHASE 2: DETERMINING WHO WON")
    for player in players:
        if player.play.deck[0].value > highest_value:
            game_status["Winner"] = player
            best_card = player.play.deck[0].id
            highest_value = player.play.deck[0].value
            game_status["Ties"].clear()
            game_status["Ties"].append(player)
        elif player.play.deck[0].value == highest_value:
            game_status["Winner"] = "TIE"
            game_status["Ties"].append(player)


    print("Round winner: " + str(game_status["Winner"]))
    print("Best Card: " + str(best_card))
    print("Ties:")
    print(game_status["Ties"])
    ##3 Resolve result of the round.
    print("************************PHASE 3: MOVING CARD BASED ON WIN")
    ##3a If the cards are equal value, put them into a holding area
    if game_status["Winner"] == "TIE":
        for player in players:
            transfer(player.play, holding_area)
    ##3b if one players card is higher than another, put all the play cards into the winners discard pile
    else :
        for player in players:
            transfer(player.play, game_status["Winner"].discard)
        ##3cWinning player also  gets all of the cards from the holding_area
        while True:
            if not transfer(holding_area, player.discard):
                break
    print("Discard Piles:")
    for player in players:
        print ("Player ID: " + str(player.id))
        player.discard.printDeck()
        print("-----")
    print("Holding Area:")
    holding_area.printDeck()
    # - Potential upgrade, flag the players that are in a tie for more than 2 people, but it needs to only do that if the tie is also the highest
    #4 Check if the game is over. Is there a player with an empty draw pile, and discard pile, they are gone
    for player in players:
        if player.play.isEmpty() and player.deck.isEmpty() and player.discard.isEmpty():
            player.active = False
            game_running = False
    # - Exit the game loop if this happens
    # - This will mean that a tie ends the last round, the player without cards loses
    # - Potential Upgrade, update the status of all players then check if there is a winner.
    #5 If a players draw pile is empty, shuffle the discard and put in into the draw pile
    for player in players:
        if player.deck.isEmpty():
            player.discard.shuffle()
            while True:
                if not transfer(player.discard, player.deck):
                    break

print("GAME ENDED!")
print("Winning player(s)")
for player in players:
    if player.active:
        print("Player ID: " + str(player.id))
#6 Return to the start of the cycle

##Bonus Features
#Create a hand and ability to play cards out of your hand. Possibly will make a function that will interface with the above phases.
#Create a player.status to handle the different exceptions that will come up in a 3+ player game
#Let a player enter their name

##Code clean up:
#Change split deck to use transfer card function
#Combine phase 1 and 2 into a single for loop
#Make everything one big for loop?


'''
Next on the list
1. Game doesn't have any graphics yest
2. Print functions need to be cleaned up so the terminal is easier to read during rounds.
3. Pauses and inputs are needed so the game doesn't instantly end itself.
4. Currently only works for 2 players I want to be able to make it work for 3 or 4 players.
 --  When there is a draw, every player gets to play next round, not just the players who tied.
 -- Game plays until someone is eliminated, not until last man standing
5. Hands don't do anything.

#Linix Test Comment
'''