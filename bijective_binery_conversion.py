import math

def bijective_to_int (bijective : str) -> int:
    total = 0
    n_str = str(bijective)[::-1]
    for i in range(len(str(bijective))):
        total += int(n_str[i]) * (2 ** i)
    return total

# fast. left to right analysis
def int_to_bijective(n : int) -> str:
    if n == 0:
        return ""
    result = []
    level = int(math.log(n + 1, 2))
    while level > 0:
        left_over = n - 2 ** level
        if left_over  >= (2 ** (level - 1) - 1):
            result.append(2)
            n = left_over
        else:
            result.append(1)
            n = left_over + 2 ** (level - 1)
        level -= 1
    return "".join([str(x) for x in result])

#slow with use of recursion
def i_to_b_engine(n, level, bijective_sequence):
    # print(level)
    if n == 0:
        del bijective_sequence[len(bijective_sequence)-1]
        return True
    if n > 0:
        tmp = 2 ** level
        bijective_sequence[level] = 2
        # recursive call. trying 2
        if i_to_b_engine(n - (2 * tmp), level + 1, bijective_sequence):
            return True
        bijective_sequence[level] = 1
        # recursive call. trying 1
        if i_to_b_engine(n - tmp, level + 1, bijective_sequence):
            return True
    return False

def int_to_bijective_slow(n : int) -> str:
    if n == 0:
        return ""
    bijective_sequence = [0 for _ in range(int(math.log(n + 1, 2)) + 1)]
    if i_to_b_engine(n, 0, bijective_sequence):
        return "".join(str(x) for x in bijective_sequence[::-1])


