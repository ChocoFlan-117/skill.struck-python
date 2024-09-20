#Color Options#

import pygame
pygame.init()

X = 500
Y = 500
GREEN = (140, 250, 90)

DISPLAY = pygame.display.set_mode([X, Y])
pygame.display.set_caption("Erm")
running = True

WHITE = (255, 255, 255)
BLUE = (97, 168, 234)
RED = (226, 8, 8)
GREEN = (51, 240, 117)
ORANGE = (255, 162, 56)

while running:
    DISPLAY.fill(BLUE)
    pygame.display.flip()