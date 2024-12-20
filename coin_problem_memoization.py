import math
import sys

coins = [1,3,4]

def solve(x, ready, value):
    if x < 0:
        return math.inf
    elif x == 0:
        return 0
    elif ready[x]:
        return value[x]
    else:
        best = math.inf
        for coin in coins:
            best = min(best, solve(x-coin, ready, value) + 1)
    ready[x] = True
    value[x] = best
    return best

def start_search(x):
    ready = [False for _ in range(x + 1)]
    value = [math.inf for _ in range(x + 1)]
    return solve(x, ready, value)

def solve_with_memoization(coins, the_number):
    store_table = [0 if i == 0 else sys.maxsize for i in range(the_number + 1)]
    for current_number in range(1, the_number + 1):
        for coin in coins:
            if coin <= current_number:
                sub_val = store_table[current_number - coin]
                if not sub_val == sys.maxsize and sub_val < store_table[current_number]:
                    store_table[current_number] = sub_val + 1
        print(store_table)

    if store_table[the_number] == sys.maxsize:
        return -1
    return store_table[the_number]



print(start_search(10))
print(solve_with_memoization(coins, 10))
