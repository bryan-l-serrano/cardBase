from card import *
from basicDeck import *
import pygame

width = 800
height = 600
screen = pygame.display.set_mode([width, height])

def display(ob, loc):
    for x in range(0,len(ob)):
        screen.blit(ob[x], loc[x])

def main():

    pygame.init()
    numberOfCardsDrawn = 0
    x = 0
    y = 0

    running = True
    player1 = basic()
    player2 = basic()
    gameDeck = basic()
    gameDeck.fullDeck()
    gameDeck.shuffle()
    cardBack = pygame.transform.rotozoom(pygame.image.load('./PNG/red_back.png').convert(), 0, 0.2)
    screen.fill((0,170,0))
    pygame.display.flip()
    displayObjects =[cardBack]
    locations = [(width * .02, height * .6)]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if gameDeck.deck:
                     if cardBack.get_rect(topleft=(width* 0.02, height* .6)).collidepoint(x,y):
                        cardDrawn = gameDeck.drawCard()
                        numberOfCardsDrawn += 1
                        player1.addCard(cardDrawn)
                        thisCard = pygame.transform.rotozoom(pygame.image.load(cardDrawn.image).convert(), 0, 0.2)
                        displayObjects.append(thisCard)
                        locations.append((width * 0.2 +(numberOfCardsDrawn * 6), height * 0.6))
                        print(cardDrawn.id)
                        print(len(gameDeck.deck))
                        if len(gameDeck.deck) == 0:
                            del displayObjects[0]
                            del locations[0]
        screen.fill((0,170,0))
        display(displayObjects, locations)
        pygame.display.update()
    pygame.quit()

main()

