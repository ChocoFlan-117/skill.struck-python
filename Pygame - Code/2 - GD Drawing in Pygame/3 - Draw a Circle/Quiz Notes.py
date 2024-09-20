#########################
#What does the following code do? pygame.display.flip()
#Answer: It allows the drawings to show on the screen.
#########################



########################
#What does the value of 50 mean in the following code?
pygame.draw.circle(DISPLAY, WHITE, (100, 100), 50)
#Answer: The radius of the circle.
########################



##########################
#What does the second attribute of a circle drawing in Python determine?
#Answer: color
##########################



###########################
#What color is this circle?
import pygame
pygame.init() 

X = 500
Y = 500
YELLOW = (240, 255, 15)
RED = (255, 15, 15)
ORANGE = (255, 200, 15)
PINK = (255, 15, 220)
DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  DISPLAY.fill(BLUE)
  pygame.draw.circle(DISPLAY, YELLOW, (100, 100), 25)
  pygame.display.flip()


pygame.quit()
#Answer: yellow
############################