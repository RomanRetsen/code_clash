'''
Given a file that contains a set of command to navigate through a maze (R2, L3; meaning rotate 90 deg right and move forward 2 tiles,
then rotate left 90 deg and move forward 3 tiiles),
calculate the manhattan distance between the end and the start.
'''

all_direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
current_direction = (1, 0)
start_point = [0, 0]
file = open(r"C:\Container\Downloads\s3_e2.txt")
moves = file.readline().strip().split(", ")
for move in moves:
    turn = move[:1]
    t_value = int(move[1:])
    current_dir_index = all_direction.index(current_direction)
    new_dir_index = None
    if turn == "R":
        new_dir_index = (current_dir_index + 1) % 4
    elif turn == "L":
        new_dir_index = (current_dir_index + 3) % 4
    current_direction = all_direction[new_dir_index]
    temp_x = current_direction[0] * t_value + start_point[0]
    temp_y = current_direction[1] * t_value + start_point[1]
    start_point[0] = temp_x
    start_point[1] = temp_y
    print(temp_x, temp_y, f"current pos {start_point}")

print(start_point)
print(sum([abs(x) for x in start_point]))
file.close()