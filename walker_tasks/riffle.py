'''
Rif e shuf e kerfuf e
def riffle(items, out=True):
Given a list of items whose length is guaranteed to be even (note that “oddly” enough, zero is an
even number), create and return a list produced by performing a perfect rif le to the items by
interleaving the items of the two halves of the list in an alternating fashion.
False [5, 1, 6, 2, 7, 3, 8, 4]
[] True []
['bob', 'jack'] True ['bob', 'jack']
['bob', 'jack'] False ['jack', 'bob']
[1, 2, 3, 4, 5, 6, 7, 8] [1, 5, 2, 6, 3, 7, 4, 8]
True [1, 2, 3, 4, 5, 6, 7, 8] Expected result
out items
When performing a perfect rif le shuf le, also known as the Faro shuf le, the list of items is split in
two equal sized halves, either conceptually or in actuality. The irst two elements of the result are
then the irst elements of those halves. The next two elements of the result are the second elements
of those halves, followed by the third elements of those halves, and so on up to the last elements of
those halves. The parameter out determines whether this function performs an out shuf le or an in
shuf le that determines which half of the deck the alternating card is irst taken from.
'''

def riffle(items, out=True):
    if out:
        return [x for y in zip(items[:len(items)//2], items[len(items)//2:]) for x in y]
    else:
        return [x for y in zip( items[len(items)//2:], items[:len(items)//2]) for x in y]

print(riffle([1, 2, 3, 4, 5, 6, 7, 8], out=True))
print(riffle([1, 2, 3, 4, 5, 6, 7, 8], out=False))
print(riffle([], out=True))
print(riffle(['bob', 'jack'], out=False))

