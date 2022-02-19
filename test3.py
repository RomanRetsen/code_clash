from random import randint

def sort_quick(the_list):
    perform_quick_sort(0, the_list, 0, len(the_list) - 1)

def perform_quick_sort(prt, the_list, first, last):
    if first < last:
        split_point = partition(prt, the_list, first, last)
        perform_quick_sort(prt + 1, the_list, first, split_point - 1)
        perform_quick_sort(prt + 1, the_list, split_point + 1, last)

def partition(prt, the_list, first, last):
    split_index = first
    split_value = the_list[split_index]
    first += 1
    while first <= last:
        # print(first, last)
        if the_list[first] > split_value and the_list[last] < split_value:
            the_list[first], the_list[last] = the_list[last], the_list[first]
            first += 1
            last -= 1
        elif the_list[first] <= split_value:
            first += 1
        elif the_list[last] >= split_value:
            last -= 1
    the_list[split_index], the_list[last] = the_list[last], the_list[split_index]
    # print("\t" * prt, the_list)
    return last


the_list = [randint(1, 100) for _ in range(20)]
# the_list = [3,4,6,5]
print(the_list)
print( sorted(the_list))
sort_quick(the_list)
print(the_list)
