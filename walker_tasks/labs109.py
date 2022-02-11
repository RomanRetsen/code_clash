from itertools import product

def not_skipped(the_combination):
    the_steps = sorted([step_index[0] for step_index in the_combination])
    current = the_steps[0]
    if not current == 0:
        return False
    for i in range(1, len(the_steps), 1):
        if the_steps[i] - current > 1:
            return False
        else:
            current = the_steps[i]
    else:
        return True

def midnight(inlist):
    enriched_list = [[(index, y) for index, y in enumerate(x)] for x in inlist]
    the_max = 0
    for comb in product(*enriched_list):
        if 1 in (x[1] for x in comb) \
                and 4 in (x[1] for x in comb) \
                and sum([x[1] for x in comb])-1-4 > the_max \
                and not_skipped(comb):
            the_max = sum([x[1] for x in comb])- 1 - 4
    return the_max

def collapse_intervals(items):
    if not len(items):
        return ""
    return_list = []
    start = current = items[0]
    for number in items[1:]:
        if number - current == 1:
            current = number
        else:
            if start == current:
                return_list.append(start)
            else:
                return_list.append(f"{start}-{current}")
            start  = current = number
    else:
        if start == current:
            return_list.append(start)
        else:
            return_list.append(f"{start}-{current}")
    return ",".join([str(x) for x in return_list])

def colour_trio(color):
    mixin = {frozenset("ry"):"b", frozenset("by"):"r", frozenset("br"):"y",
             frozenset("y"):"b", frozenset("b"):"b", frozenset("r"):"r",
             frozenset("yy"):"y", frozenset("bb"):"b", frozenset("rr"):"r",
             }
    new_color = []
    while len(color) > 1:
        for i in range(0, len(color)-1):
            new_color.append(mixin[frozenset(color[i:i+2])])
        color = "".join(new_color)
        new_color.clear()
    return color

def count_dominators(items):
    if len(items) > 0:
        counter = 1
        items_reversed = list(reversed(items))
        current = items_reversed[0]
    else:
        counter = 0
    for i in range(1, len(items)):
        if items_reversed[i] > current:
            current = items_reversed[i]
            counter += 1
    return counter

def only_odd_digits(n):
    while (new_n := n // 10) > 0:
        if n % 10 % 2 == 0:
            return "False"
            break
        n = new_n
    else:
        if n % 10 % 2 == 0:
            return "False"
        else:
            return "True"

def expand_intervals(intervals):
    return_list = []
    for iterval in intervals.split(","):
        if not iterval.find("-") == -1:
            start, end = [int(x) for x in iterval.split("-")]
            return_list.extend(range(start, end + 1))
        elif iterval:
            return_list.append(int(iterval))
    return return_list

def pancake_scramble(text):
    the_list = list(text)
    for i in range(2, len(text) + 1):
        start_temp = list(reversed(the_list[:i]))
        end_temp = the_list[i:]
        the_list.clear()
        the_list = start_temp + end_temp
    return "".join(the_list)

def taxi_zum_zum(moves):
    current_location = [0, 0]
    current_vector = "N"
    move_adjust = {"N": (0,1), "S": (0,-1), "E":(1, 0), "W":(-1, 0)}
    vector_adjust = {"L":{"N":"W", "S":"E", "E":"N", "W":"S"}, "R":{"N":"E", "S":"W", "E":"S", "W":"N"}}

    for move in moves:
        if move == "F":
            current_location[0] += move_adjust[current_vector][0]
            current_location[1] += move_adjust[current_vector][1]
        elif move in vector_adjust.keys():
            current_vector = vector_adjust[move][current_vector]
    return tuple(current_location)

def domino_cycle(tiles):
    head = tail = None
    for i in tiles:
        x, y =  i
        if head is not None and tail is not None and not tail == x:
            return "False"
            break
        elif head is None and tail is None:
            head = x
            tail = y
        else:
            tail = y
    else:
        if head == tail:
            return 'True'
        else:
            return "False"


def get_torch(in_list, side=None):
    s = 0
    if side == "right":
        for multiplier, value in enumerate(in_list, 1):
            s += multiplier * value
    elif side == "left":
        for multiplier, value in enumerate(reversed(in_list), 1):
            s += multiplier * value
    else:
        s = -1
    return s

# the_list = [6, 1, 10, 5, 4]  # output 2
# the_list = [10, 3, 3, 2, 1] # output 1
# the_list = [7, 3, 4, 2, 9, 7, 4] # output -1
# the_list = [randint(1, 200) for _ in range(10000)] # 10000 elements list takes 10 sec. to process
the_list = [42]

left_side_smaller = True
start_point = 0
while left_side_smaller and start_point <= len(the_list):
    if get_torch(the_list[:start_point], side="left") == \
            get_torch(the_list[start_point + 1:], side="right"):
        print(start_point)
        break
    elif get_torch(the_list[:start_point], side="left") > \
            get_torch(the_list[start_point + 1:], side="right"):
        left_side_smaller = False
    start_point += 1
else:
    print(-1)

