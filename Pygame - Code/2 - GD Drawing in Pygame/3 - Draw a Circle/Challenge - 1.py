#Build a Snowman!#

import pygame
pygame.init()

X = 400
Y = 400
WHITE = (255, 255, 255)
BLUE = (168, 202, 255)

DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
    DISPLAY.fill(BLUE)
    pygame.draw.circle(DISPLAY, WHITE,(200, 300), 50)
    pygame.draw.circle(DISPLAY, WHITE,(200, 215), 40)
    pygame.draw.circle(DISPLAY, WHITE,(200, 144), 30)
    pygame.display.flip() 