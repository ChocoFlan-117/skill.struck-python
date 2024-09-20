import pygame
pygame.init()

X = 500
Y = 500
YELLOW = (240, 255, 15)
NAVY_BLUE = (30, 0, 180)

DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
    DISPLAY.fill(YELLOW)
    pygame.draw.circle(DISPLAY, NAVY_BLUE,(200, 200), 100)
    pygame.display.flip() 