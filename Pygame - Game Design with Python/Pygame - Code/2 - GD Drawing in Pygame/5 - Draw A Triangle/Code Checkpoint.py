import pygame 
pygame.init()

X = 500
Y = 500

BLUE = (15, 107, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

DISPLAY = pygame.display.set_mode([X, Y])
running  = True

while running:
    DISPLAY.fill(BLACK)

    pygame.draw.polygon(DISPLAY, WHITE, [[100, 100], [100, 200], [300, 150]])

    pygame.display.flip()