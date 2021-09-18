n = 8
def is_safe(x, y, board):
    if (x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False

def print_solution(n, board):
    for i in range(n):
        for y in range(n):
            print(board[i][y], end=" ")
        print()

def solve_kt(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    print(board)
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    possible_moves = zip(move_x, move_y)
    board[0][0] = 0

    pos = 1
    if (not solve_kt_util(n, board, 0, 0, move_x, move_y, pos)):
        print("Solution does not exist")
    else:
        print_solution(n, board)

def solve_kt_util(n, board, curr_x, curr_y, move_x, move_y, pos):
    print(f'-----------------------')
    print(f'Pos is {pos}')
    print(f'board {board}')
    print(f'-----------------------')
    if pos == 200:
        return True

    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if is_safe(new_x, new_y, board):
            board[new_x][new_y] = pos
            solve_kt_util(n, board, new_x, new_y, move_x, move_y, pos+1)
            # if solve_kt_util(n, board, new_x, new_y, move_x, move_y, pos+1):
            #     return True
            # board[new_x][new_y] = -1
    # return False
    return True



solve_kt(8)