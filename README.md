# Mandelbulb
If you are interested in Fractals, you've probably heard of the Mandelbulb, however there is little documentation on 
the internet as to how to render it, even less so on how to do it in python. 

This code is made to render the Mandelbulb 3D fractal in python 2.7.16 using pygame. The method used is called ray-tracing.

The Mandelbulb iteration equation consists of taking powers of 3D points (8 is standard). However what does it mean to raise
a vector to the 8th power? This is of course not defined, but we can define it in any way we wish. One way of defining it
is to write down the vector position in spherical polars, and then multiply each angle by 8 and take the vector lenght to the
8th power.

The formulas for coordinates as a function of spherical polar angles are as follows

x = R sin(t) cos(p)
    
y = R sin(t) sin(p)
    
z = R cos(p)


Then the 8th power of this point is

x' = R^8 sin(t) cos(p)
    
y' = R^8 sin(t)*sin(p)
    
z' = R^8 cos(p)
