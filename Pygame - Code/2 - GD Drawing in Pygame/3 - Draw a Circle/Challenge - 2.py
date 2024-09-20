#Target#

import pygame
pygame.init()

X = 400
Y = 400
WHITE = (255, 255, 255)
BLUE = (168, 202, 255)
RED = (254, 0, 0)

DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
    DISPLAY.fill(BLUE)
    pygame.draw.circle(DISPLAY, RED,(200, 200), 150)
    pygame.draw.circle(DISPLAY, WHITE,(200, 200), 130)
    pygame.draw.circle(DISPLAY, RED,(200, 200), 110)
    pygame.draw.circle(DISPLAY, WHITE,(200, 200), 90)
    pygame.draw.circle(DISPLAY, RED,(200, 200), 70)
    pygame.draw.circle(DISPLAY, WHITE,(200, 200), 50)
    pygame.draw.circle(DISPLAY, RED,(200, 200), 30)
    pygame.display.flip() 