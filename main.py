from card import *
from basicDeck import *

def main():
    player1 = basic()
    player2 = basic()
    gameDeck = basic()
    gameDeck.fullDeck()
    print("first card in game deck: " + gameDeck.deck[0].id)
    gameDeck.shuffle()
    print("first card in game deck after shuffling: " + gameDeck.deck[0].id)
    cardDrawn = gameDeck.drawCard()
    player1.addCard(cardDrawn)
    print("length of player 1 deck after card is drawn: " + str(len(player1.deck)))
    print("length of player 2 deck after card is drawn: " + str(len(player2.deck)))
    print("length of game deck after card is drawn: " + str(len(gameDeck.deck)))



if __name__ == "__main__":
    main()

