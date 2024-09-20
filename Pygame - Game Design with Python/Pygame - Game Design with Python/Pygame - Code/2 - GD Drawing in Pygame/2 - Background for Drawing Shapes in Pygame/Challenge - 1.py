#Greatest and Least RGB values.#

import pygame
pygame.init()

X = 500
Y = 500
GREEN = (140, 250, 90)

DISPLAY = pygame.display.set_mode([X, Y])
pygame.display.set_caption('  ')
running = True

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

while running:
    DISPLAY.fill(WHITE)
    pygame.display.flip()