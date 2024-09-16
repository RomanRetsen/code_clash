import sys
import math

def detect_distance(x1,y1, x2, y2, the_grid):
    return ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5

def re_scan_grid_warmer_colder(x0, y0, x1, y1, the_grid):
    height = len(the_grid)
    width = len(the_grid[0])
    min_x = min_y = math.inf
    max_x = max_y = -math.inf
    for h in range(height):
        for w in range(width):
            if the_grid[h][w] == 0 and \
                    detect_distance(w, h, x0, y0, the_grid) < detect_distance(w, h, x1, y1, the_grid):
                the_grid[h][w] = 1
            elif the_grid[h][w] == 0 :
                if min_x == math.inf:
                    min_x = w
                    min_y = h
                elif max_x < w or max_y < h:
                    max_x = w
                    max_y = h
    print(f"{min_x}-{max_x}==={min_y}-{max_y}")
    return ((min_x + max_x)//2, (min_y + max_y)//2)

def re_scan_grid_same(x0, y0, x1, y1, the_grid):
    height = len(the_grid)
    width = len(the_grid[0])
    min_x = min_y = math.inf
    max_x = max_y = -math.inf
    for h in range(height):
        for w in range(width):
            if the_grid[h][w] == 0 and \
                    not detect_distance(w, h, x0, y0, the_grid) == detect_distance(w, h, x1, y1, the_grid):
                the_grid[h][w] = 1
            elif the_grid[h][w] == 0 :
                if min_x == math.inf:
                    min_x = w
                    min_y = h
                elif max_x < w or max_y < h:
                    max_x = w
                    max_y = h
    return ((min_x + max_x)//2, (min_y + max_y)//2)



w, h = 10, 10
n = 6
x0, y0 = 2, 5
the_grid = [[0 for _ in range(w)] for _ in range(h)]
x1, y1 = x0, y0

while True:
    bomb_dir = input()
    if bomb_dir == "UNKNOWN":
        x1, y1 = w-x0-1, h-y0-1
        print(f"{x1} {y1}")
    elif bomb_dir == "WARMER":
        next_x1, next_y1 = re_scan_grid_warmer_colder(x0, y0, x1, y1, the_grid)
        x0, y0 = x1, y1
        x1, y1 = next_x1, next_y1
        print(x1, y1)
        print(*the_grid, sep="\n")
    elif bomb_dir == "COLDER":
        next_x1, next_y1 = re_scan_grid_warmer_colder(x1, y1, x0, y0, the_grid)
        x1, y1 = next_x1, next_y1
        print(x1, y1)
        print(*the_grid, sep="\n")
    elif bomb_dir == "SAME":
        x1, y1 = re_scan_grid_same(x0, y0, x1, y1, the_grid)
        print(x1, y1)
        print(*the_grid, sep="\n")
