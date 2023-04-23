from memory_profiler import memory_usage
import random
import time

def bubble_sort(input_list:list):
    len_list = len(input_list)
    for i in range(len_list):
        for y in range(len_list - i - 1):
            if input_list[y+1] < input_list[y]:
                input_list[y], input_list[y+1] = input_list[y+1], input_list[y]
    return input_list

def insert_sort(input_list):
    len_list = len(input_list)
    for targeted_index in range(1, len_list):
        targeted_element = input_list[targeted_index]
        iter_index = targeted_index - 1
        while iter_index >= 0 and input_list[iter_index] > targeted_element:
            input_list[iter_index + 1] = input_list[iter_index]
            iter_index -= 1
        input_list[iter_index + 1] = targeted_element
    return input_list

def select_sort(input_list):
    len_list = len(input_list)
    for i in range(len_list):
        current_min_index = i
        for y in range(i+1, len_list):
            if input_list[y] < input_list[current_min_index]:
                current_min_index = y
        input_list[i], input_list[current_min_index] = input_list[current_min_index], input_list[i]
    return input_list


def merge_sorting_v1_memory_test():
    input_list = [x for x in range(1000, 0)]
    merge_sorting_v1(input_list)

#merge sorting
def merge_sorting_v1(input_list):
    if len(input_list) > 1:
        # print('Splitting ', input_list)
        middle_mark = len(input_list) // 2
        left_list = input_list[:middle_mark]
        right_list = input_list[middle_mark:]
        merge_sorting_v1(left_list)
        merge_sorting_v1(right_list)

        left_index = right_index = general_index = 0

        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] < right_list[right_index]:
                input_list[general_index] = left_list[left_index]
                left_index += 1
                general_index += 1
            else:
                input_list[general_index] = right_list[right_index]
                right_index+= 1
                general_index += 1

        while left_index < len(left_list):
            input_list[general_index] = left_list[left_index]
            left_index += 1
            general_index += 1

        while right_index < len(right_list):
            input_list[general_index] = right_list[right_index]
            right_index += 1
            general_index += 1
        # print('list after merging', input_list)


def merge_sorting_v2_memory_test():
    input_list = [x for x in range(10000000, 0)]
    recursive_split_array(input_list, 0, len(input_list))

def merge_sorting_v2(input_list):
    recursive_split_array(input_list, 0, len(input_list))
    # return input_list

def recursive_split_array(input_array_chunk, start, end):
    # print(f"start {start}; end {end}")
    if (end - start) > 1:
        middle = (start + end) // 2
        recursive_split_array(input_array_chunk, start, middle)
        recursive_split_array(input_array_chunk, middle,  end)
        stitch_array(input_array_chunk, start, middle, end)

def stitch_array(input_array_chunk, start, middle, end):
    left_list = input_array_chunk[start:middle]
    right_list = input_array_chunk[middle:end]
    left_list_length = len(left_list)
    right_list_length = len(right_list)
    general_index = start
    left_index = right_index= 0


    while left_index < left_list_length and right_index < right_list_length:
        if left_list[left_index] < right_list[right_index]:
            # print(f"general index {general_index} {input_array_chunk}")
            input_array_chunk[general_index] = left_list[left_index]
            left_index += 1
            general_index += 1
        else:
            # print(f"general index {general_index} {input_array_chunk}")
            input_array_chunk[general_index] = right_list[right_index]
            right_index += 1
            general_index += 1
    while left_index < left_list_length:
        input_array_chunk[general_index] = left_list[left_index]
        left_index += 1
        general_index += 1
    while right_index < right_list_length:
        input_array_chunk[general_index] = right_list[right_index]
        general_index += 1
        right_index += 1




my_list = [random.randint(1, 1000) for x in range(1000000)]
# my_list = [14, 343, 264, 363, 996, 583, 381, 474]
# print(my_list)
# print(f"Sorted natevly: {sorted(my_list)}")
# print(f"bubble sort   : {bubble_sort(my_list[:])}")
# print(f"insert sort   : {insert_sort(my_list[:])}")
# print(f"selection sort: {select_sort(my_list[:])}")

t2 = time.time()
print(f"merge sort v2    : {merge_sorting_v2(my_list[:])}")
t3 = time.time()
print(f"time needed for new merge sort {t3-t2}")
t0 = time.time()
print(f"merge sort v1   : {merge_sorting_v1(my_list[:])}")
t1 = time.time()
print(f"time needed for old merge sort {t1 - t0}")