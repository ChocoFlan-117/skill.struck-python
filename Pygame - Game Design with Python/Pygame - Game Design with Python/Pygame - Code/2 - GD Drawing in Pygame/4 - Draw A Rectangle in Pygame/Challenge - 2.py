#Rectangle Mind Bender#

import pygame
pygame.init()

X = 500
Y = 500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
    DISPLAY.fill(BLACK)

    pygame.draw.rect(DISPLAY, WHITE, [100, 100, 300, 160], 5)
    pygame.draw.rect(DISPLAY, WHITE, [30, 100, 120, 60], 5)
    pygame.draw.rect(DISPLAY, WHITE, [230, 220, 200, 60], 5)
    pygame.draw.rect(DISPLAY, WHITE, [300, 80, 50, 120], 5)
    pygame.draw.rect(DISPLAY, WHITE, [200, 100, 50, 60], 5)

    pygame.display.flip()