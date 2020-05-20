from card import *
from basicDeck import *
import pygame
import time

# initialize pygame
pygame.init()

# creates screen and width/height variables
width = 800
height = 600
screen = pygame.display.set_mode([width, height])


# function to blit all images
def display(ob, loc):
    for x in range(0, len(ob)):
        screen.blit(ob[x], loc[x])

def refresh(displayObjects, locations):
    screen.fill((0, 170, 0))
    display(displayObjects, locations)
    pygame.display.update()


def main():
    # set variable to ensure game loop continues until manually stopped
    running = True
    x = 0
    y = 0

    cardBack = pygame.transform.rotozoom(pygame.image.load('./PNG/red_back.png').convert(), 0, 0.08)

    # create lists to store image data and locations
    displayObjects = []
    locations = []
    cardsSelected = []
    # create locations for all cards
    for i in range(0, 13):
        for j in range(0, 4):
            locations.append((5 + (i * 60), 10 + (j * 150)))

    # create gameDeck from deck and card classes and shuffle it
    gameDeck = basic()
    gameDeck.fullDeck()
    gameDeck.shuffle()

    # add cardBacks into displayObject array
    for i in range(0, len(gameDeck.deck)):
        displayObjects.append(cardBack)

    # game loop
    while running:
        for event in pygame.event.get():
            #checks if exit
            if event.type == pygame.QUIT:
                running = False
            #checks is mouse clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                #gets point where mouse was clicked
                x, y = event.pos

                for i in range(0, len(locations)):
                    #checks to see if clicked on a card
                    if displayObjects[i].get_rect(topleft=(locations[i][0], locations[i][1])).collidepoint(x, y) and not i in cardsSelected:
                        cardsSelected.append(i)
                        print("collision with item: " + str(i))
                        todis = pygame.transform.rotozoom(pygame.image.load(gameDeck.deck[i].image).convert(), 0, 0.08)
                        displayObjects[i] = todis
                        refresh(displayObjects, locations)
                #if 2 cards have been clicked checks to see if equal value
                if len(cardsSelected) == 2:
                    cardsSelected.sort(reverse=True)
                    time.sleep(0.75)
                    if gameDeck.deck[cardsSelected[0]].value == gameDeck.deck[cardsSelected[1]].value:
                        #if equal remove both cards from display
                        locations.pop(cardsSelected[0])
                        locations.pop(cardsSelected[1])
                        displayObjects.pop(cardsSelected[0])
                        displayObjects.pop(cardsSelected[1])
                        cardsSelected = []
                    else:
                        # if not equal display backs of cards again
                        displayObjects[cardsSelected[0]] = cardBack
                        displayObjects[cardsSelected[1]] = cardBack
                        cardsSelected = []

        # refresh screen
        refresh(displayObjects, locations)


    pygame.quit()


main()
