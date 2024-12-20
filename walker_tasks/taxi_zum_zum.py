'''
Taxi Zum Zum

def taxi_zum_zum(moves):
A lone taxicab cruising the street grid of the dusky Manhattan that we know and love from classic
hardboiled ilm noir works such as “Blast of Silence” starts its journey at the origin (0,0) of the
in inite two-dimensional integer grid, denoted by Z 2 . Fitting in the gaunt and angular spirit of the
time that tolerates few deviations or grey areas, the taxicab is at all times headed straight in one of
the four main axis directions, initially north.
This taxicab then executes the given sequence of moves, given as a string of characters 'L' for
turning 90 degrees left while standing in place (just in case we are making a turn backwards, in case
you spotted some glad rags or some out-of-town palooka looking to be taken for a ride), 'R' for
turning 90 degrees right (ditto), and 'F' for moving one block forward to current heading. This
function should return the inal position of the taxicab on this in initely spanning Manhattan.
(Before the reader objects to the idea of Manhattanization of everything, perhaps the rest of the
world lazily simulates this in inite street grid with mirrors?)
'''
def taxi_zum_zum(moves):
    current_location = [0, 0]
    current_vector = "N"
    move_adjust = {"N": (0,1), "S": (0,-1), "E":(1, 0), "W":(-1, 0)}
    vector_adjust = {"L":{"N":"W", "S":"E", "E":"N", "W":"S"}, "R":{"N":"E", "S":"W", "E":"S", "W":"N"}}

    for move in moves:
        if move == "F":
            current_location[0] += move_adjust[current_vector][0]
            current_location[1] += move_adjust[current_vector][1]
        elif move in vector_adjust.keys():
            current_vector = vector_adjust[move][current_vector]
    return tuple(current_location)

# str_to_process = 'RFRL'
# str_to_process = 'FFLLLFRLFLRFRLRRL'
# str_to_process = 'FR' * 1729
str_to_process = 'LFFLF'
print(taxi_zum_zum(str_to_process))

