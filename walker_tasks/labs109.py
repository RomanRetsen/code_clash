from itertools import product
import operator
import math

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
        current = items[-1]
    else:
        counter = 0
    for i in range(len(items)-2, -1, -1):
        if items[i] > current:
            current = items[i]
            counter += 1
    return counter

def group_and_skip(n, out, ins):
    recording_list = []
    while (piles:= n // out) > 0:
        recording_list.append(n % out)
        n = ins * piles
    else:
        recording_list.append(n % out)
    return recording_list

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

def reverse_ascending_sublists(items):
    if len(items) == 0:
        return []
    else:
        result = []
        temp = [items[0], ]
        current = items[0]
        for item in items[1:]:
            if item > current:
                temp.append(item)
                current = item
            else:
                result.extend(reversed(temp))
                temp.clear()
                temp.append(item)
                current = item
        else:
            if len(temp):
                result.extend(reversed(temp))
    return result

def josephus(n, k):
    return_sequence = []
    # zealot_circle = deque(range(1, n + 1), maxlen=n)
    zealot_circle = list(range(1, n + 1))
    for i in range(n):
        killed = (k - 1) % len(zealot_circle)
        return_sequence.append(zealot_circle[killed])
        left_side = zealot_circle[killed + 1:]
        right_side = zealot_circle[:killed]
        zealot_circle = left_side + right_side
    return return_sequence

def recaman_item(n):
    if n == 0:
        return 1
    recaman_seq = [1,]
    # power of set!!! if list is used to check existance with 'in' operator
    # code become quite inefficient
    check_set = {1,}
    for i in range(1, n):
        possible_new_value = recaman_seq[i-1] - (i + 1)
        if possible_new_value > 0 and not possible_new_value in check_set:
            recaman_seq.append(possible_new_value)
            check_set.add(possible_new_value)
        else:
            new_value = recaman_seq[i-1] + (i + 1)
            recaman_seq.append(new_value)
            check_set.add(new_value)
    return recaman_seq[-1]

def generate_all_categories():
    all_categories = {(1, 50): set(), (2, 26): set(), (3, 25): set(), \
                      (4, 20):set(), (5, 20):set(), (6, 20):set(), (7, 20): set(), \
                      (8, 18): set(), (9, 12): set(), (10, 6): set(), \
                      (11, 15): set(), (12, 10): set(), (13, 5): set(), \
                      (14, 12): set(), (15, 8): set(), (16, 4): set(), \
                      (17, 9): set(), (18, 6): set(), (19, 3): set(), \
                      (20, 6): set(), (21, 4): set(), (22, 2): set(), \
                      (23, 3): set(), (24, 2): set(), (25, 1): set()
                      }
    for comb in product([1,2,3,4,5,6], repeat=3):
        sorted_comb = tuple(sorted(comb))
        if sum(comb) == 13:
            if len(set(comb)) == 2:
                all_categories[(1,50)].add(sorted_comb)
            all_categories[(2, 26)].add(sorted_comb)
        if len(set(comb)) == 1:
            all_categories[(3, 25)].add(sorted_comb)
        if sorted_comb == (1,2,3):
            all_categories[(4, 20)].add(sorted_comb)
        if sorted_comb == (4,5,6):
            all_categories[(5, 20)].add(sorted_comb)
        if sorted_comb == (1,3,5):
            all_categories[(6, 20)].add(sorted_comb)
        if sorted_comb == (2,4,6):
            all_categories[(7, 20)].add(sorted_comb)
        if sorted_comb.count(6) == 3:
            all_categories[(8, 18)].add(sorted_comb)
        elif sorted_comb.count(6) == 2:
            all_categories[(9, 12)].add(sorted_comb)
        elif sorted_comb.count(6) == 1:
            all_categories[(10, 6)].add(sorted_comb)
        if sorted_comb.count(5) == 3:
            all_categories[(11, 15)].add(sorted_comb)
        elif sorted_comb.count(5) == 2:
            all_categories[(12, 10)].add(sorted_comb)
        elif sorted_comb.count(5) == 1:
            all_categories[(13, 5)].add(sorted_comb)
        if sorted_comb.count(4) == 3:
            all_categories[(14, 12)].add(sorted_comb)
        elif sorted_comb.count(4) == 2:
            all_categories[(15, 8)].add(sorted_comb)
        elif sorted_comb.count(4) == 1:
            all_categories[(16, 4)].add(sorted_comb)
        if sorted_comb.count(3) == 3:
            all_categories[(17, 9)].add(sorted_comb)
        elif sorted_comb.count(3) == 2:
            all_categories[(18, 6)].add(sorted_comb)
        elif sorted_comb.count(3) == 1:
            all_categories[(19, 3)].add(sorted_comb)
        if sorted_comb.count(2) == 3:
            all_categories[(20, 6)].add(sorted_comb)
        elif sorted_comb.count(2) == 2:
            all_categories[(21, 4)].add(sorted_comb)
        elif sorted_comb.count(2) == 1:
            all_categories[(22, 2)].add(sorted_comb)
        if sorted_comb.count(1) == 3:
            all_categories[(23, 3)].add(sorted_comb)
        elif sorted_comb.count(1) == 2:
            all_categories[(24, 2)].add(sorted_comb)
        elif sorted_comb.count(1) == 1:
            all_categories[(25, 1)].add(sorted_comb)
    return all_categories

def crag_score(dice):
    sorted_dice = tuple(sorted(dice))
    for category_result, category_combinations \
            in sorted(generate_all_categories().items(), key=lambda x:x[0][1], reverse=True):
        if sorted_dice in category_combinations:
            return category_result[1]
    else:
        return 0
    
def sum_of_two_squares(n):
    if n == 1:
        return None
    if (start := math.floor(n ** 0.5)) == n ** 0.5:
        start -= 1
    for i in range(start, start//2, -1):
        end = n-i ** 2
        if (i ** 2 + math.floor(end ** 0.5) ** 2) == n:
            return (i, math.floor(end ** 0.5))
    else:
        return None

def winning_card(cards, trump=None):
    r = []
    ranks = {'two': 2, 'three': 3, 'four': 4, 'five': 5,
             'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
             'ten': 10, 'jack': 11, 'queen': 12, 'king': 13,
             'ace': 14}
    if not trump or trump not in {x[1] for x in cards}:
        trump = cards[0][1]
    for card in cards:
        if card[1] == trump:
            r.append((1, card[0], card[1]))
        else:
            r.append((0, card[0], card[1]))
    return tuple(max(r, key=lambda x:(x[0], ranks[x[1]]))[1:])

def postfix_evaluate(items):
    operational_stack = []
    operations = {"+":operator.add, "-":operator.sub, \
                  "/":operator.floordiv, "*":operator.mul
                  }
    for item in items:
        if item in operations:
            operand_2 = operational_stack.pop()
            operand_1 = operational_stack.pop()
            if item == "/" and operand_2 == 0:
                operational_stack.append(0)
            else:
                operational_stack.append(
                    operations[item](operand_1, operand_2)
            )
        elif str(item).isdigit():
            operational_stack.append(item)
    if len(operational_stack) == 1: # it could be only one left-over item in the list
        return operational_stack[0]
    else:
        return 0
