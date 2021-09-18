from itertools import combinations

#knapsack problem
#recusrsion & memoization solutions

val = [60, 61, 100, 120, 200]
wt = [10, 20, 20, 30, 60]
W = 50
n = len(val)
t = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
print(*t, sep='\n')

def knapsack(W, wt, val, n):
    if W == 0 or n == 0:
        return 0
    if not t[n][W] == -1:
        return t[n][W]

    if wt[n - 1] <= W:
        t[n][W] =  max(val[n - 1] + knapsack(W-wt[n - 1], wt, val, n- 1),
                   knapsack(W, wt, val, n-1))
        return  t[n][W]
    else:
        t[n][W] = knapsack(W, wt, val, n - 1)
        print(f"tnw {t[n][W]}")
        return t[n][W]

print(knapsack(W, wt, val, n))
print(*t, sep='\n')


#knapsack problem
#recusrsion & memoization solutions

current_max = -1
for j in range(0, len(wt) + 1, 1):
    for x in combinations(zip(wt, val), r=j):
        if sum([a[0] for a in x]) <= W and sum([a[1] for a in x]) > current_max:
            current_max = sum([a[1] for a in x])

print(current_max)

"""
#knapsack problem solved with prone to mistakes.
# for instance 800 will produce 500 + 100 + 100 + 100
#must be 400 + 400

bills = {500:0, 400:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
_sum = int(input())

for bill in bills:
    if _sum >= bill and _sum > 0:
        bills[bill] = _sum // bill
        _sum -= bills[bill] * bill
    elif _sum == 0:
        break

print(*bills.values(), sep="\n")
"""


"""
#lnapsack problem solved using memoization

# USD - $1, $5, $10, etc.
currency = [1, 2, 5, 10, 20, 50, 100, 400, 500]

# the amount to change - $120
amount = int(input())

# initialize arrays for $0
minimum_number_of_currency = [0]
currency_composition = [[]]

for i in range(1, amount + 1):
    best = 10000
    best_currency_composition = None

    for j in currency:
        if i - j > -1 and minimum_number_of_currency[i - j] + 1 < best:
            best = minimum_number_of_currency[i - j] + 1
            best_currency_composition = currency_composition[i - j] + [j]

    minimum_number_of_currency.append(best)
    currency_composition.append(best_currency_composition)

    print('{0:3} {1} {2}'.format(i, best, best_currency_composition))
"""