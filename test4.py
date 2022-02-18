from random import randint


def bubble_sort(in_list):
    n = 0
    for i in range(len(in_list)):
        for y in range(len(in_list) - i - 1):
            n += 1
            if in_list[y] > in_list[y+1]:
                temp = in_list[y+1]
                in_list[y+1] = in_list[y]
                in_list[y] = temp

    print(f"bubble_sort took {n}")

def bubble_sort2(in_list):
    n = 0
    do_swap = True
    for i in range(len(in_list) - 1, 0, -1):
        if do_swap:
            do_swap = False
            for y in range(i):
                n += 1
                if in_list[y] > in_list[y+1]:
                    do_swap = True
                    temp = in_list[y+1]
                    in_list[y+1] = in_list[y]
                    in_list[y] = temp
        else:
            break
    print(f"bubble_sort2 took {n}")

def selection_sort(in_list):
    for i in range(len(in_list)-1):
        swap_index = 0
        for y in range(1, len(in_list)-i):
            if in_list[swap_index] < in_list[y]:
                swap_index = y
        else:
            temp = in_list[y]
            in_list[y] = in_list[swap_index]
            in_list[swap_index] = temp

def insert_sort_v2(in_list):
    for i in range(1, len(in_list)):
        temp = in_list[i]
        place_index = i
        for y in range(i, 0, -1):
            if in_list[y-1] > temp:
                in_list[y] = in_list[y-1]
                place_index = y-1
            else:
                break
        in_list[place_index] = temp

def merge_sort(in_list):
    l = len(in_list)
    if l > 1:
        l_side = in_list[:l//2]
        r_side = in_list[l//2:]
        general_index = 0
        l_index = 0
        r_index = 0
        merge_sort(l_side)
        merge_sort(r_side)
        while l_index < len(l_side) and r_index < len(r_side):
            print(f"in_list is {in_list}")
            if l_side[l_index] < r_side[r_index]:
                in_list[general_index] = l_side[l_index]
                l_index += 1
                general_index += 1
            else:
                in_list[general_index] = r_side[r_index]
                r_index += 1
                general_index += 1
        else:
            while l_index < len(l_side):
                in_list[general_index] = l_side[l_index]
                general_index += 1
                l_index += 1
            while r_index < len(r_side):
                in_list[general_index] = r_side[r_index]
                general_index += 1
                r_index += 1





# the_list = [randint(1, 100) for _ in range(5)]
the_list = [51, 92, 52, 76,80,93,100]
# the_list2 = the_list[:]
# print(the_list)
# bubble_sort(the_list)
# merge_sort(the_list2)
# print(the_list)
# print(the_list2)

print(bubble_sort([randint(0, 100) for x in range(10000)]))