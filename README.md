# Mandelbulb
If you are interested in Fractals, you've probably heard of the Mandelbulb, however there is little documentation on 
the internet as to how to render it, even less so on how to do it in python.

<img src="/photo_exports/version_1.png" width="400" height="400" align="middle" >

This code is made to render the Mandelbulb 3D fractal in python 2.7.16 using pygame. The method used is called ray-tracing.
Link to Mandelbulb [Wikipedia](https://en.wikipedia.org/wiki/Mandelbulb).

The Mandelbulb iteration equation consists of taking powers of 3D points (8 is standard). However what does it mean to raise
a vector to the 8th power? This is of course not defined, but we can define it in any way we wish. One way of defining it
is to write down the vector position in spherical polars, and then multiply each angle by 8 and take the vector lenght to the
8th power.

The formulas for coordinates as a function of spherical polar angles are as follows


x = R sin(t) cos(p)
    
y = R sin(t) sin(p)
    
z = R cos(p)


Then the 8th power of this point is

x' = R^8 sin(8t) cos(8p)
    
y' = R^8 sin(8t)*sin(8p)
    
z' = R^8 cos(8p)



Once we know how to take powers of points, the Mandelbulb set is defined as the set of points c in R^3 such that z' = z^8 + c
converges (analogous to the definition of the Mandelbrot set in R^2).



