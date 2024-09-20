#Build a Maze!#

import pygame
pygame.init()

X = 500
Y = 500

YELLOW = (255, 187, 0)
BLUE = (3, 42, 255)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
    DISPLAY.fill(YELLOW)

    pygame.draw.rect(DISPLAY, BLUE, [200, 100, 20, 500])
    pygame.draw.rect(DISPLAY, BLUE, [124, 0, 20, 230])
    pygame.draw.rect(DISPLAY, BLUE, [0, 50, 70, 20])
    pygame.draw.rect(DISPLAY, BLUE, [0, 370, 100, 20])
    pygame.draw.rect(DISPLAY, BLUE, [300, 420, 150, 20])
    pygame.draw.rect(DISPLAY, BLUE, [60, 300, 150, 20])
    pygame.draw.rect(DISPLAY, BLUE, [50, 140, 20, 180])
    pygame.draw.rect(DISPLAY, BLUE, [200, 340, 120, 20])
    pygame.draw.rect(DISPLAY, BLUE, [300, 0, 20, 260])
    pygame.draw.rect(DISPLAY, BLUE, [360, 200, 20, 220])
    pygame.draw.rect(DISPLAY, BLUE, [100, 430, 120, 20])
    pygame.draw.rect(DISPLAY, BLUE, [240, 40, 140, 20])

    pygame.draw.circle(DISPLAY, WHITE, (20, 20), 4)
    pygame.draw.circle(DISPLAY, BLACK, (400, 470), 4)

    pygame.display.flip()