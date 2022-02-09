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

the_list = [[3, 4, 6, 6, 6, 2], [3, 2, 6, 2, 3, 3], [2, 2, 2, 2, 2, 3],
            [6, 1, 4, 2, 2, 2], [2, 2, 2, 3, 2, 3], [2, 3, 3, 3, 3, 2]] # 14
# the_list = [[2, 6, 2, 1, 3, 3], [2, 2, 2, 2, 2, 3], [2, 2, 4, 3, 6, 6],
#             [4, 5, 6, 3, 2, 5], [2, 4, 2, 6, 5, 3], [2, 2, 2, 2, 2, 3]] # 17
# the_list = [[2, 3, 5, 3, 2, 2], [1, 3, 2, 3, 6, 4], [3, 2, 3, 3, 3, 5],
#             [3, 6, 4, 6, 2, 3], [2, 3, 3, 2, 3, 2], [3, 5, 3, 5, 1, 2]] # 17
# the_list = [[2, 6, 2, 5, 2, 5], [5, 3, 3, 2, 5, 3], [2, 2, 2, 2, 5, 2],
#             [3, 6, 3, 2, 2, 5], [6, 2, 2, 6, 3, 2], [2, 2, 3, 2, 2, 2]] # 0
print(midnight(the_list))