"""
In this challenge we need to calculate all the total number of legal chess moves for the knight piece.
You receive a list of Initial position for the Knight piece and you need to add all the position

As an example : 
A1
H1
F4
E5
A7

The expected move are : 
A1: ['B3', 'C2']
H1: ['F2', 'G3']
F4: ['D3', 'D5', 'E2', 'E6', 'G2', 'G6', 'H3', 'H5']
E5: ['C4', 'C6', 'D3', 'D7', 'F3', 'F7', 'G4', 'G6']
A7: ['B5', 'C6', 'C8']

So the answer would be : 23

Answer to large example 525378
"""
the_board = {}
the_moves = {}
total = 0

#build map of the board the map of the moves
for key_height, value_num in enumerate("87654321"):
    for key_width, value_letter in enumerate("ABCDEFGH"):
        the_board[(key_height, key_width)] = f"{value_letter}{value_num}"
        the_moves[f"{value_letter}{value_num}"] = []

for key_height, value_num in enumerate("87654321"):
    for key_width, value_letter in enumerate("ABCDEFGH"):
        if key_height - 2 > -1 and key_width + 1 < 8:
            the_moves[the_board[(key_height, key_width)]].append(the_board[(key_height-2, key_width+1)])
        if key_height - 2 > -1 and key_width - 1 > -1:
            the_moves[the_board[(key_height, key_width)]].append(the_board[(key_height-2, key_width-1)])
        if key_height + 2 < 8 and key_width + 1 < 8:
            the_moves[the_board[(key_height, key_width)]].append(the_board[(key_height+2, key_width+1)])
        if key_height + 2 < 8 and key_width - 1 > -1:
            the_moves[the_board[(key_height, key_width)]].append(the_board[(key_height+2, key_width-1)])
        if key_height - 1 > -1 and key_width + 2 < 8:
            the_moves[the_board[(key_height, key_width)]].append(the_board[(key_height-1, key_width+2)])
        if key_height - 1 > -1 and key_width - 2 > -1:
            the_moves[the_board[(key_height, key_width)]].append(the_board[(key_height-1, key_width-2)])
        if key_height + 1 < 8 and key_width + 2 < 8:
            the_moves[the_board[(key_height, key_width)]].append(the_board[(key_height+1, key_width+2)])
        if key_height + 1 < 8 and key_width - 2 > -1:
            the_moves[the_board[(key_height, key_width)]].append(the_board[(key_height+1, key_width-2)])

while True:
    one_line = input()
    if one_line == "":
        break
    else:
        total += len(the_moves[one_line])
print(total)



