#Draw a Cow#

import pygame
pygame.init()

X = 500
Y = 500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (168, 200, 249)
GREEN = (36, 189, 14)
PINK = (236, 177, 231)

DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
    DISPLAY.fill(BLUE)

    #Grass
    pygame.draw.rect(DISPLAY, GREEN, [0, 300, 429, 450])
    pygame.draw.rect(DISPLAY, BLACK, [0, 300, 430, 451], 3)

    #Body
    pygame.draw.rect(DISPLAY, WHITE, [150, 230, 150, 150])
    pygame.draw.rect(DISPLAY, BLACK, [150, 230, 151, 151], 3)

    #Spots
    pygame.draw.rect(DISPLAY, BLACK, [180, 280, 50, 30])
    pygame.draw.rect(DISPLAY, BLACK, [240, 340, 50, 30])
    pygame.draw.rect(DISPLAY, BLACK, [250, 250, 30, 20])
    pygame.draw.rect(DISPLAY, BLACK, [150, 340, 30, 40])

    #Head
    pygame.draw.rect(DISPLAY, WHITE, [120, 200, 78, 90])
    pygame.draw.rect(DISPLAY, BLACK, [120, 200, 79, 91], 3)

    #Snout
    pygame.draw.rect(DISPLAY, PINK, [120, 250, 78, 40])
    pygame.draw.rect(DISPLAY, BLACK, [120, 250, 79, 41], 3)

    #Nostrils
        #Left
    pygame.draw.rect(DISPLAY, BLACK, [140, 260, 5, 15])
        #Right
    pygame.draw.rect(DISPLAY, BLACK, [160, 260, 5, 15])
    
    #Eyes
        #Left
    pygame.draw.circle(DISPLAY, BLACK, (145, 230), 5)
        #Right
    pygame.draw.circle(DISPLAY, BLACK, (170, 230), 5)

    #Ears
        #Right
    pygame.draw.rect(DISPLAY, WHITE, [196, 200, 15, 25])
    pygame.draw.rect(DISPLAY, BLACK, [196, 200, 16, 26], 3)
        #Left
    pygame.draw.rect(DISPLAY, WHITE, [106, 200, 15, 25])
    pygame.draw.rect(DISPLAY, BLACK, [106, 200, 16, 26], 3)

    pygame.display.flip()

#Moo