#Solar System#

import pygame
pygame.init()

X = 400
Y = 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

MERCURY = (5, 255, 226)
VENUS = (157, 43, 233)
EARTH = (4, 0, 224)
MARS = (51, 225, 187)
JUPITER = (245, 36, 168)
SATURN = (255, 160, 71)
URANUS = (130, 238, 23)
NEPTUNE = (232, 168, 255)
SUN = (255, 200, 0)

DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
    DISPLAY.fill(BLACK)

    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 200, 1)    # Ring 1
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 179, 1)   # Ring 2
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 170, 1)   # Ring 3
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 156, 1)   # Ring 4
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 144, 1)   # Ring 5
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 120, 1)  # Ring 6
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 79, 1)  # Ring 7
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 50, 1)  # Ring 8

 

    pygame.draw.circle(DISPLAY, MERCURY,(95, 200), 20)
    pygame.draw.circle(DISPLAY, VENUS,(230, 240), 25)
    pygame.draw.circle(DISPLAY, EARTH,(287, 150), 10)
    pygame.draw.circle(DISPLAY, MARS,(230, 240), 15)
    pygame.draw.circle(DISPLAY, JUPITER,(230, 240), 8)
    pygame.draw.circle(DISPLAY, SATURN,(230, 240), 12)
    pygame.draw.circle(DISPLAY, URANUS,(230, 240), 21)
    pygame.draw.circle(DISPLAY, NEPTUNE,(230, 240), 10)
    pygame.draw.circle(DISPLAY, SUN,(200, 200), 20)
    
    pygame.display.flip() 