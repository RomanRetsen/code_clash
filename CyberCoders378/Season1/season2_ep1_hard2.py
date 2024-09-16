"""
A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.
This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.
Consider the same engine schematic again:
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345.
The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.)
Adding up all of the gear ratios produces 467835.
What is the sum of all of the gear ratios in your engine schematic?

Answer to large example - 79026871

"""

the_list = []

def populate_neighbors(key, the_numbers_dict, height, width):
    h, w , value = key
    num_len = len(str(value))
    if h > 0:
        for i in range(w, w + num_len):
            the_numbers_dict[key].append((h-1, i))
        if w > 0:
            the_numbers_dict[key].append((h-1, w-1))
        if w + num_len < width-1:
            the_numbers_dict[key].append((h-1, w+num_len))
    if h < height-1:
        for i in range(w, w + num_len):
            the_numbers_dict[key].append((h+1, i))
        if w  > 0:
            the_numbers_dict[key].append((h+1, w-1))
        if w + num_len < width-1:
            the_numbers_dict[key].append((h+1, w+num_len))
    if w  > 0:
        the_numbers_dict[key].append((h, w-1))
    if w + num_len < width-1:
        the_numbers_dict[key].append((h, w+num_len))

while True:
    one_line = input()
    if one_line == "":
        break
    else:
        the_list.append([x for x in one_line])

height = len(the_list)
width = len(the_list[0])
total = 0
the_gear_dict = {} # key - (h,w). value - list of numbers
the_numbers_dict = {} # key - (h,w, digit). value - list of neighbors
single_number_holder = []
h = 0

while h < height:
    w = 0
    while w < width:
        if the_list[h][w] == "*":
            the_gear_dict[(h,w)] = []
        elif the_list[h][w].isdigit():
            number_w_start = w
            single_number_holder.append(the_list[h][w])
            w += 1
            while w < width:
                if the_list[h][w].isdigit():
                    single_number_holder.append(the_list[h][w])
                    w += 1
                else:
                    digit_to_insert = int("".join(single_number_holder))
                    the_numbers_dict[(h, number_w_start, digit_to_insert)] = []
                    populate_neighbors((h, number_w_start, digit_to_insert), the_numbers_dict, height, width)
                    single_number_holder.clear()
                    w -= 1
                    break
            else:
                digit_to_insert = int("".join(single_number_holder))
                the_numbers_dict[(h, number_w_start, digit_to_insert)] = []
                populate_neighbors((h, number_w_start, digit_to_insert), the_numbers_dict, height, width)
                single_number_holder.clear()
        w += 1
    h += 1

for gear in the_gear_dict:
    for number in the_numbers_dict:
        if gear in the_numbers_dict[number]:
            the_gear_dict[gear].append(number[2])
    if len(the_gear_dict[gear]) > 1:
        total += the_gear_dict[gear][0] * the_gear_dict[gear][1]

# print(f"the_list {the_list}")
# print(f"gears {the_gear_dict}")
# print(f"numbers {the_numbers_dict}")
print(total)


