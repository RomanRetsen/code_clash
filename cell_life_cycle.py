"""
    Print the next state of the game of life board.

A board is represented by heightxwidth cells.
Each cell is either alive or dead. Represented by O and ..
A dead cell with 3 alive neighbors (including diagonals) becomes alive.
An alive cell with less than 2 alive neighbors or more than 3 alive neighbors becomes dead.
All other cells stay in the same state.
Input
Line 1: Two integers height and width: The size of the board.
Next height lines: A string row: Each row of the board.
Output
height lines: The rows of the next state of the board.
Constraints
The board contains only O and ..
Example
Input

6 6
......
.OO...
..O.O.
....O.
....O.
......

Output

......
.OOO..
.OO...
....OO
......
......


_____test2


3 7
.O...OO
O.O..OO
.O.....


.O...OO
O.O..OO
.O.....


__________test3

3 8
..O..O..
O.O...OO
.OO..OO.


.O....O.
..OO...O
.OO..OOO



__________________

10 50
.O.OOOO.O.OO.OOOOO.OO.O.O.O.O.O.O.O..O...O.O...O.O
.......O.O.OO..OO..O..OOO....OO.OO.OOOO..OO.O.OO..
..OOO.O.OO....OO.O..OO.O.OOO..O....OOO..O...OO.O..
...O.O....O..OO...OOOOO.O...OOOO.....O...OOO....OO
.OO.OO..O.O.O.O..O...O..O.OOOOOOOO.OO.O.OOO...OO..
OOOOO.O..OO.O.OOOOO.OO.O.O....O...OO..OOO..OO.OOO.
.O....OO...OO.OO.O....O.O.O.OOO.O........O.OO.OO..
.OOO.OOOOOOOOOO...OOO.O...OOO....O...O.OO.O.OOO.O.
O.OO.O....O..O.OO.O.O.O..O.OO..O.OO.O.OOO..OOO....
OOO..O..OO.OO..O..OO..OOOOO..OO..O.OOOOO.OO...OO..


....OOOOOOOO.OO..OOOOOO.OO....O.O.OO.OO..O.O..OOO.
...........OO......O........O.O.OO....O.OOO.O..O..
..OOOOOOOO.OO....O.......OOO....O.OO....O...OO.O..
.O....OOO.OO....OOOO....O.........O...OO...OOO..O.
O.....O...O.O...........O.OO....OO.OO.O.....OOO..O
O...O.O.OOO.O.....O.OO.O..........OOOOO.....O...O.
......................O.O.O.O.OO.OO......O........
O..O.O..OO........O.O.O.......OO.OO..O....O.......
O....O.........OO...O.O.......O..O................
O.OOO....OOOO.OOOOOO.OOOOOOOOOO.OO.OO....OOOOOO...


"""

import itertools

def will_be_alive(input_array, x, j):
    around = 0
    # all_options = [(n, m) for n, m in itertools.product([-1, 1, 0], repeat=2) if (not n == 0 or not m == 0)]
    all_options = filter(lambda x: (x[0] != 0 or x[1] != 0), itertools.product([-1, 1, 0], repeat=2))
    for option_x, option_j in all_options:
        if x - option_x >= 0 and x - option_x <= height -1 and j - option_j >= 0 and j - option_j <= width - 1:
            if input_array[x-option_x][j-option_j] == "O":
                around += 1
    if input_array[x][j] == "." and around == 3:
        return True
    elif input_array[x][j] == "O" and around in [2,3]:
        return True
    else:
        return False

height, width = [int(i) for i in input().split()]
the_matrix = []
for i in range(height):
    row = input()
    the_matrix.append([x for x in row])

next_round = [["." for _ in range(width)] for _ in range(height)]

for i in range(height):
    for j in range(width):
        if will_be_alive(the_matrix, i, j):
            next_round[i][j] = "O"
        else:
            next_round[i][j] = "."

for i in range(height):
    print(*next_round[i], sep="")
    