"""
Background
On board a satellite or spacecraft, a star tracker is an optical device that measures the positions of stars using photocells or a camera.

As the positions of many stars have been measured by astronomers to a high degree of accuracy, a star tracker allows to determine the orientation (or attitude) of the spacecraft with respect to the stars. In order to do this, the star tracker will obtain an image of the stars as input, measure their apparent position in its Field of View (FoV), and identify the stars so their position can be compared with their known absolute position from a star catalog.

Task
Your task is to write (a very simplified) processor that identifies stars (represented by the characters + or x or o and outputs their individual coordinates line by line.

The scanning of the sky is done row by row, starting from coordinate (1,1) in the top left corner of the FoV.
Input
Line 1: An integer n for the number of rows in your FoV.
Next n lines: each line represents a row of what the star tracker sees.

Be careful, there might be some noise in the FoV (for example comet dust), and not everything you see is a star.
Output
Line 1: The coordinates (x,y) of the first detected star.
Line 2: Coordinates of the second detected star.
Line N: Coordinates of the Nth detected star.

Exceptions are:
- if your FoV is filled with #, then you are blinded by a celestial object (for example the moon) and you have to output: BLINDED
- if your FoV does not contain enough valid stars (i.e. less than 1), then you have to output: SEARCH
Constraints
1 ≤ n ≤ 99
0 ≤ len(row) ≤ 1024
Example
Input

1
+

Output

(1,1)

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    row = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("I am blind and lost in space!")
------------------------------------
4
x 

                               +
                                                          


(1,1)
(32,3)
-------------------------
4
     .        +.                     .                      .
# .                    . x                .
                 o                               .
+             .                        .



(15,1)
(26,2)
(18,3)
(1,4)
------------------------------------
	6
	###############################
	###############################
	###############################
	###############################
	###############################
	###############################


BLINDED
-------------------------------------
2
+++++
                                                          

(1,1)
(2,1)
(3,1)
(4,1)
(5,1)

----------------------------------

6
###############################
###############################
####                  #########
####                  #########
###############################
###############################
"""

blinded = True
search = 0
n = int(input())
for i in range(1, n + 1, 1):
    row = input()
    if not blinded or not len(row) == row.count("#"):
        blinded = False
    for index, x in enumerate(row, 1):
        if x in "+xo":
            print(f"({index},{i})")
            search += 1
else:
    if blinded:
        print("BLINDED")
    elif search == 0:
        print("SEARCH")