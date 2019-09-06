# Fun Project : Rendering the Mandelbulb 3d fractal!
# Python 2.7.16

# The way the Mandelbulb is made is analogous to the madelbrot set
# Details about how to calculate the set can be found on it's wikipedia
# page : https://en.wikipedia.org/wiki/Mandelbulb


# imports
import numpy as np
import math

# colors
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

# camera and light positions in 3d space
cam = np.array([0,0,-2])
light = np.array([1,1,-1.5])

# Executes the Mandelbulb iteration operation
# q is the power variable (8 is standard)
def nextpoint(c,p,q):
    x = p[0]
    y = p[1]
    z = p[2]

    R = (x**2 + y**2 + z**2)**0.5
    p = math.atan2(y,x)
    t = math.atan2((x**2 + y**2)**0.5,z)

    x2= (R**q)*math.sin(q*t)*math.cos(q*p)+c[0]
    y2= (R**q)*math.sin(q*t)*math.sin(q*p)+c[1]
    z2= (R**q)*math.cos(q*t)+c[2]

    return (x2,y2,z2)


# This is the Distance Estimation function
# It will estimate the distance from point c to the set
# Formula and how it works can be found on the internet
def DE(c,q):
	dr = 1.0
	r = 0
	z=c

	for i in range(100):
		r = float(np.linalg.norm(z))
		if r>4:
			return 0.5*math.log(r)*r/dr
		dr = (r**(q-1))*q*dr +1
		z = nextpoint(c,z,q)
	return 0


# Each pixel is given a location in 3d space
# the screen is -2 to 2 on both x and y axis, 0 on z axis
# The size of the screen is chosen to fit the mandelbulb
def location(pixel):
    i = pixel[0]
    j = pixel[1]
    deltax = 4./800
    deltay = 4./800
    x = -2 + i*deltax
    y = -2 + j*deltay
    return np.array([x,y,0])


# Normalise a vector
def normalise(vec):
    r = np.linalg.norm(vec)
    if r==0:
        return vec
    else:
        return (1./r)*vec


# determine the location of contact with the fractal when shooting a ray
# towards a pixel in the screen
def contactpixel(pixel):

	s = location(pixel)

	direction = normalise(s-cam)

	v = cam
	x = 0

    # if want more precision must give it more time to get there 40->100
	for i in range(100):
		x+=1

		change = DE(v,8)

        # 0.3 i added for safety
        # used to be 0.2, i think 0.3 is also okay
		v = v + direction*change*0.3


        # 0.005 is higher precision, used to be 0.01
		if DE(v,8)<=0.005:
			return v

	return 'none'


# the color is determined by looking at the angle between the normal to the fractal
# and the vector coming from the light
def colorcontactpixel(pixel):
    pixel_right = (pixel[0]+1,pixel[1])
    pixel_left = (pixel[0]-1,pixel[1])
    pixel_up = (pixel[0],pixel[1]+1)
    pixel_down = (pixel[0],pixel[1]-1)

    s1 = contactpixel(pixel)
    s2 = contactpixel(pixel_right)
    s3 = contactpixel(pixel_up)


    # check if none of the pixels have diverged
    if s1=='none' or s2=='none' or s3=='none':
        return (0,0,0)


    normal = normalise(np.cross(s1-s2,s1-s3))
    lightdir = normalise(s1-light)

    costheta = abs(np.dot(normal, lightdir))

    # color gradient of blue
    return (0,0,int(254*costheta))








# colorcontactpixel can be made better by considering points in the set and points not in set to not fuclk off the border
# right now very elementary
# for higher resolutions can increase number of pixels or zoom in
# This can also be made better by considering the fact that light intensity should depend on both angles to camera and light
# Think of averaging the cross product?







# need to be aware that the fractal will be draw to the precision of the pixel grid no more, no less

