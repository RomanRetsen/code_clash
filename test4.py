def is_attacked(x, y, board, N):
    l = len(board)
    if any([i for i  in board[x]]):
        return True
    if any([i[y] for i in board]):
        return True
    for correction_x, correction_y in ((1, 1), (-1, -1), (1, -1), (-1, 1)):
        c_x = x + correction_x
        c_y = y + correction_y
        while c_x >= 0 and c_x < l \
            and c_y >= 0 and c_y < l:
            if board[c_x][c_y] == True:
                return True
            c_x += correction_x
            c_y += correction_y
    return False

def queen_func(board, N):
    if N == 0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            if is_attacked(i, j, board, N):
                continue
            # print(f"placing at {(i,j)}")
            board[i][j] = True
            print(board)
            if queen_func(board, N-1) == True:
                return True
            board[i][j] = False
    return False

# board = [[0, 1, 0, 0],
         # [0, 0, 0, 1],
         # [1, 0, 0, 0],
         # [0, 0, 1, 0]]

board = [[0 for _ in range(4)] for _ in range(4)]
print(board)
print(queen_func(board, 4))
print(board)
