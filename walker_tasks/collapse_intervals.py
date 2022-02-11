'''
Collapse positive integer intervals

def collapse_intervals(items):
This function is the inverse of the previous problem of expanding positive integer intervals. Given a
nonempty list of positive integer items guaranteed to be in sorted ascending order, create and
return the unique description string where every maximal sublist of consecutive integers has been
condensed to the notation first-last. Such encoding doesn’t actually save any characters when
first and last differ by only one. However, it is usually more important for the encoding to be
uniform than to be pretty. As a general principle, uniform and consistent encoding of data allows the
processing of that data to also be uniform in the tools down the line.
If some maximal sublist consists of a single integer, it must be included in the result string all by
itself without the minus sign separating it from the now redundant last number. Make sure that
the string returned by your function does not contain any whitespace characters, and that it does
not have a silly redundant comma hanging at the end.
'''
def collapse_intervals(items):
    return_list = []
    start = current = items[0]
    for number in items[1:]:
        if number - current == 1:
            current = number
        else:
            if start == current:
                return_list.append(start)
            else:
                return_list.append(f"{start}-{current}")
            start  = current = number
    else:
        if start == current:
            return_list.append(start)
        else:
            return_list.append(f"{start}-{current}")
    return ",".join([str(x) for x in return_list])


# the_list = [1, 2, 4, 6, 7, 8, 9, 10, 12, 13] # 1-2,4,6-10,12-13
# the_list = range(1,1000001) # 1-1000000
# the_list = [42] # 42
the_list = [3, 5, 6, 7, 9, 11, 12, 13] # 3,5-7,9,11-13
print(collapse_intervals(the_list))