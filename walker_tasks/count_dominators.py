'''

-----------------------test 1
42 7 12 9 2 5
output
4
----------------------test2
42 42 42 42
output
1

'''
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

items = [int(x) for x in input().split()]
# items = range(10**7, 0, -1)
print(count_dominators(items))