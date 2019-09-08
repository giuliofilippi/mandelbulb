# Mandelbulb
If you are interested in Fractals, you've probably heard of the Mandelbulb, however there is little documentation on 
the internet as to how to render it, even less so on how to do it in python.

<img src="/photo_exports/capture_2.jpeg" width="400" height="400" />

This code is made to render the Mandelbulb 3D fractal in python 2.7.16 using pygame. The method used is called ray-tracing.
Link to [Mandelbulb Wikipedia](https://en.wikipedia.org/wiki/Mandelbulb).

The Mandelbulb iteration equation consists of taking powers of 3D points (we use 8). However what does it mean to raise
a vector to the 8th power? This is of course not defined, but we can define it in any way we wish. One way of defining it
is to write down the vector position in spherical polars, and then multiply each angle by 8 and take the vector lenght to the
8th power.

The Mandelbulb set is then defined as the set of points c in <b>R</b><sup>3</sup> such that z' = z<sup>8</sup> + c
converges (analogous to the definition of the Mandelbrot set in <b>R</b><sup>2</sup>).
