'''
this method works but not efficient. Simple brute force iteration.
10000 elements list takes 10 sec to process.
'''
from random import randint


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