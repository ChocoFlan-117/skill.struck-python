#Draw a Sun#

import pygame
pygame.init() 

X = 400
Y = 400
BLUE = (90, 90, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (247, 171, 38)
YELLOW = (255, 251, 133)

DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:

  DISPLAY.fill(BLUE)
  
  pygame.draw.circle(DISPLAY, ORANGE, (200, 200), 70)

    #1
  pygame.draw.polygon(DISPLAY, YELLOW, [[180, 120], [190, 20], [230, 120]])
    #2
  pygame.draw.polygon(DISPLAY, YELLOW, [[120, 150], [80, 90], [150, 120]])
    #3
  pygame.draw.polygon(DISPLAY, YELLOW, [[120, 170], [

  pygame.display.flip()