### 1. How does a program read the cvMat object, in particular, what is the order of the pixel structure?

The cvMat is a matrix, the location of a particular pixel can be represented in a x and y way, say (x,y) would the pixel at row x and column y.
If the pixel has a third dimension of color feature. Then the color can be represented in the third dimension, using (x,y)[index].
