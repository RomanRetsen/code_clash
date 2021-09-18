points = {0:10, 1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3, 9: 2, 10: 1}



print(points)
n = int(input())
for i in range(n):
    player_points = 0
    for i in range(5):
        x, y = [int(j) for j in input().split()]
        distance = round(( ((x**2) + (y**2)) ** 0.5) + 0.49)
        # print(distance)
        player_points += 0 if distance > 10 else  points[distance]
    print(player_points)


# Line 1: An integer N, number of archers.
# Next 5*N lines: Integers x and y (coordinates of shot).
# Note: Remember that every archer has five shots.
# Output
# N lines: Number of points of archers, a new line for each of them.
# Constraints
# 1≤N ≤10
# 0≤ x ≤ 20
# 0≤ y ≤ 20
#
#
#
# 2
# 2 3
# 5 7
# 10 7
# 5 6
# 7 7
# 2 3
# 6 6
# 1 2
# 5 1
# 7 7
#
#
# 13
# 23
# _______________
#
# 2
# 0 0
# 1 1
# 2 2
# 3 3
# 4 4
# 5 5
# 6 6
# 7 7
# 8 8
# 9 9
#
#
# 38
# 6
#
#
# _______________
#
#
# 4
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 2 1
# 2 2
# 2 3
# 2 4
# 2 5
# 3 1
# 3 2
# 3 3
# 3 4
# 3 5
# 4 1
# 4 2
# 4 3
# 4 4
# 4 5
#


35
34
31
27
