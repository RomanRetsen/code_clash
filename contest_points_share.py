# Line 1: An integer N for the number of problems
# Line 2: An integer C for the number of contestants
# Next C lines: A line for each contestant in order, starting with contestant 1. Each line is a string with a character for each problem, the character is an X if the problem is completed or an O if it is not.
# Output
# Line 1: The winning player and score separated with space
# Constraints
# 1 ≤ N ≤ 100
# 1 ≤ C ≤ 100
#
#
# test 1
# 10
# 8
# XXOOOXOOOO
# XXOOXXXOOO
# XOOXOOOOOO
# XXXXOOOXOO
# XXOXXOOOXX
# XOXXOXOOXX
# OXOXXOOXOX
# OOOOOOOXXX
#
# result
# 2 2033333
#
# test2
# 5
# 5
# XXOOX
# XOOOX
# XXXOO
# XXOOX
# XOXOX
# result:
# 3 1033333
#

n = int(input())
c = int(input())
players = {}
for i in range(c):
    row = input()
    players[i] = [x for x in row]
    players[i].append(0)
print(players)
for i in range(n):
    comp_result = [x[i] for x in players.values() if x[i] == 'X']
    shared_score = round(1000000 / len(comp_result))
    for y in players.keys():
        if players[y][i] == 'X':
            players[y][n] += shared_score

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
x,y = max(players.items(), key=lambda x:x[1][n])
print(x,y[n], sep=" ")

