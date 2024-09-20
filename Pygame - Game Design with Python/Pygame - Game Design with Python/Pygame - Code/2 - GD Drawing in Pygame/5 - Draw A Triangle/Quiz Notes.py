######################
#Which code would you use to draw a triangle in Pygame?
#Answer: pygame.draw.polygon()
######################



########################
#True or False: A triangle is a kind of polygon.
#Answer: True
#########################



#########################
#What would this draw if you ran the following code?
import pygame
pygame.init() 

X = 500
Y = 500
BLUE = (90, 90, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:

  DISPLAY.fill(BLUE)
  pygame.draw.polygon( )
  pygame.display.flip()
#Answer: Nothing.
###########################



##############################
#In the third attribute of a triangle, what do these numbers mean?
#Answer: The (x,y) location of the three points of the triangle.
##############################