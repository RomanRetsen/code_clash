N = 4



def print_solution(board):
    for i in range(len(board)):
        for y in range(len(board)):
            print(board[i][y], end=" ")
        print()

def is_valid(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
        for i, y in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][y] == 1:
                return False

        for i, y in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][y] == 1:
                return False
    return True



def solve_util(board, start_col):
    print("-----------")
    print_solution(board)
    print("-----------")
    if start_col >= N:
        return True

    for i in range(N):
        if is_valid(board, i, start_col):
            board[i][start_col] = 1

            if solve_util(board, start_col + 1):
                return True

            board[i][start_col] = 0

    return False


def solve_ng():
    board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0] ]

    if solve_util(board, 0) == False:
        print("Solution does not exist")
        return False

    print_solution(board)
    return True

solve_ng()