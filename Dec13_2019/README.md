# Riddler Classic : Dec 13th, 2019


## Problem Statement

From Steve Abney comes a particularly prismatic puzzle:

Suppose I have a rectangle whose side lengths are each a whole number, and whose area (in square units) is the same as its perimeter (in units of length). What are the possible dimensions for this rectangle?

Alas, that’s not the riddle — that’s just the appetizer. The rectangle could be 4 by 4 or 3 by 6. You can check both of these: 4 · 4 = 16 and 4 + 4 + 4 + 4 = 16, while 3 · 6 = 18 and 3 + 6 + 3 + 6 = 18. These are the only two whole number dimensions the rectangle could have. (One way to see this is to call the rectangle’s length a and its width b. You’re looking for whole number solutions to the equation ab = 2a + 2b.)

On to the main course! Instead of rectangles, let’s give rectangular prisms a try. What whole number dimensions can rectangular prisms have so that their volume (in cubic units) is the same as their surface area (in square units)?

To get you started, Steve notes that 6 by 6 by 6 is one such solution. How many others can you find?

## Solution

Rectangular prism dimentions that have equal surface area and volume are as follows:

    - 3 x 7 x 42
    
    - 3 x 8 x 24
    
    - 3 x 9 x 18
    
    - 3 x 10 x 15
    
    - 3 x 12 x 12
    
    - 4 x 5 x 20
    
    - 4 x 6 x 12
    
    - 4 x 8 x 8
    
    - 5 x 5 x 10
    
    - 6 x 6 x 6

Full solution/Program output can be found in results.txt


## Solution Methodology

Pretty simple script this time around.  Iterated through all values in the range of a specified maximum.  If that specific combination of dimentions resulted in a rectangular prism with equal surface area and volume print the combination.
