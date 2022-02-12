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

def get_torque(in_list, side=None):
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


def get_torque(in_list, side=None):
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

def can_balance(items):
    left_side_smaller = True
    start_point = 0
    while left_side_smaller and start_point <= len(items):
        if get_torque(items[:start_point], side="left") == \
                get_torque(items[start_point + 1:], side="right"):
            return start_point
        elif get_torque(items[:start_point], side="left") > \
                get_torque(items[start_point + 1:], side="right"):
            left_side_smaller = False
        start_point += 1
    else:
        return -1

# simple greedy version.
def give_change(amount, coins):
    r = []
    for coin in coins:
        n = amount // coin
        amount -= n * coin
        r.append([coin, ] * n)
    return [ y for x in r for y in x if len(x) > 0]

def riffle(items, out=True):
    if out:
        return [x for y in zip(items[:len(items)//2], items[len(items)//2:]) for x in y]
    else:
        return [x for y in zip( items[len(items)//2:], items[:len(items)//2]) for x in y]

def is_cyclops(in_value):
    left_side = 0
    right_side = 0
    eye_passed = False

    while (new_value := in_value // 10) > 0:
        tail = in_value % 10
        if tail == 0 and eye_passed:
            return "False"
            break
        elif tail == 0 and not eye_passed:
            eye_passed = True
        elif not tail == 0 and not eye_passed:
            right_side += 1
        elif not tail == 0 and eye_passed:
            left_side += 1
        in_value = new_value
    else:
        if not in_value % 10 == 0:
            left_side += 1

        if left_side == right_side:
            return "True"
        else:
            return "False"

def count_growlers(animals):
    the_dict = {"cat":0, "dog":0, "tac":0, "god":0}
    growling_count = 0

    for animal in animals:
        if (animal == "cat" or animal == "dog") and \
                the_dict["cat"] + the_dict["tac"] < the_dict["dog"] + the_dict["god"]:
            growling_count +=1
        the_dict[animal] +=1

    the_dict = {"cat":0, "dog":0, "tac":0, "god":0}

    for animal in animals[::-1]:
        if (animal == "tac" or animal == "god") and \
                the_dict["cat"] + the_dict["tac"] < the_dict["dog"] + the_dict["god"]:
            growling_count +=1
        the_dict[animal] +=1

    return growling_count

def extract_increasing(digits):
    current = int(digits[0])
    result = [current,]
    build = 0
    build_string = []
    for char in digits[1:]:
        build_string.append(char)
        build = int("".join(build_string))
        if build > current:
            result.append(build)
            current = build
            build = 0
            build_string.clear()
    return result

def winning_card(cards, trump=None):
    r = []
    ranks = {'two': 2, 'three': 3, 'four': 4, 'five': 5,
             'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
             'ten': 10, 'jack': 11, 'queen': 12, 'king': 13,
             'ace': 14}
    if not trump:
        trump = cards[0][1]
    for card in cards:
        if card[1] == trump:
            r.append((1, card[0], card[1]))
        else:
            r.append((0, card[0], card[1]))
    # print(r)
    return tuple(max(r, key=lambda x:(x[0], ranks[x[1]]))[1:])

