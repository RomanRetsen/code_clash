'''
Nearest smaller element
def nearest_smaller(items):
Given a list of integer items, create and return a new list of equal length so that each element has
been replaced with the nearest element in the original list whose value is smaller. If no smaller
elements exist because that element was the minimum of the original list, that element should
remain as it is in the result list. If two smaller elements exist equidistant in both directions, this
function should resolve this ambiguity by always using the smaller of these two elements.
items Expected result
[42, 42, 42] [42, 42, 42]
[42, 1, 17] [1, 1, 1]
[42, 17, 1] [17, 1, 1]
[6, 9, 3, 2] [3, 3, 2, 2]
[5, 2, 10, 1, 13, 15, 14, 5,
11, 19, 22] [2, 1, 1, 1, 1, 13, 5, 1, 5,
11, 19]
[1, 3, 5, 7, 9, 11, 10, 8, 6,
4, 2] [1, 1, 3, 5, 7, 9, 8, 6, 4, 2,
1]
Side question for any combinatorics enthusiasts: starting from a random permutation of n distinct
elements, what is the expecte
'''
def nearest_smaller(items):
    return_list = [0 for _ in range(len(items))]
    for i in range(len(items)):
        left = i - 1
        right = i + 1
        current = items[i]
        while left >= 0 and right <= len(items) - 1:
            if (pair_min := min((items[left], items[right])) ) < current:
                return_list[i] = pair_min
                break
            left -= 1
            right += 1
        else:
            while left >= 0:
                if items[left] < current:
                    # return_list[i] = items[left]
                    current =  items[left]
                    break
                left -= 1
            while right <= len(items) - 1:
                if items[right] < current:
                    # return_list[i] = items[right]
                    current = items[right]
                    break
                right += 1
            return_list[i] = current
    return return_list




# the_list = [6, 9, 3, 2]
# the_list = [42, 42, 42]
# the_list = [42, 1, 17]
# the_list = [42, 17, 1]
# the_list = [5, 2, 10, 1, 13, 15, 14, 5, 11, 19, 22]
the_list = [1, 3, 5, 7, 9, 11, 10, 8, 6, 4, 2]
print(nearest_smaller(the_list))
