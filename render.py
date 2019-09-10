# Fun Project : Rendering the Mandelbulb 3d fractal!
# Python 2.7.16

# The way the Mandelbulb is made is analogous to the madelbrot set
# Details about how to calculate the set can be found on it's wikipedia
# page : https://en.wikipedia.org/wiki/Mandelbulb


# This file executes the drawing of the Mandelbulb using pygame


# imports
import time
from mandelbulb import *
import caffeine
caffeine.on(display=True)
import pygame, sys
from pygame.locals import *
import numpy as np
import math
import pickle
import os


if os.path.exists("pickles/contactpixelgrid2.pkl")==False:

    # create the grid of 3D locations of contact points of rays
    # fired through each pixel
    start = time.time()
    print ('Creating Pixel Locations Grid ...')
    arr = createcontactpixelgrid()
    print ('Done creating grid')
    end = time.time()
    print (str((end-start)/60)+' minutes elapsed')


    # export a pickle file for faster reference later
    with open('pickles/contactpixelgrid2.pkl','wb') as pickle_file:
        pickle.dump(arr,pickle_file)

else:
    with open('pickles/contactpixelgrid2.pkl','rb') as pickle_file:
        arr = pickle.load(pickle_file)


# Initiate a pygame screen
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Mandelbulb Set')


# Loop over each pixel and assign their colors
for i in range(0,800):
    print (str(i)+'/'+str(800))
    for j in range(0,800):
        # each pixel should get the right color
        col = colorcontactgrid((i,j),arr)
        pygame.Surface.set_at(screen, (i,j), col)


# Show display update
pygame.display.update()


# Save a photo of this Mandelbulb with new name
print ('Saving Photo ...')

i = 0
while os.path.exists("photo_exports/capture_" + str(i) + ".jpeg"):
    i += 1

filename = "photo_exports/capture_" + str(i) + ".jpeg"

pygame.image.save(screen, filename)

print ('DONE')


# Endless loop awaiting QUIT
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

