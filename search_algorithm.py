from time import time
import random


def find_x(x, input_list):
    for index, i in enumerate(input_list):
        if x == i:
            return index
    return -1

def find_x_binary_search(x, input_list):
    a = 0
    b = len(input_list)-1
    steps_counter = 0
    temp_list = sorted([(index, x) for index,x in zip(range(len(input_list)), input_list)], key=lambda x:x[1])
    while a <= b:
        steps_counter += 1
        k = (a+b) // 2
        if temp_list[k][1] == x:
            print(f'Search steps counter: {steps_counter}')
            return temp_list[k][0]
        if temp_list[k][1] > x:
            # b = temp_list[k-1][1]
            b = k-1
        else:
            # a = temp_list[k+1][1]
            a = k + 1
    return -1

def find_x_binary_search_step(x, input_list):
    n = len(input_list)
    temp_list = sorted([(index, x) for index,x in zip(range(n), input_list)], key=lambda x:x[1])
    step = int(n/2)
    k = 0
    steps_counter = 0
    while step >= 1:
        while (k+step) < n and temp_list[k+step][1] <= x:
            steps_counter += 1
            k += step
        step = int(step / 2)
    print(f'Search steps counter: {steps_counter}')
    if temp_list[k][1] == x:
        return temp_list[k][0]
    else:
        return -1


my_list = list(range(1,10000001))
random.shuffle(my_list)
print(f'Original list: {my_list}')
search_number = random.randint(1,10000000)
t0 = time()
print(f'index of 1234 is {find_x(search_number, my_list)}')
t1 = time()
print(f'Time needed to find number: {t1-t0}')
print(f'index of 1234 is {find_x_binary_search(search_number, my_list)}')
t2 = time()
print(f'Time needed to find number with binary search: {t2-t1}')
print(f'index of number is {find_x_binary_search_step(search_number, my_list)}')
t3 = time()
print(f'Time needed to tind number: {t3-t2}')
