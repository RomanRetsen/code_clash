def words_with_letters(words, letters):
    pass


current_location = [0, 0]
current_vector = "N"
move_adjust = {"N": (0,1), "S": (0,-1), "E":(1, 0), "W":(-1, 0)}
vector_adjust = {"L":{"N":"W", "S":"E", "E":"N", "W":"S"}, "R":{"N":"E", "S":"W", "E":"S", "W":"N"}}

moves = input()
for move in moves:
    if move == "F":
        print("here")
        current_location[0] += move_adjust[current_vector][0]
        current_location[1] += move_adjust[current_vector][1]
    elif move in vector_adjust.keys():
        current_vector = vector_adjust[move][current_vector]

print(current_location)

