import random
import time

#buble sorting
list_to_sort = [random.randint(1,100) for _ in range(10000)]
list_for_buble_sort = list_to_sort[:]
list_for_insert_sort = list_to_sort[:]
list_for_merge_sort = list_to_sort[:]
list_for_native_sort = list_to_sort[:]
list_for_selection_sort = list_to_sort[:]
list_for_quicksort_v1 = list_to_sort[:]
list_for_quicksort_v2 = list_to_sort[:]
print(list_to_sort)

t0 = time.time()
list_for_native_sort.sort()
t1 = time.time()
print(f'native sorting operation counter. time spent {t1-t0}')
print(list_for_native_sort)


t1 = time.time()
buble_operation_counter = 0
for i in range(len(list_for_buble_sort)):
    needed_to_correct = False
    for j in range(len(list_for_buble_sort) - i - 1):
        buble_operation_counter += 1
        if list_for_buble_sort[j] > list_for_buble_sort[j + 1]:
            list_for_buble_sort[j + 1], list_for_buble_sort[j] = list_for_buble_sort[j], list_for_buble_sort[j + 1]
            needed_to_correct = True
    if not needed_to_correct:
        break
t2 = time.time()

print(f'buble sorting operation counter {buble_operation_counter}. time spent {t2-t1}')
print(list_for_buble_sort)

t2 = time.time()
#insertion sorting
insert_operation_counter = 0
for i in range(1, len(list_for_insert_sort)):
    key = list_for_insert_sort[i]
    go_down_index = i - 1
    while go_down_index >= 0 and list_for_insert_sort[go_down_index] > key:
        insert_operation_counter += 1
        list_for_insert_sort[go_down_index + 1] = list_for_insert_sort[go_down_index]
        go_down_index -= 1
    list_for_insert_sort[go_down_index + 1] = key

t3 = time.time()
print(f'insert sorting operation counter {insert_operation_counter}. time spent {t3-t2}')
print(list_for_insert_sort)

#selection sort
def select_sort(input_list):
    for i in range(len(input_list)):
        min_index = i
        for y in range(i+1, len(input_list)):
            if input_list[y] < input_list[min_index]:
                min_index = y
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]


#merge sorting
def merge_sorting(input_list):
    if len(input_list) > 1:
        # print('Splitting ', input_list)
        middle_mark = len(input_list) // 2
        left_list = input_list[:middle_mark]
        right_list = input_list[middle_mark:]
        merge_sorting(left_list)
        merge_sorting(right_list)

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

t3 = time.time()
merge_sorting(list_for_merge_sort)
t4 = time.time()
print(f'merge sorting operation counter. time spent {t4-t3}')
print(list_for_merge_sort)

#selection sort
t4 = time.time()

for i in range(len(list_for_selection_sort)):
    cycle_min = i
    for y in range(i+1, len(list_for_selection_sort)):
        if list_for_selection_sort[y] < list_for_selection_sort[cycle_min]:
            cycle_min = y
    if cycle_min != i:
        list_for_selection_sort[i], list_for_selection_sort[cycle_min] = \
            list_for_selection_sort[cycle_min], list_for_selection_sort[i]
t5 = time.time()
print(f'selection sorting. time spent {t5-t4}')
print(list_for_selection_sort)

#quick sort using extra lists

def quicksort_v1(input_list):
    if len(input_list) < 2:
        return input_list
    else:
        pivot = input_list[0]
        left_side = [x for x in input_list[1:] if x <= pivot]
        right_side = [x for x in input_list[1:] if x > pivot]
        return quicksort_v1(left_side) + [pivot] + quicksort_v1(right_side)

t6 = time.time()
print(quicksort_v1(list_for_quicksort_v1))
t7 = time.time()
print(f'Quick sort NOT in place sorting(wastefull) {t7-t6}')

#quick sort with in place sorting

def partition(inputlist, start, end):
    edge = start - 1
    pivot = inputlist[end]
    for i in range(start, end):
        if inputlist[i] <= pivot:
            edge += 1
            inputlist[i], inputlist[edge] = inputlist[edge], inputlist[i]

    inputlist[edge + 1], inputlist[end] = inputlist[end], inputlist[edge + 1]
    return (edge + 1)

def quicksort_v2(inputlist, start, end):
    if len(inputlist) < 2 :
        return inputlist
    if start < end:
        pivot = partition(inputlist, start, end)
        quicksort_v2(inputlist, start, pivot -1)
        quicksort_v2(inputlist, pivot + 1, end)

t8 = time.time()
quicksort_v2(list_for_quicksort_v2, 0, len(list_for_quicksort_v2)-1)
print(list_for_quicksort_v2)
t9 = time.time()
print(f'Quick sort in place sorting (good version) {t9-t8}')
