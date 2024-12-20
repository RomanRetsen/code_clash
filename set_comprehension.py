
# Input
# Line 1: An integer N representing the size of the grids
# Next N Lines: A string containing exactly N characters representing the first grid, each character will be either '.', '/' or '\'.
# Next Line: Empty line
# Next N Lines: A string containing exactly N characters representing the second grid, each character will be either '.', '/' or '\'.
# Output
# N Lines with exactly N characters in each line, which are the description of the output grid as described above. Each character should be either '.', '/', '\' or 'X'.
# Example
# Input
#
# 3
# //.
# ./.
# /./
#
# /.\
# ./.
# \/\
#
# Output
#
# //\
# ./.
# X/X



q=input
n = int(q())
original_grid = []
for i in range(n):
    row = q()
    original_grid.append(row)

empty_line = input()
second_grid = []
for i in range(n):
    row2 = q()
    second_grid.append(row2)

#short version not not very verbose
for i in range(n):
    print(''.join(['X' if len(set(x+y)-set('.')) == 2 else (set(x+y)-set('.')).pop() if len((set(x+y)-set('.'))) == 1 else '.' for x,y in zip(original_grid[i], second_grid[i])]))

# long loop version but bit more verbose

# for i in range(n):
#     for in_set in ([set(a + b) for a,b in zip(original_grid[i], second_grid[i])]):
#         if len(in_set) == 1:
#             print(*in_set, end='')
#         elif len(in_set) == 2 and '.' not in in_set:
#             print('X', end='')
#         else:
#             print(*(in_set - set('.')), end='')
#     print()
