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
