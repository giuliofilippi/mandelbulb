# Fun Project : Rendering the Mandelbulb 3d fractal!
# Python 2.7.16

# The way the Mandelbulb is made is analogous to the madelbrot set
# Details about how to calculate the set can be found on it's wikipedia
# page : https://en.wikipedia.org/wiki/Mandelbulb


# This file contains functions useful to draw the Mandelbulb
# The drawing is done in render.py


# imports
import numpy as np
import math
import numpy as np

# colors
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
grey = (183,185,187)

# camera and light positions in 3d space
cam = np.array([1,1,-1.5])
light = np.array([1,1,-1.5])


# Get unit vectors spanning screen as function of camera position
# there is some randomness to it
zero = np.array([0,0,0])

# normalise camera position
ncam = cam/np.linalg.norm(cam)

# get first unit vector
unit_1 = np.random.randn(3)
unit_1 -= unit_1.dot(ncam) * ncam
unit_1 /= np.linalg.norm(unit_1)

# get second unit vector
unit_2 = np.cross(ncam, unit_1)


# -----------------------------------------------------------------


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


# Each pixel is given a location in 3d space
# This is an altered version of the above function that allows for different
# camera positions
def location_ext(pixel):

    # recenter at (400,400)
    i = pixel[0]-400
    j = pixel[1]-400

    # set the delta
    delta = 4./800

    vec = delta*unit_1*i + delta*unit_2*j

    return vec



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

    s = location_ext(pixel)
    direction = normalise(s-cam)
    v = cam

    # if want more precision must give it more iterations to get there
    for i in range(150):

        # distance estimator
        dist = DE(v,8)

        # 0.0005 is precision
        if dist<=0.0005:
            return v

        if dist>5:
            return 'none'



        # 0.3 i added for safety because DE is an approximation
        v = v + direction*dist*0.3



    return 'none'

# create grid of contact locations
def createcontactpixelgrid():

    arr = np.empty(shape=(801,801),dtype=np.ndarray)

    for i in range(0,801):
        print (str(i)+'/'+str(800))
        for j in range(0,801):
            # each pixel should get it's position
            pos = contactpixel((i,j))
            arr[i][j] = pos

    return arr


def color_pixel(theta,color):
    a = color[0]*theta
    b = color[1]*theta
    c = color[2]*theta

    return (a,b,c)


# get the pixel color from a grid of positions
def colorcontactgrid(pixel,arr):
    i = pixel[0]
    j = pixel[1]

    s1 = arr[i][j]
    s2 = arr[i+1][j]
    s3 = arr[i][j+1]

    # check if none of the pixels have diverged
    if s1=='none' or s2=='none' or s3=='none':
        return (0,0,0)

    normal = normalise(np.cross(s1-s2,s1-s3))
    lightdir = normalise(s1-light)

    costheta = abs(np.dot(normal, lightdir))

    # color gradient of blue
    return color_pixel(costheta,grey)






# right now very elementary
# Think of averaging the cross product
# need to be aware that the fractal will be draw to the precision of the pixel grid no more, no less

