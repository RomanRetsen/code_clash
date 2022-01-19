'''
Domino cycle
def domino_cycle(tiles):
A single domino tile is represented as a two-tuple of its pip values, such as (2,5) or (6,6). This
function should determine whether the given list of tiles forms a cycle so that each tile in the list
ends with the exact same pip value that its successor tile starts with, the successor of the last tile
being the irst tile of the list since this is supposed to be a cycle instead of a chain. Return True if
the given list of tiles forms such a cycle, and False otherwise.
tiles Expected result
[(3, 5), (5, 2), (2, 3)] True
[(4, 4)] True
[] True
[(2, 6)] False
[(5, 2), (2, 3), (4, 5)] False
[(4, 3), (3, 1)] False

'''

n = int(input())

head = tail = None
for i in range(n):
    x,y = [int(x) for x in input().split()]
    if head is not None and tail is not None and not tail == x:
        print("False")
        break
    elif head is None and tail is None:
        head = x
        tail = y
    else:
        tail = y
else:
    if head == tail:
        print('True')
    else:
        print("False")