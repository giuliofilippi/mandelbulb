# Mandelbulb
If you are interested in Fractals, you've probably heard of the Mandelbulb, however there is little documentation on 
the internet as to how to render it in python.

<img src="/photo_exports/capture_2.jpeg" width="400" height="400" />

This repository is made to render the Mandelbulb 3D fractal using python 2.7.16 and pygame.
Link to [Mandelbulb Wikipedia](https://en.wikipedia.org/wiki/Mandelbulb).

The Mandelbulb iteration equation consists of taking powers of 3D points (we use 8). However what does it mean to raise
a vector to the 8th power? This is of course not defined, but we can define it in any way we wish. One way of defining it
is to write down the vector position in spherical polars, and then multiply each angle by 8 and take the vector lenght to the
8th power.

The Mandelbulb set is then defined as the set of points c in <b>R</b><sup>3</sup> such that z' = z<sup>8</sup> + c
converges (analogous to the definition of the Mandelbrot set in <b>R</b><sup>2</sup>).

The method used to draw the fractal is called ray tracing. Each pixel is given a location in 3D space, then the camera is also assigned a location. We shine a ray from the camera to each pixel in the screen and look at where it hits the fractal. To find out where it hits we use underestimates for Distance Estimations from a point to the fractal ([more information](http://blog.hvidtfeldts.net/index.php/2011/09/distance-estimated-3d-fractals-v-the-mandelbulb-different-de-approximations/)).

To show depth, we use gradients of a color with the intensity being determined by how much light shines on that point. More specifically, the formula used to determine intensity of a pixel is proportional to the cosine of the angle between the tangent to the fractal and the vector from the point light source to the fractal

