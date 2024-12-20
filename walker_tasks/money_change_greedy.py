def give_change_greedy(amount, coins):
    r = []
    for coin in coins:
        n = amount // coin
        amount -= n * coin
        r.append([coin, ] * n)
    return [ y for x in r for y in x if len(x) > 0]

amount = int(input())
coins = [int(x) for x in input().split()]
print(give_change_greedy(amount, coins))