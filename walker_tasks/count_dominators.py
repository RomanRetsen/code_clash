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
        current = items[-1]
    else:
        counter = 0
    for i in range(len(items)-2, -1, -1):
        if items[i] > current:
            current = items[i]
            counter += 1
    return counter


# items = [int(x) for x in input().split()]
# items = range(10**7, 0, -1)
# items = [99]
# items = [42, 42, 42, 42]
# items = []
# items = [42, 7, 12, 9, 2, 5]
# items = range(10**7)
items = range(10**7, 0, -1)
print(count_dominators(items))