import re


def do_toggle(all_parts, the_grid):
    start = all_parts[1].split(",")
    start_x_orig = int(start[0])
    start_y_orig = int(start[1])
    end = all_parts[3].split(",")
    end_x_orig = int(end[0])
    end_y_orig = int(end[1])

    start_x = start_x_orig
    start_y = start_y_orig
    while start_y <= end_y_orig:
        start_x = start_x_orig
        while start_x <= end_x_orig:
            the_grid[start_y][start_x] ^= 1
            start_x += 1
        start_y += 1

def do_turn_on(all_parts, the_grid):
    start = all_parts[2].split(",")
    start_x_orig = int(start[0])
    start_y_orig = int(start[1])
    end = all_parts[4].split(",")
    end_x_orig = int(end[0])
    end_y_orig = int(end[1])

    start_x = start_x_orig
    start_y = start_y_orig
    while start_y <= end_y_orig:
        start_x = start_x_orig
        while start_x <= end_x_orig:
            the_grid[start_y][start_x] = 1
            start_x += 1
        start_y += 1

def do_turn_off(all_parts, the_grid):
    start = all_parts[2].split(",")
    start_x_orig = int(start[0])
    start_y_orig = int(start[1])
    end = all_parts[4].split(",")
    end_x_orig = int(end[0])
    end_y_orig = int(end[1])

    start_x = start_x_orig
    start_y = start_y_orig
    while start_y <= end_y_orig:
        start_x = start_x_orig
        while start_x <= end_x_orig:
            the_grid[start_y][start_x] = 0
            start_x += 1
        start_y += 1

def do(the_grid):
    with open(r"C:\Container\Downloads\3.txt") as file:
        for operation in file:
            all_parts = operation.strip().split()
            if all_parts[0] == "toggle":
                do_toggle(all_parts, the_grid)
            elif all_parts[0] == "turn" and all_parts[1] == "on":
                do_turn_on(all_parts, the_grid)
            elif all_parts[0] == "turn" and all_parts[1] == "off":
                do_turn_off(all_parts, the_grid)
            else:
                print("Something if off!!!!!!!!!!!!!!!!!!!!!!!!")

if __name__ == "__main__":
    the_grid = [[0 for _ in range(1000)] for _ in range(1000)]
    do(the_grid)
    with open("ressult.txt", "w") as file:
        for i in range(1000):
            file.write("".join([str(x) for x in the_grid[i]]) + "\n")
            # print(*the_grid[i], sep="")
    counter = 0
    for i in range(1000):
        for y in range(1000):
            if the_grid[i][y]:
                counter += 1
    print(f"Counter {counter}")