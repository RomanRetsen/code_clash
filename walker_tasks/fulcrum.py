'''
this method works but not efficient. Simple brute force iteration.
10000 elements list takes 10 sec to process.
'''
from random import randint

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


items = [6, 1, 10, 5, 4]  # output 2
# items = [10, 3, 3, 2, 1] # output 1
# items = [7, 3, 4, 2, 9, 7, 4] # output -1
# items = [randint(1, 200) for _ in range(10000)] # 10000 elements list takes 10 sec. to process
# items = [42]
print(can_balance(items))