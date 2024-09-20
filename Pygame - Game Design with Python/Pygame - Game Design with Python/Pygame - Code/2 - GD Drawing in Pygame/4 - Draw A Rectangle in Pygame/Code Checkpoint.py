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

    pygame.draw.rect(DISPLAY, WHITE, [100, 100, 50, 70])

    pygame.display.flip()