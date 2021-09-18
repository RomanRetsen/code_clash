import math
from random import randint
from time import time


counter = 0

def max_sum_path(input_matrix, visited_matrix, sum_matrix, x, y):
    global  counter
    counter += 1
    matrix_width = len(input_matrix[0])
    matrix_height = len(input_matrix)

    #reached end of path/maze
    if x == matrix_height-1  and y == matrix_width -1:
        return input_matrix[x][y]

    #this prevent redantent calculation.
    if visited_matrix[x][y]:
        return sum_matrix[x][y]

    visited_matrix[x][y] = True

    total_sum = sum_matrix[x][y]
    if x < (matrix_height - 1) and  y < (matrix_width - 1):
        current_sum = max (max_sum_path(input_matrix, visited_matrix, sum_matrix, x, y + 1),
                           max_sum_path(input_matrix, visited_matrix, sum_matrix, x + 1, y + 1),
                           max_sum_path(input_matrix, visited_matrix, sum_matrix, x + 1, y))
        total_sum = input_matrix[x][y] + current_sum
    elif x == matrix_height - 1:
        total_sum = input_matrix[x][y] \
                    + max_sum_path(input_matrix, visited_matrix, sum_matrix, x, y + 1)
    elif y == matrix_width - 1:
        total_sum = input_matrix[x][y] \
                    + max_sum_path(input_matrix, visited_matrix, sum_matrix, x + 1, y)

    sum_matrix[x][y] = total_sum
    return total_sum

def max_sum_path2(input_matrix, sum_matrix):
    sum_matrix[0][0] = input_matrix[0][0]

    matrix_width = len(input_matrix[0])
    matrix_height = len(input_matrix)

    for i in range(1, matrix_height):
        sum_matrix[i][0] = sum_matrix[i-1][0] + input_matrix[i][0]
    for i in range(1, matrix_width):
        sum_matrix[0][i] = sum_matrix[0][i-1] + input_matrix[0][i]

    for i in range(1, matrix_height):
        for y in range(1, matrix_width):
            sum_matrix[i][y] = max(sum_matrix[i][y-1], sum_matrix[i-1][y]) + input_matrix[i][y]

    return sum_matrix[matrix_height-1][matrix_width-1]

if __name__ == "__main__":
    ##############pre-setup######################################################
    input_matrix = [[randint(50,1000) for _ in range(10)] for _ in range(10)]

    print(*["--".join([str(x) for x in y]) for y in input_matrix], sep="\n")
    matrix_width = len(input_matrix[0])
    matrix_height = len(input_matrix)
    visited_matrix = [[False for _ in range(matrix_width)] for _ in range(matrix_height)]
    total_sum_matrix = [[-math.inf for _ in range(matrix_width)] for _ in range(matrix_height)]
    ################################################################################
    t0 = time()
    max_value = max_sum_path(input_matrix, visited_matrix, total_sum_matrix, 0, 0)
    t1 = time()
    print(*["--".join([str(x) for x in y]) for y in total_sum_matrix], sep="\n")
    print(*["--".join([str(x) for x in y]) for y in visited_matrix], sep="\n")
    print(f'max_value for vertion 1: {max_value}')
    print(f'Global counter function1: {counter}')
    print(f'Time taken for version 1 {t1-t0}')
    #################################################################################

    total_sum_matrix.clear()
    total_sum_matrix = [[-math.inf for _ in range(matrix_width)] for _ in range(matrix_height)]
    t2 = time()
    max_value = max_sum_path2(input_matrix, total_sum_matrix)
    t3 = time()
    print(*["--".join([str(x) for x in y]) for y in total_sum_matrix], sep="\n")
    print(f'max_value for vertion 2: {max_value}')
    print(f'Time taken for version 2 {t3-t2}')
