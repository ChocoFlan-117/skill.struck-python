import pygame
pygame.init()

X = 500
Y = 500
GREEN = (140, 250, 90)

DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
    DISPLAY.fill(GREEN)
    pygame.display.flip()