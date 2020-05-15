from card import *
from basicDeck import *
import pygame

def main():
    pygame.init()
    x = 0
    y = 0
    width = 800
    height = 600
    screen = pygame.display.set_mode([width, height])

    running = True

    player1 = basic()
    player2 = basic()
    gameDeck = basic()
    gameDeck.fullDeck()
    gameDeck.shuffle()
    cardBack = pygame.transform.rotozoom(pygame.image.load('./PNG/red_back.png').convert(), 0, 0.2)
    screen.fill((0,200,0))
    screen.blit(cardBack, (width * .3, height * .6))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if cardBack.get_rect().collidepoint(x,y):
                    cardDrawn = gameDeck.drawCard()
                    player1.addCard(cardDrawn)
                    cardDis = pygame.transform.rotozoom(pygame.image.load(cardDrawn.image).convert(), 0, 0.2)
                    #cardD = pygame.transform.rotozoom(cardDis, 0, 0.1)
                    screen.blit(cardDis, (width * .6, height * .6))
                    print(cardDrawn.id)
        if not gameDeck.deck:
            del cardBack
        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main()

