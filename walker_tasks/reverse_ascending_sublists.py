'''
Reverse ascending sublists
def reverse_ascending_sublists(items):
Create and return a new list that contains the same elements as the items list argument, but where
the order of the elements inside every maximal strictly ascending sublist has been reversed. Note
the modi ier “strictly” used in the previous sentence to require each element to be greater than the
previous element, not merely equal to it.
As is the case with all functions found in this problem collection, this function should not modify the
contents of the original items list, but create and return a brand new list object that contains the
result, no matter how tempting it might be to perform this operation in place in the original list to
save memory. If you want to use the original items as the starting point of computation, you can
always assign items=items[:] in the irst line of your function to create a separate but equal
copy of the items, to operate on that copy instead of the original from that point onwards.
items Expected result
[1, 2, 3, 4, 5] [5, 4, 3, 2, 1]
[5, 7, 10, 4, 2, 7, 8, 1, 3] [10, 7, 5, 4, 8, 7, 2, 3, 1]
[5, 4, 3, 2, 1] [5, 4, 3, 2, 1]
[5, 5, 5, 5, 5] [5, 5, 5, 5, 5]
[1, 2, 2, 3] [2, 1, 3, 2]
In the table below, different colours highlight the maximal strictly ascending sublists for readability,
and are not part of the actual argument object given to the Python function.
'''
def reverse_ascending_sublists(items):
    if len(items) == 0:
        return []
    else:
        result = []
        temp = [items[0], ]
        current = items[0]
        for item in items[1:]:
            if item > current:
                temp.append(item)
                current = item
            else:
                result.extend(reversed(temp))
                temp.clear()
                temp.append(item)
                current = item
        else:
            if len(temp):
                result.extend(reversed(temp))
    return result

# items = [1,2,3,4,5] # [5, 4, 3, 2, 1]
items = [5, 7, 10, 4, 2, 7, 8, 1, 3] # [10, 7, 5, 4, 8, 7, 2, 3, 1]
# items = [5, 4, 3, 2, 1] # [5, 4, 3, 2, 1]
# items = [5, 5, 5, 5, 5] # [5, 5, 5, 5, 5]
# items = [1, 2, 2, 3] [2, 1, 3, 2]


print(reverse_ascending_sublists(items))