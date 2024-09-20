####################
#What values are used in Pygame to represent colors?
#Answer: RGB
#####################



######################
#How many numbers are needed for a RGB value to get color?
#Answer: 3
######################



#########################
#Which of the following code segments will color the background green for this game code?
import pygame
pygame.init() 

X = 500
Y = 500
GREEN = (30, 255, 15)


DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  DISPLAY.fill(GREEN)

pygame.quit()
#Answer: DISPLAY.fill(GREEN)
########################



########################
#True or False: You can only use certain designated colors in Pygame.
#Answer: False
##########################



#########################
#Where does the main code to run the game go?
#Answer: Inside the while running loop.
#########################



#########################
#What kind of data type is the variable named running equal to?
running = True
#Answer: boolean
#########################