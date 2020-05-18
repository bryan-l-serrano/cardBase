from card import *
from basicDeck import *
import pygame

#initialize pygame
pygame.init()

#creates screen and width/height variables
width = 800
height = 600
screen = pygame.display.set_mode([width, height])


#function to blit all images
def display(ob, loc):
    for x in range(0,len(ob)):
        screen.blit(ob[x], loc[x])


def main():
    # set variable to ensure game loop continues until manually stopped
    running = True
    x = 0
    y = 0

    cardBack = pygame.transform.rotozoom(pygame.image.load('./PNG/red_back.png').convert(), 0, 0.08)


    #create lists to store image data and locations
    displayObjects = []
    locations = []

    #create locations for all cards
    for i in range(0, 13):
        for j in range(0, 4):
            locations.append((5+(i * 60), 10+(j * 150)))

    #create gameDeck from deck and card classes and shuffle it
    gameDeck = basic()
    gameDeck.fullDeck()
    gameDeck.shuffle()

    #add cardBacks into displayObject array
    for i in range(0, len(gameDeck.deck)):
        displayObjects.append(cardBack)

    #game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                print(str(x) + ":" + str(y))

                #
                #           To do
                # find collision conditions for all values
                # logic for displaying selected cards
                # logic for removing matching cards
                #
                #
        #refresh screen
        screen.fill((0, 170, 0))
        display(displayObjects, locations)
        pygame.display.update()


    pygame.quit()

main()