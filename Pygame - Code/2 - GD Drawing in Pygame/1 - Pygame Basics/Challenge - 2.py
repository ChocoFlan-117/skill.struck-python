#Custom Game Name#

import pygame
pygame.init()
 
X = 400
Y = 400

custom_title = input("What would you like the game to be called? ")

DISPLAY = pygame.display.set_mode([X, Y])
pygame.display.set_caption(custom_title)