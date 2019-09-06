# Fun Project : Rendering the Mandelbulb 3d fractal!
# Python 2.7.16

# The way the Mandelbulb is made is analogous to the madelbrot set
# Details about how to calculate the set can be found on it's wikipedia
# page : https://en.wikipedia.org/wiki/Mandelbulb


# imports
import time
from mandelbulb import *
import caffeine
caffeine.on(display=True)
import pygame, sys
from pygame.locals import *
import numpy as np
import math

# Initiate a pygame screen
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Mandelbulb Set')
screen.fill((0,0,0))
pygame.display.update()

# start time to count number of seconds to execute code
start = time.time()

for i in range(0,800):
    end = time.time()
    print (str(end-start)+' seconds elapsed')
    print (str(i)+'/'+str(800))
    for j in range(0,800):
        # each pixel should get the right color
        col = colorcontactpixel((i,j))
        pygame.Surface.set_at(screen, (i,j), col)


pygame.display.update()

print ('Saving Photo')

pygame.image.save(screen, "photo_exports/capture.jpeg")

print ('DONE')

# Endless loop awaiting QUIT
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

