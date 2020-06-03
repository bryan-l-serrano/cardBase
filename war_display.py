import sys, pygame, time
pygame.init()

size = width, height = 1600, 900
speed = [10, 10]
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
background = 145,30,30
print(type(background))

colors = [red, green, blue]

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]



    screen.fill(background)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    time.sleep(1/60)