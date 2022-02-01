size_of_maze = 7

def print_solution(solution_matrix):
    for i in range(size_of_maze):
        for y in range(size_of_maze):
            sm_to_int = int(solution_matrix[i][y])
            if sm_to_int == 0:
                print("\033[1;37;40m0", end=" ")
            elif sm_to_int == 1:
                print("\033[1;37;46m1", end=" ")
            elif sm_to_int == 2:
                print("\033[1;37;41m1", end=" ")

        print("\033[1;37;47m")

def is_valid(maze_matrix, x, y):
    if x >= 0 and y >= 0 and x < size_of_maze and y < size_of_maze and maze_matrix[x][y] == 1:
        return True
    return False

def find_path(maze_matrix):
    solution_matrix = [[0 for _ in range(size_of_maze)] for _ in range(size_of_maze)]
    if make_step(maze_matrix, 0, 0, solution_matrix):
        print_solution(solution_matrix)
        return True
    else:
        print("Can't find way out")
        return False

def make_step(maze_matrix, pos_x, pos_y, solution_matrix):
    print(f'____________{pos_x}:{pos_y}__________')
    print_solution(solution_matrix)
    print('______________________')
    if pos_x == 0 and pos_y == 6 and maze_matrix[pos_x][pos_y] == 1:
        solution_matrix[pos_x][pos_y] = 1
        return True

    if is_valid(maze_matrix, pos_x, pos_y):
        print(f'Valid x;y {pos_x}:{pos_y}')
        if solution_matrix[pos_x][pos_y] == 1:
            return False
        solution_matrix[pos_x][pos_y] = 1

        if make_step(maze_matrix, pos_x+1, pos_y, solution_matrix):
            return True
        if make_step(maze_matrix, pos_x, pos_y+1, solution_matrix):
            return True
        if make_step(maze_matrix, pos_x-1, pos_y, solution_matrix):
            return True
        if make_step(maze_matrix, pos_x, pos_y-1, solution_matrix):
            return True

        # print(f'Backtracking x {pos_x}- y {pos_y}')
        solution_matrix[pos_x][pos_y] = 2
        return False


    return False



if __name__ == "__main__":
    maze = [ [1, 0, 0, 0, 0, 0, 1],
             [1, 1, 0, 1, 0, 1, 1],
             [0, 1, 0, 0, 0, 1, 0],
             [1, 1, 1, 1, 0, 1, 0],
             [1, 0, 0, 0, 0, 1, 0],
             [1, 0, 0, 0, 0, 1, 0],
             [1, 1, 1, 1, 1, 1, 1] ]

    find_path(maze)
