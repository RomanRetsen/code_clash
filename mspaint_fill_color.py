"""

 Goal
Paint is a magical tool and birthplace to amazing early 2000s' artists. One functionality, in particular has revolutionized the way to make art: "Fill the color". This feature allows to change the color of a pixel and all neighboring pixels which share the same color.

Example:

.---.---.---.---.
| R | R | R | R |
:---+---+---+---:
| B | R | R | G |
:---+---+---+---:
| P | P | P | R |
'---'---'---'---'



Suppose we have a canvas like the one shown above and we want to change the upper row pixels from color 'R' to 'K'. If we click on the pixel (0,0), then it will change the color of the pixel (0,0) and all its vertical and horizontal neighbors to the desired color, like shown below:

.---.---.---.---.
| K | K | K | K |
:---+---+---+---:
| B | K | K | G |
:---+---+---+---:
| P | P | P | R |
'---'---'---'---'



Your goal is to replicate the "fill the color" feature as shown above. You'll be given the canvas as a 2D array, the coordinates of the mouse click by the user, and the new color.

Here are the following feature constraints:
- The colors are represented by integers
- The user's mouse click is always on the canvas
- The spread is only in horizontal, and vertical
- The y axis is vertical, and the x axis is horizontal
- The canvas is never empty
- The canvas is always a rectangle
Input
Line 1: the space-separated Y and X integer coordinates of the user's mouse click.
Line 2: the new integer color to apply.
Line 3: H, the height the canvas and W, the width of the canvas.
Next H lines: A sequence of space-separated integers that represents a row of the image.
Output
H lines: The sequences of space-separated integers that represent the rows of the new image.
Constraints
1 ≤ H, W ≤ 15
0 ≤ Y < H
0 ≤ X < W
Example
Input

1 0
4
2 3
1 2 3
9 5 6

Output

1 2 3
4 5 6

------------test2 Row

0 0
5
2 5
1 1 1 1 1
2 6 7 8 9

out

5 5 5 5 5
2 6 7 8 9

-----------test3 Column

0 0
7
4 4
1 2 3 4
1 5 6 7
1 8 9 10
1 11 12 13

out

7 2 3 4
7 5 6 7
7 8 9 10
7 11 12 13

----------test4 all

1 1
3
3 4
2 2 2 2
2 2 2 2
2 2 2 2

out

3 3 3 3
3 3 3 3
3 3 3 3


----------test5  one row and column

2 3
3
4 5
1 3 4 4 5
6 7 8 9 5
5 5 5 5 5
10 11 12 13 14

out

1 3 4 4 3
6 7 8 9 3
3 3 3 3 3
10 11 12 13 14

--------test6 old is new color
4 4
5
9 9
1 1 1 1 1 1 1 1 1
1 2 2 2 2 2 2 2 1
1 2 3 3 3 3 3 2 1
1 2 3 4 4 4 3 2 1
1 2 3 4 5 4 3 2 1
1 2 3 4 4 4 3 2 1
1 2 3 3 3 3 3 2 1
1 2 2 2 2 2 2 2 1
1 1 1 1 1 1 1 1 1

out

1 1 1 1 1 1 1 1 1
1 2 2 2 2 2 2 2 1
1 2 3 3 3 3 3 2 1
1 2 3 4 4 4 3 2 1
1 2 3 4 5 4 3 2 1
1 2 3 4 4 4 3 2 1
1 2 3 3 3 3 3 2 1
1 2 2 2 2 2 2 2 1
1 1 1 1 1 1 1 1 1

-----------test7 few rows and columns

1 3
9
9 9
1 1 2 1 2 1 2 1 1
1 2 2 2 2 2 2 2 1
1 2 3 3 3 3 3 2 1
1 2 3 4 2 4 3 2 1
1 2 3 4 5 4 3 2 1
1 2 3 4 4 4 3 2 1
1 2 3 3 2 3 3 2 2
1 2 2 2 2 2 2 2 1
2 1 1 1 1 1 1 1 2

out

1 1 9 1 9 1 9 1 1
1 9 9 9 9 9 9 9 1
1 9 3 3 3 3 3 9 1
1 9 3 4 2 4 3 9 1
1 9 3 4 5 4 3 9 1
1 9 3 4 4 4 3 9 1
1 9 3 3 9 3 3 9 9
1 9 9 9 9 9 9 9 1
2 1 1 1 1 1 1 1 2
"""

def fill_color_at(canvas, y, x, old_color, new_color):
    y_len = len(canvas)
    x_len = len(canvas[0])
    if y < 0 or y >= y_len or x < 0 or x >= x_len:
        return False
    elif not canvas[y][x] == old_color:
        return False
    else:
        canvas[y][x] = new_color
        fill_color_at(canvas, y-1, x, old_color, new_color)
        fill_color_at(canvas, y+1, x, old_color, new_color)
        fill_color_at(canvas, y, x-1, old_color, new_color)
        fill_color_at(canvas, y, x+1, old_color, new_color)

canvas = []
y_click, x_click = [int(i) for i in input().split()]
new_color = int(input())
height, width = [int(i) for i in input().split()]
for i in range(height):
    canvas.append([int(x) for x in input().split()])

fill_color_at(canvas, y_click, x_click, canvas[y_click][x_click], new_color)

print("\n".join([" ".join([str(y) for y in x]) for x in canvas]))